<img src="./assets/images/gitRepo_cover.png" alt="logo" width="1000" height="auto">



## Global Registry of Agricultural Irrigation Networks
GRAIN is an OpenStreetMap (OSM) based dataset of the world's irrigation canals. OSM country-scale data is retrieved from [Geofrabrik.de](https://www.geofabrik.de/), processed using [OSMium CLI Toolkit](https://osmcode.org/osmium-tool/), and [QGIS](https://qgis.org/) to filter for waterways and to convert the OSM PBF file to the lightweight cloud optimised GeoParquet format. 

A Random Forest classifier, trained on 20,000 samples of rivers and canal geometry, is used to differentiate between man-made canals and natural rivers to correct tagging issues prevalent in OSM data. Canal use type is determined using [ESA CCI Land Cover](https://www.esa-landcover-cci.org/) dataset. Validation is done on in-stu canal network data obtained from national and regional scale government datasets, and manually delineated canal vector data. 

Dataset is available for download at [Zenodo - GRAIN v.1.0](https://doi.org/10.5281/zenodo.16786487) <br>
GRAIN is made available as country level files in GeoParquet and ESRI shapefile formats. All GRAIN files are projected to EPSG:4326, based on the WGS-84 datum. Users are recommended to download the GeoParquet files due to the significant smaller file size.

The methodology and validation is described in : [Suresh, S., Hossain, F., Mishra, V., Hossain, N., 2025. GRAIN - Global Registry of Agricultural Canal Networks, Earth System Science Data](https://www.earth-system-science-data.net/) <b style="color:orange;">*Submitted for review</b>

### Documentation
Users are encouraged to refer to the
[GRAIN Documentation](https://grain-canals.readthedocs.io/en/latest/) website for information on reading and visualizing GRAIN, general methodology, recreating GRAIN data, GRAIN attribute schema etc.

### Issues and Feedback

We welcome feedback, bug reports, and suggestions for improvements.

**Issue Tracker:** Please use the [GitHub Issues](../../issues) page to report:
  - Bugs or data errors
  - Missing canal networks in specific regions with prevalent OSM data
  - Feature requests (e.g., new attributes, processing steps)
  - Questions about data usage

When reporting a bug or data issue, please include:
- The **country/region** affected
- The **GRAIN version** you are using
- A **clear description** of the issue
- Screenshots, shapefiles, or links to reference data (if available)

---

### Contributing to GRAIN

GRAIN is designed as a **community-driven dataset**.  
We encourage contributions from researchers, GIS specialists, and citizen scientists.

#### How to Contribute
1. **Fork** the repository and create a new branch for your changes.
2. Make your changes:
   - Improve code in `/src`
   - Add new validation data by providing a link to the data in a text file in `/assets/validation`
3. **Test** your changes locally to ensure nothing is broken.
4. Submit a **pull request** with:
   - A short description of the changes
   - Links to any supporting data or references
   - Clear notes if the changes affect dataset structure or methodology

#### Contribution Ideas
- Adding new **regional validation datasets**.
- Improving the **classification pipeline** or adding new ML features.
- Creating **notebooks** that showcase GRAIN applications.

For large contributions (e.g., major processing changes, new metadata fields), please open an **issue first** so we can discuss and coordinate.

---

### Contact

For general inquiries or collaboration requests, please contact:

**Sarath Suresh**  
Graduate Research Assistant, SASWE Research Group  
University of Washington  
✉️ Email: saraths@uw.edu  
🔗 [LinkedIn](https://www.linkedin.com/in/sarathsuresh96/)


