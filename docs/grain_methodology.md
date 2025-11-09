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

<h4> GRAIN Methodology </h4>
<div class="grain-intro">
The end-to-end overview of the workflow used in the creation of the GRAIN dataset is shown in the flowchart below. The process starts with the extraction of the OSM data for countries having significant irrigated land, based on the FAO Global Irrigation Area v.5. dataset. Waterway features such as rivers, canals, stream, and drain, are then extracted from this country scale OSM data. 
<br><br>These features then serve as input to a machine learning (ML) classifier trained to distinguish man-made irrigation canals from natural watercourses. The classification is supported by in-situ canal data, SWORD river centreline dataset , and land use/land cover (LULC) information from ESA’s CCI product to identify non-agricultural channels. The output is a pre-validated canal dataset that undergoes statistical validation using both manually delineated canal maps and curated in-situ datasets from multiple regions. Finally, validated canal segments are assigned various metadata, to produce the final GRAIN dataset.
</div>

![Image title](./images/grain_workflow.png){ align=center }

