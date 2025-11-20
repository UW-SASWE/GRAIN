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


<img src="./images/landing_heropic_1.png" alt="logo" width="1000" height="auto">
<p style="text-align:right">
<i>Current Version – <b>v.1.0.</b></i>
</p>

<h4>What is GRAIN?</h4>

<div class="grain-intro">

GRAIN (Global Registry of Agricultural Irrigation Networks) provides an open, globally consistent map of surface irrigation canals derived from OpenStreetMap (OSM) and enhanced with machine learning.
The dataset spans 95 countries and includes over 3.8 million km of canal networks, classified by use type (agricultural, urban, navigation) and validated against regional inventories.<br>  

<br>This website serves as a documentation portal for GRAIN, and contains information on the following:
<!-- 
<ul>
  <li>GRAIN Workflow and Data Sources</li>
  <li>Reproduction of GRAIN Workflow</li>
  <li>GRAIN Dataset Structure</li>
  <li>Reading and Vizualising GRAIN data</li>
  <li>Download links</li>
</ul> -->
</div>

<div class="grid cards" markdown>

-   :octicons-workflow-16:{ .lg .middle } __Methodology and Datasets Used__

    ---

    Brief details on the methodology and datasets used to generate the GRAIN dataset.

    [:octicons-arrow-right-24:](./grain_methodology.md)

-   :material-database-cog:{ .lg .middle } __Reproduce Workflow__

    ---

    Step-by-step explanation of how to recreate GRAIN data for a sample region.

    [:octicons-arrow-right-24:](./reproduce_workflow.md)

-   :material-table-of-contents:{ .lg .middle } __Dataset Structure__

    ---

    Information on the GRAIN Dataset Attribute Schema. 

    [:octicons-arrow-right-24:](./attribute_schema.md)

-   :material-language-python:{ .lg .middle } __Reading GRAIN__

    ---

    Instructions on how to read and visualize GRAIN data using Python and QGIS.

    [:octicons-arrow-right-24:](./reading_grain.md)

<br>Codebase:
<a href="https://github.com/UW-SASWE/GRAIN/" target="_blank"><b>GRAIN GitHub Page</b></a><br>
</div>

<p style="text-align:left; font-size:0.8rem; margin-top:1.2rem;">
Links to reference paper and the latest version of the GRAIN dataset: <br>
📘 <b>Reference Paper:</b> 
<a href="https://essd.copernicus.org/preprints/essd-2025-488/" target="_blank">
Suresh et&nbsp;al., 2025, <i>Earth System Science Data</i> (in review)
</a> 
<br>

💾 <b>Dataset (v1.0.0):</b> 
<a href="https://doi.org/10.5281/zenodo.16786488" target="_blank">
10.5281/zenodo.16786488
</a>

</p>





