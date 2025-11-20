
import pandas as pd
import geopandas as gpd
import rasterio
import json
from shapely.geometry import LineString, MultiLineString
from tqdm import tqdm

from shapely.geometry import Point
from shapely.strtree import STRtree
from shapely.geometry import MultiPoint
from shapely.ops import snap

#function to safely sample data from a dataframe by iteration
def safe_sample(df, columns, n, label):
    """
    Safely sample n rows from the given columns of a DataFrame, retrying with decreasing sample size until data is available or n reaches 0.

    Parameters:
    df (pandas.DataFrame): The DataFrame to sample from
    columns (list): The columns to sample
    n (int): The number of samples to try for
    label (str): A label to print when sampling fails

    Returns:
    pandas.Series: A Series containing the sampled data, or an empty Series if sampling fails
    """
    while n > 0:
        try:
            return df[columns].sample(n=n, random_state=22)
        except ValueError:
            print(f"Not enough data in {label} for {n} samples, trying {n-50}")
            n -= 50
    print(f" Failed to sample any data from {label}")
    return df[columns].head(1).iloc[0:0] 

#function to identify koppen-geiger climate zone for a given canal vector
def get_koppen_climate_class(canal_dataset,koppen_class_map_json,koppen_geiger_fp):
    """
    Assign Koppen Climate Class to a given canal vector.

    Parameters:
    canal_dataset (geopandas.GeoDataFrame): A GeoDataFrame containing the canal geometry.

    Returns:
    geopandas.GeoDataFrame: A GeoDataFrame with a new column ("koppen_class_code") containing the Koppen Climate Class code for each canal geometry.

    Notes:
    The function uses the Koppen Climate Map data to assign the Koppen Climate Class to each canal geometry. The Koppen Climate Class is based on the Koppen Climate Classification system, which is a widely used climate classification classification system.

    """
    with open(koppen_class_map_json, 'r') as f:
        koppen_climate_map = json.load(f)
    koppen_data = rasterio.open(koppen_geiger_fp)
    
    canal_dataset_withKoppen = canal_dataset.copy()
    def startpoint(line):
        
        if isinstance(line, LineString):
            coords = list(line.coords)
        elif isinstance(line, MultiLineString):
            # flatten into a single coordinate list
            coords = [pt for seg in line.geoms for pt in seg.coords]
        else:
            raise ValueError("Geometry is neither LineString nor MultiLineString")
        return coords[0]
    canal_dataset_withKoppen["koppen_class_code"] = pd.NA
    # canal_dataset_withKoppen["koppen_class_desc"] = pd.NA
    error_count = 0
    for idx, row in tqdm(canal_dataset_withKoppen.iterrows(), total=canal_dataset_withKoppen.shape[0], desc="Assigning Koppen Climate Class"):
        try:
            first_coord = startpoint(row.geometry)
            # print(first_coord)
            koppen_value = koppen_data.sample([(first_coord[0], first_coord[1])])
            koppen_value = int(list(koppen_value)[0])
            koppen_string = str(koppen_value)

            koppen_desc = koppen_climate_map[koppen_string]
            canal_dataset_withKoppen.at[idx, "koppen_class_code"] = koppen_desc
            # canal_dataset_withKoppen.at[idx, "koppen_class_desc"] = koppen_desc
        except:
            error_count = error_count + 1
            continue
    return canal_dataset_withKoppen


#function to add a unique grain id to each canal vector
def add_GRAIN_id(final_canal_gdf, country_iso, hydrobasin_l6_file):
    """
    Function to add a unique grain id to each canal vector based on the country and the pfaf id.

    Parameters
    ----------
    final_canal_gdf : GeoDataFrame
        GeoDataFrame containing the canal geometry
    country_iso : str
        ISO code of the country

    Returns
    -------
    GeoDataFrame
        GeoDataFrame with an additional column "grain_id" containing the unique grain id for each canal vector.
    """
    basins = gpd.read_parquet(hydrobasin_l6_file)[["PFAF_ID", "geometry"]]
    basins = basins.to_crs(final_canal_gdf.crs)
    print(country_iso)
    canals = gpd.sjoin(
        final_canal_gdf,
        basins,
        predicate="intersects",       
        how="left"                    
    ).rename(columns={"PFAF_ID": "pfaf_id"})

   
    canals = canals.dropna(subset=["pfaf_id"])
    canals["pfaf_id"] = canals["pfaf_id"].astype(int)
    canals["id_counter"] = canals.groupby("pfaf_id").cumcount() + 1
    
    canals["id_counter_str"] = canals["id_counter"].apply(lambda n: f"{n:05d}")

    canals["grain_id"] = (
        country_iso + "_" +
        canals["pfaf_id"].astype(str) + "_" +
        canals["id_counter_str"]
    )

    return canals


#helper functions to extract OSM tags
def get_osm_name(tags):
    """
    Helper function to extract the OSM name from the tags.

    Parameters
    ----------
    tags : str
        A string containing the OSM tags.

    Returns
    -------
    str
        The OSM name extracted from the tags, or None if not found.
    """
    if tags is None:
        return None
    try:
        tag_dict_str = tags
        tag_dict = json.loads(tag_dict_str)
        if "name" not in tag_dict.keys():
            return None
        else:
            return tag_dict["name"]
    except:
        return None
    

def get_osm_source(tags):
    
    """
    Helper function to extract the OSM source from the tags.

    Parameters
    ----------
    tags : str
        JSON string containing the OSM tags

    Returns
    -------
    str
        OSM source name if found, None otherwise
    """
    if tags is None:
        return None
    try:
        tag_dict_str = tags
        tag_dict = json.loads(tag_dict_str)
        if "source:name" not in tag_dict.keys():
            return None
        else:
            return tag_dict["source:name"]
    except:
        return None

def get_osm_name_fromOtherTags(other_tags):
    
    """
    Helper function to extract the OSM name from the other tags.

    Parameters
    ----------
    other_tags : str
        A string containing the other tags.

    Returns
    -------
    str
        The OSM name extracted from the other tags, or None if not found.
    """
    if other_tags is None:
        return None
    try:
        tag_raw = other_tags.split(",")
        tag_dict_str = {}
        for item in tag_raw:
            key, value = item.strip('"').split('"=>"', 1)
            tag_dict_str[key] = value
        # tag_dict = json.loads(tag_dict_str)
        if "name:en" not in tag_dict_str.keys():
            return None
        else:
            return tag_dict_str["name:en"]
    except:        
        return None
    
# functions to extract endpoints
def get_endpoints(geom):
    """
    Helper function to extract the endpoints from a LineString or MultiLineString.

    Parameters
    ----------
    geom : shapely.geometry.LineString or shapely.geometry.MultiLineString
        The geometry from which to extract the endpoints

    Returns
    -------
    tuple of 2 shapely.geometry.Point
        The endpoints of the geometry, or (None, None) if the geometry type is not supported
    """
    if geom.geom_type == 'LineString':
        return Point(geom.coords[0]), Point(geom.coords[-1])
    elif geom.geom_type == 'MultiLineString':
        parts = geom.geoms
        return Point(parts[0].coords[0]), Point(parts[-1].coords[-1])
    return None, None