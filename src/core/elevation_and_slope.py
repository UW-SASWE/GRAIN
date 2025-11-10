import numpy as np
import geopandas as gpd
import rasterio
from rasterio.sample import sample_gen
from shapely.geometry import LineString, MultiLineString
from tqdm import tqdm
import pandas as pd

def compute_elevDiff_and_slope(dem_cog_fp, country_grain_gdf):
    """
    compute slope and elevation difference between two points using SRTM dem.

    parameters:
        dem_cog_fp: string - path to the dem cog file
        country_grain_gdf: geopandas dataframe containing the grain/osm canal data.
    
    returns:
        gdf with two new columns: elevation difference and slope
        elevation difference = abs(end_elevation - start_elevation)
        slope = (end_elevation - start_elevation) / length
    
    """
    
    #defining local helper function to return endpoint and start point of a canal
    def endpoints(line):
        """Return (x0, y0), (x1, y1) for LineString or MultiLineString."""
        if isinstance(line, LineString):
            coords = list(line.coords)
        elif isinstance(line, MultiLineString):
            # flatten into a single coordinate list
            coords = [pt for seg in line.geoms for pt in seg.coords]
        else:
            raise ValueError("Geometry is neither LineString nor MultiLineString")
        return coords[0], coords[-1]


    #reading the dem cog file
    dem = rasterio.open(dem_cog_fp)
    
    country_grain_gdf = country_grain_gdf.to_crs(epsg=4326)
    for col in ['start_el', 'end_el', 'elev_diff', 'slope']:
        country_grain_gdf[col] = pd.NA

    counter = 0
    error_counter = 0
    for idx, row in tqdm(country_grain_gdf.iterrows(),
                                  total= country_grain_gdf.shape[0],
                                  desc="Computing slopes"):
        p0, p1 = endpoints(row.geometry)

        try:
            z_iter = sample_gen(dem, [p0, p1], indexes=1, masked=False)
            (z0,), (z1,) = list(z_iter)
        
            diff   = np.abs(z0 - z1) #z1 - z0
            slope  = diff / row.length #m/km
        
        except:
            diff = 0
            slope = 0
            error_counter += 1
            continue
        # print(row.id,"coord elevs:",z1, z0,"elev diff:", diff, "length(km):",row.length,"slope:", slope)
        
        country_grain_gdf.at[idx, "start_el"]  = z0
        country_grain_gdf.at[idx, "end_el"]    = z1
        country_grain_gdf.at[idx, "elev_diff"] = diff
        country_grain_gdf.at[idx, "slope"]     = slope

        counter +=1
        
    print("Errors in slope computation:",error_counter)
    return country_grain_gdf
                          
    #computing the slope and elevation difference for each canal
    