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

<h4> GRAIN Attributes </h4>
<div class="grain-intro">
The GRAIN Dataset is distributed as country-scale files in two formats, a lightweight GeoParquet format and as ESRI Shapefiles, to ensure compatibility with legacy GIS software. All files are projected to EPSG:4326 based on the WGS-84 datum as per standard geospatial data convention. The attribute scheme for each GRAIN canal is given in the table below. 
</div>

| Field | Type | Unit | Description |
| :----- | :---- | :---- | :----------- |
| **grain_id** | String | – | Unique identifier – format: `ISO3_PfafstetterL6ID_seq.numbering`. |
| **osm_id** | String | – | OpenStreetMap feature ID. |
| **country** | String | – | Country where the canal segment is located. |
| **continent** | String | – | Continent in which the canal lies. |
| **country_iso** | String | – | ISO-3 country code. |
| **length_KM** | Float | km | Canal path length. |
| **slope_mkm** | Float | m km⁻¹ | Longitudinal slope derived from SRTM DEM. |
| **elev_diff_M** | Float | m | Elevation difference between start and end points. |
| **predicted_class** | String | – | ML-classified label (`"canal"` or `"river"`). |
| **confidence** | Float | – | Prediction confidence of ML classifier (0–1). |
| **osm_label** | String | – | Original OSM waterway label. |
| **osm_name** | String | – | Canal name from OSM (if available). |
| **alt_name** | String | – | Alternate canal name detected from OSM tags. |
| **tags** | String | – | Raw OSM tags (JSON string). |
| **canal_use** | String | – | Canal use class (e.g., Agricultural, Urban, Navigation). |
| **koppen_class_code** | String | – | Köppen–Geiger climate-zone code. |
| **update_date** | String | – | Date of dataset creation or latest update. |
| **version** | String | – | GRAIN dataset release version number. |


