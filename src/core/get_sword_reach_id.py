import geopandas as gpd
import warnings

warnings.filterwarnings("ignore")
def get_sword_reach(canal_vector, projection='4326'):
    """
    Function to get SWORD reach IDs for all Hydrobasins for a given canal geometry.
    Hydrobasins L2 shapefiles merged for the whole globe are used, and the PFAF ID is utilized as the identifier field.
    
    Parameters:
    canal_vector (GeoDataFrame): A GeoDataFrame containing the canal geometry.
    projection (str): The coordinate reference system of the canal geometry. Default is 'EPSG4326'.
    Returns:
    sword_reach_id (list): List of SWORD reach IDs for the specified canal geometry.
    """

    #buffer the canal vector and create a new gdf
    canal_vector = canal_vector.buffer(0.1)
    canal_vector_gdf = gpd.GeoDataFrame(geometry=canal_vector)
    #specifying hydrobasins folder path and format. Note: Change this to your local path. Logic for projection based path is included.    
    hydrobasins_path = '../assets/supporting_data/hydrobasins_allBasins_l2_geoParquet_EPSG{}.parquet'
    country_shapefiles_path = '../assets/supporting_data/world-administrative-boundaries.geojson'
    if projection != '4326':
        hydrobasins_path = hydrobasins_path.format(projection)
    else:
        hydrobasins_path = hydrobasins_path.format('4326')

    # Load the hydrobasins data
    hydrobasins = gpd.read_parquet(hydrobasins_path)

    # Load the country shapefiles
    country_shapefiles = gpd.read_file(country_shapefiles_path)
    #convert country shapefiles to the same projection as the canal vector
    country_shapefiles = country_shapefiles.to_crs(f'epsg:{projection}')

    country_subset = country_shapefiles[['iso3','name','continent', 'geometry']]
    #obtain country that interesects with canal_vector and change 'name' to 'country'
    country_subset = country_subset.rename(columns={'name': 'country'})
    intersection_country_canal = gpd.sjoin(canal_vector_gdf, country_subset, how='inner', predicate='intersects')
    country_name = intersection_country_canal['country'].unique().tolist()
    country_iso = intersection_country_canal['iso3'].unique().tolist()
    continent = intersection_country_canal['continent'].unique().tolist()
    print('Country detected:', country_name, "ISO:", country_iso)

    intersection_hydrobasins_country = gpd.sjoin(hydrobasins, country_subset.loc[country_subset['country'] == country_name[0]], how='inner', predicate='intersects')
    num_of_level_2_hydrobasins = intersection_hydrobasins_country['PFAF_ID'].nunique()
    print(f'Number of level 2 hydrobasins in {country_name[0]}: {num_of_level_2_hydrobasins}')
    print('PFAF_IDs:', intersection_hydrobasins_country['PFAF_ID'].unique().tolist())
    print('returning pfaf ids as sword reach ids')
    sword_reach_id = intersection_hydrobasins_country['PFAF_ID'].unique().tolist()

    return country_iso, country_name, continent, sword_reach_id