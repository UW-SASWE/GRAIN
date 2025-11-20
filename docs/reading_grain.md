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

<h4>Reading and Visualizing GRAIN Data</h4>

<div class="grain-intro">

The GRAIN dataset is distributed as vector geospatial files in both <code>.parquet</code> and <code>.shp</code> formats.  
These files contain the irrigation canal geometries and associated metadata fields such as canal length, slope, use type, country name, and more.

This page provides a quick guide on how to visualize GRAIN canal datasets using  
<b>(I) Python and GeoPandas</b> and <b>(II) QGIS</b>.  
Both methods are suitable for exploring, styling, and inspecting the irrigation canal networks.

</div>


---



<div class="grain-intro">
<b>I. Visualizing GRAIN Using Python + GeoPandas</b><br>
GeoPandas provides a simple Python interface for loading and plotting GRAIN canal files.  
You may use either the GeoParquet or Shapefile versions of the dataset.

Below is an example of viewing the GRAIN canals for Egypt.

</div>

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Example file path (modify based on your folder structure)
grain_fp = "./GRAIN_sample_data_EGYPT/sample_outputs/egypt_GRAIN_v1_0.parquet"

# Load the dataset
grain_gdf = gpd.read_parquet(grain_fp)

# Basic info
print(grain_gdf.head())
print(grain_gdf.crs)

#Filter for only Agricultural Canals
grain_irrigation_canals = grain_gdf[grain_gdf["canal_use"] == "Agricultural"]

# Quick visualization
plt.figure(figsize=(8,8))
grain_irrigation_canals.plot(linewidth=0.6, color="blue")
plt.title("GRAIN Irrigation Canals - Egypt")
plt.show()
```
![Viz Python - 1](../images/egypt_viz_python_1.png){ align=center }

<div class="grain-intro">
<br> For interactive visualization, the <code>.explore()</code> method of GeoPandas can be used.  
This renders an interactive Leaflet map directly inside a Jupyter notebook, allowing you to zoom, pan, and inspect canal features.
</div>

```python
# Interactive map using GeoPandas
grain_irrigation_canals.explore()
```

![Viz Python - 1](../images/egypt_viz_python_2.png){ align=center }


<div class="grain-intro">
<br>
<b>II. Visualizing GRAIN in QGIS</b><br>
QGIS provides a graphical environment for exploring and styling the GRAIN dataset. 
Both <code>.parquet</code> and <code>.shp</code> formats can be loaded directly.

<br><br><b>Step 1 — Open QGIS</b><br>
Create a new empty project.

<br><br><b>Step 2 — Load GRAIN data</b><br>
You can load the dataset using either method:
<ul>
  <li><b>Drag-and-drop</b> the <code>.parquet</code> or <code>.shp</code> file into the QGIS window</li>
  <li>Or use the <b>Browser</b> panel and double-click the file</li>
</ul>
Once loaded, the canal network will appear as a polyline layer.

<br><br><b>Step 3 — Style the canals</b><br>
Right-click the layer → <b>Properties</b> → <b>Symbology</b>.<br>
You may:
<ul>
  <li>Change line color and thickness</li>
  <li>Use <b>Categorical</b> styling on <code>canal_use</code></li>
  <li>Use <b>Graduated</b> styling on attributes like <code>length_KM</code> or <code>slope_mkm</code></li>
</ul>

<br><b>Step 4 — View canal metadata</b><br>
Open the attribute table to explore fields such as:
<ul>
  <li><code>grain_id</code> – unique canal identifier</li>
  <li><code>length_KM</code></li>
  <li><code>slope_mkm</code></li>
  <li><code>elev_diff_M</code></li>
  <li><code>canal_use</code></li>
  <li><code>confidence</code> (ML prediction score)</li>
  <li><code>koppen_class_code</code></li>
</ul>
These attributes can be used for filtering, map styling, and spatial analysis.
</div>

![Viz Python - 1](../images/egypt_viz_qgis.png){ align=center }