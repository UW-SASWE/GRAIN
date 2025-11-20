<style>
  .md-typeset h1,
  .md-content__button {
    display: none;
  }
    /* Justify the main paragraph text */
  .grain-intro {
    text-align: justify;
    text-justify: inter-word;
    font-size: 0.7rem; 
    line-height: 1.3;
    margin-top: -0.6rem;
  }

</style>

<h4>Reproduction of GRAIN Workflow</h4>

<div class="grain-intro">

This page outlines the process to recreate GRAIN data for the country of Egypt. The same process may be used to generate GRAIN canals for any country by changing the related input files <br>  

<br>Provided in the GRAIN Git repository is a python jupyter notebook titled 'GRAIN_sample_workflow.ipynb', which has been set up to be run cell by cell to generate the GRAIN data. It can be found in <a href="https://github.com/UW-SASWE/GRAIN/tree/main/src/sample_workflow"> src->sample_workflow.</a><br>

<br><b>I.Python Environment set up</b><br>
<br>All python modules required to run the workflow notebook is listed in the grain_environment.yml file. The .yml file can be used with either mamba or conda to create the environment using the following bash command:
</div>

``` bash
conda env create -f grain_environment.yml #(1)!
```

1. :exclamation: This command requires a working installation of conda or mamba (Python environment managers) on your machine.

<div class="grain-intro">
<br><b>II.Prerequisite Data</b><br>
<br> The sample workflow requires some pre-requisite data such as OpenStreetMap(OSM) data for Egypt, the trained grain ML model, and other supporting datasets to run. They have been hosted on Zenodo and needs to be downloaded and unzipped into the sample_workflow folder.<br>   
<br>Zenodo Link: <a href="https://zenodo.org/records/17608198" >https://zenodo.org/records/17608198</a>

<br><br>The following Bash command can also be used for the same:
</div>

``` bash
cd src/sample_workflow
curl -L -o GRAIN_sample_data_EGYPT.zip "https://zenodo.org/records/17608198/files/GRAIN_sample_data_EGYPT.zip?download=1"
unzip GRAIN_sample_data_EGYPT.zip
```
<div class="grain-intro">
<br>Once the file has been downloaded and unzipped, ensure that there is now a folder named GRAIN_sample_data_EGYPT inside the sample_workflow folder.<br>
<br><b>III.Running GRAIN sample workflow python</b><br>
<ul>
<li>Open the GRAIN_sample_workflow.ipynb jupyter notebook and set the kernel to the GRAIN python environment that contains the required modules.
<li> Run <b>cell [3]</b> ##imports to import all the required modules. Ensure that the python scripts feature_engineering.py, and GRAIN_helper_functions.py is present in the sample_workflow folder.
<li><b>Cell [4]</b> may be run to ignore any kind of warnings that might be outputted. This is optional.
<li><b>Cell [5]</b> contains specification of the file and folder paths to all the required pre-requsite data. Ensure that the data has been downloaded as provided in step II, and that the GRAIN_sample_data_EGYPT folder is present in sample_workflow.
</ul>
</div>

```python
## File paths for input data

egypt_osm_waterways_fp = './GRAIN_sample_data_EGYPT/egypt_waterway.parquet' #(1)!
ml_model_fp = './GRAIN_sample_data_EGYPT/ML_model_random_forest.pkl'
sword_data_folder = './GRAIN_sample_data_EGYPT/SWORD_v16_shp/'
sword_fileName_format = '{}_sword_reaches_hb{}_v16.shp'
hydrobasins_l2_folder = './GRAIN_sample_data_EGYPT/HydroBasins_world_L2'
hydrobasin_l6_file = './GRAIN_sample_data_EGYPT/hydrobasins_allBasins_l6_geoParquet_EPSG4326.parquet'
hydrobasins_l2_fileName_format = 'hybas_{}_lev02_v1c.shp'
world_countries_filePath = './GRAIN_sample_data_EGYPT/world-administrative-boundaries.geojson'

sword_continent_map = './GRAIN_sample_data_EGYPT/sword_continents.json'
koppen_class_map = './GRAIN_sample_data_EGYPT/koppen_class_label.json'
koppen_geiger_fp = './GRAIN_sample_data_EGYPT/koppen_geiger_0p00833333.cog'
dem_cog_fp = './GRAIN_sample_data_EGYPT/dem_data/World_e-Atlas-UCSD_SRTM30-plus_v8.cog'

esa_cci_cog_path = "./GRAIN_sample_data_EGYPT/ESACCI-LC-L4-LCCS-Map-300m-P1Y-2015-v2.0.7.cog" 

##Output folder path
save_path = './GRAIN_sample_data_EGYPT/sample_outputs/' #(2)!
```

1. Check the 'Processing OSM PBF' files section at the end of this page to understand how to obtain the OSM parquet files.
2. You can change the save_path to any other folder of choice.

<div class="grain-intro">
<br>
<ul>
<li>Run <b>cells [6] and [7]</b> that declares functions to perform topology based promotion of canal segments and to assign canal use case.
<li> Run <b>cell [8]</b>. It contains the core function that runs the GRAIN ml model for a given country. Additional code may be added after line 279 of cell [8] to export the GRAIN data in further formats. For instance, if you want to export as a GeoJSON file, then add the following line.
</div>

```python
final_grain_canal_dataset.to_file(f"{save_path}/{country}_GRAIN_v.1.0.geojson", driver='GeoJSON')
```

<div class="grain-intro">
<br>
<ul>
<li>Run <b>cell [9]</b> which will call the run_grain_ml_model function. If you are recreating GRAIN data for a country other than egypt, change the country name in Line 3 of this cell.

<br><br> This should now have created the GRAIN canal files in .parquet, .shp, and other user provided formats within the folder specified in save_path.
</div>

<div class="grain-intro">
<br><b>IV.Downloading and Processing OSM PBF data</b><br>
<br> OSM data for any country not present in GRAIN or the updated data for exisiting countries can be downloaded from <a href = "https://download.geofabrik.de/"> Geofabrik.de</a>. Ensure that country level files are downloaded. These can be accessed by clicking on the continent names as shown below.
</div>

![Geofabrik](../images/geofabrik.png){ align=center }

<div class="grain-intro">
The OSM data that is provided withing the pre-requisite data folder contains only the waterways and is in .parquet format. Note that conversion to .parquet is not strictly necessary for smaller countries. However, it is highly recommended for larger OSM files due to their file size. This can be achieved as follows.
<ol>
<li> <b>Filtering for waterways:</b> Using the <a href="https://osmcode.org/osmium-tool/"> Osmium Toolkit </a> for processing OSM data. Osmium-tool is a command-line utility for filtering, converting, and extracting information from large <code>.osm.pbf</code> files efficiently.
<br><br> Once installed on your machine, the OSM data can be filtered for waterways using the following terminal command. Example shown for Egypt.
</div>

```bash
osmium tags-filter  egypt.osm.pbf w/waterway -o egypt_waterway.osm.pbf
```
<div class="grain-intro">
This file can now be converted to <code>.parquet</code> format in several ways. Note that <b>osmium-tool itself cannot export directly to Parquet</b>, as it only supports OSM-native formats (e.g., <code>.osm</code>, <code>.osc</code>, <code>.pbf</code>) and simple CSV/JSON exports. Therefore, one of the following tools must be used to convert the filtered <code>.osm.pbf</code> file into a GeoParquet file suitable for the GRAIN workflow:
</div>

<div class="grain-intro">
<ol start="2">
  <br>
  <li>
    <b>Using QGIS</b><br>
    The filtered file <code>egypt_waterway.osm.pbf</code> can be loaded into QGIS directly.  
    QGIS automatically parses OSM geometry and attributes. Once loaded:
    <ul>
      <li>Open the <i>Layers</i> panel</li>
      <li>Right-click the waterways layer → <b>Export → Save Features As…</b></li>
      <li>Select <b>GeoParquet</b> as the output format</li>
      <li>Save as <code>egypt_waterway.parquet</code></li>
    </ul>
    This is the simplest GUI-based method for conversion.
  </li>

  <li>
    <b>Using Python and <code>pyrosm</code> / GeoPandas</b><br>
    Python provides a fully programmatic way to convert OSM PBF files into GeoParquet.  
    For example:
    <pre><code class="python">
from pyrosm import OSM

osm = OSM("egypt_waterway.osm.pbf")
waterways = osm.get_data("waterways")     # Extract waterway features

# Save to GeoParquet
waterways.to_parquet("egypt_waterway.parquet")
    </code></pre>
  </li>

  <li>
    <b>Using <code>osmium-export</code> (optional)</b><br>
    Osmium provides <code>osmium export</code> to generate <code>.geojson</code> or NDJSON.  
    Although it cannot write Parquet directly, you can convert the GeoJSON output to Parquet via Python:
    <pre><code class="bash">
osmium export egypt_waterway.osm.pbf -o egypt_waterway.geojson
    </code></pre>
    Then in Python:
    <pre><code class="python">
import geopandas as gpd

gdf = gpd.read_file("egypt_waterway.geojson")
gdf.to_parquet("egypt_waterway.parquet")
    </code></pre>
    This two-step method is useful if <code>pyrosm</code> is not available.
  </li>
</ol>
</div>
