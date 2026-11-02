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

  /* Publication cards: whole card links to the paper */
  /* Light grey hover shades for the publication cards */
  :root {
    --pub-hover-border: rgba(0, 0, 0, 0.14);
    --pub-hover-bg: rgba(0, 0, 0, 0.035);
  }
  [data-md-color-scheme="slate"] {
    --pub-hover-border: rgba(255, 255, 255, 0.16);
    --pub-hover-bg: rgba(255, 255, 255, 0.05);
  }
  .pub-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
    gap: 0.8rem;
    margin-top: 0.6rem;
  }
  /* One card per row; remove "pub-cards--single" from the div to go back to side by side */
  .pub-cards--single {
    grid-template-columns: 1fr;
  }
  .pub-card {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 0.6rem 0.9rem;
    padding: 0.8rem 1rem;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.3rem;
    font-size: 0.7rem;
    line-height: 1.4;
    transition: box-shadow 0.2s, border-color 0.2s;
  }
  .pub-card:hover {
    border-color: var(--pub-hover-border);
    box-shadow: var(--md-shadow-z2);
  }
  /* Cover + text; clicking it opens the paper */
  .md-typeset a.pub-link {
    flex: 1 1 18rem;
    display: flex;
    align-items: center;
    gap: 0.9rem;
    color: var(--md-default-fg-color);
  }
  /* Keep the theme's green link hover off the card text */
  .md-typeset a.pub-link:hover,
  .md-typeset a.pub-link:focus {
    color: var(--md-default-fg-color);
  }
  /* Citation button with a dropdown of copy formats */
  .pub-cite {
    position: relative;
    align-self: flex-start;
    /* Pull the button up into the card's top right corner */
    margin: -0.5rem -0.6rem 0 auto;
  }
  .md-typeset .pub-cite-toggle {
    display: inline-flex;
    align-items: center;
    gap: 0.2rem;
    padding: 0.1rem 0.2rem;
    color: #a8a8a8;
    font-size: 0.55rem;
    white-space: nowrap;
    cursor: pointer;
    transition: color 0.2s;
  }
  .md-typeset .pub-cite-toggle:hover,
  .md-typeset .pub-cite-toggle[aria-expanded="true"] {
    color: #808080;
  }
  .pub-cite-toggle svg {
    width: 0.65rem;
    height: 0.65rem;
    fill: currentColor;
  }
  .pub-cite-menu {
    position: absolute;
    right: 0;
    top: calc(100% + 0.25rem);
    z-index: 10;
    min-width: 10rem;
    padding: 0.25rem 0;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.2rem;
    background: var(--md-default-bg-color);
    box-shadow: var(--md-shadow-z2);
  }
  .md-typeset .pub-cite-menu button {
    display: block;
    width: 100%;
    padding: 0.35rem 0.8rem;
    text-align: left;
    color: var(--md-default-fg-color);
    font-size: 0.6rem;
    white-space: nowrap;
    cursor: pointer;
  }
  .md-typeset .pub-cite-menu button:hover {
    background: var(--pub-hover-bg);
  }
  .pub-card .pub-title {
    display: block;
    font-weight: 700;
    font-size: 0.8rem;
    margin-bottom: 0.3rem;
  }
  .pub-card .pub-meta {
    display: block;
    color: var(--md-default-fg-color--light);
  }
  /* Journal name in the site's link color */
  .pub-card .pub-meta i {
    color: var(--md-typeset-a-color);
  }
  /* Journal cover thumbnail; fixed box so every cover renders at the same size */
  .md-typeset .pub-card img.pub-logo {
    flex: 0 0 3.6rem;
    width: 3.6rem;
    height: 4.65rem;
    object-fit: cover;
    border-radius: 0.2rem;
    box-shadow: var(--md-shadow-z1);
  }

</style>


<img src="./images/landing_heropic_1.png" alt="logo" width="1000" height="auto">
<p style="text-align:right">
<i>Current Version – <b>v.1.1</b></i><br>
<span style="font-size:0.8rem;"><b>Dataset (v.1.1):</b>
<a href="https://doi.org/10.5281/zenodo.23067127" target="_blank">10.5281/zenodo.23067127</a></span>
</p>

!!! success ""
    <span style="font-size:0.8rem;"><span style="color:#c00000; font-weight:700;">NEW:</span> The <strong>[GRAIN Visualizer](https://uw-saswe.github.io/GRAIN-Visualizer/)</strong> website is now LIVE.</span>

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

</div>

<h4>Related Publications</h4>

<div class="pub-cards pub-cards--single">

<div class="pub-card">
<a class="pub-link" href="https://essd.copernicus.org/articles/18/1855/2026/" target="_blank">
<img class="pub-logo" src="./images/essd_cover.jpg" alt="Earth System Science Data cover">
<span>
<span class="pub-title">GRAIN – a Global Registry of Agricultural Irrigation Networks</span>
<span class="pub-meta">Suresh, S., Hossain, F., Mishra, V., &amp; Hossain, N. (2026)</span>
<span class="pub-meta"><i>Earth System Science Data</i></span>
</span>
</a>
<div class="pub-cite">
<button type="button" class="pub-cite-toggle" aria-haspopup="true" aria-expanded="false"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 21H8V7h11m0-2H8a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2m-3-4H4a2 2 0 0 0-2 2v14h2V3h12V1Z"/></svg><span class="pub-cite-label">Cite</span></button>
<div class="pub-cite-menu" hidden>
<button type="button" data-cite="essd" data-format="apa">Copy as text (APA)</button>
<button type="button" data-cite="essd" data-format="bibtex">Copy as BibTeX</button>
</div>
</div>
</div>

<div class="pub-card">
<a class="pub-link" href="https://doi.org/10.1029/2026GL124090" target="_blank">
<img class="pub-logo" src="./images/grl_cover.jpg" alt="Geophysical Research Letters cover">
<span>
<span class="pub-title">How well can the Surface Water and Ocean Topography (SWOT) satellite mission observe irrigation canals?</span>
<span class="pub-meta">Sharma, M., Hossain, F., Suresh, S., Pavelsky, T. M., Minocha, S., &amp; Khan, S. (2026)</span>
<span class="pub-meta"><i>Geophysical Research Letters</i></span>
</span>
</a>
<div class="pub-cite">
<button type="button" class="pub-cite-toggle" aria-haspopup="true" aria-expanded="false"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 21H8V7h11m0-2H8a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h11a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2m-3-4H4a2 2 0 0 0-2 2v14h2V3h12V1Z"/></svg><span class="pub-cite-label">Cite</span></button>
<div class="pub-cite-menu" hidden>
<button type="button" data-cite="grl" data-format="apa">Copy as text (APA)</button>
<button type="button" data-cite="grl" data-format="bibtex">Copy as BibTeX</button>
</div>
</div>
</div>

</div>

<script>
  // Citation text copied by the publication card buttons
  const PUB_CITATIONS = {
    essd: {
      apa: "Suresh, S., Hossain, F., Mishra, V., & Hossain, N. (2026). GRAIN – a Global Registry of Agricultural Irrigation Networks. Earth System Science Data, 18, 1855–1875. https://doi.org/10.5194/essd-18-1855-2026",
      bibtex: `@article{suresh2026grain,
  title   = {{GRAIN} -- a Global Registry of Agricultural Irrigation Networks},
  author  = {Suresh, Sarath and Hossain, Faisal and Mishra, Vimal and Hossain, Nehan},
  journal = {Earth System Science Data},
  volume  = {18},
  pages   = {1855--1875},
  year    = {2026},
  doi     = {10.5194/essd-18-1855-2026}
}`
    },
    grl: {
      apa: "Sharma, M., Hossain, F., Suresh, S., Pavelsky, T. M., Minocha, S., & Khan, S. (2026). How well can the Surface Water and Ocean Topography (SWOT) satellite mission observe irrigation canals? Geophysical Research Letters, 53, e2026GL124090. https://doi.org/10.1029/2026GL124090",
      bibtex: `@article{sharma2026swot,
  title   = {How well can the Surface Water and Ocean Topography ({SWOT}) satellite mission observe irrigation canals?},
  author  = {Sharma, M. and Hossain, F. and Suresh, S. and Pavelsky, T. M. and Minocha, S. and Khan, S.},
  journal = {Geophysical Research Letters},
  volume  = {53},
  pages   = {e2026GL124090},
  year    = {2026},
  doi     = {10.1029/2026GL124090}
}`
    }
  };

  function pubCopyFallback(text) {
    const area = document.createElement("textarea");
    area.value = text;
    area.style.position = "fixed";
    area.style.opacity = "0";
    document.body.appendChild(area);
    area.select();
    document.execCommand("copy");
    area.remove();
  }

  function pubCloseMenus(except) {
    document.querySelectorAll(".pub-cite").forEach((cite) => {
      if (cite === except) return;
      cite.querySelector(".pub-cite-menu").hidden = true;
      cite.querySelector(".pub-cite-toggle").setAttribute("aria-expanded", "false");
    });
  }

  document.addEventListener("click", async (event) => {
    const toggle = event.target.closest(".pub-cite-toggle");
    if (toggle) {
      const cite = toggle.closest(".pub-cite");
      const menu = cite.querySelector(".pub-cite-menu");
      pubCloseMenus(cite);
      menu.hidden = !menu.hidden;
      toggle.setAttribute("aria-expanded", String(!menu.hidden));
      return;
    }

    const option = event.target.closest(".pub-cite-menu button");
    pubCloseMenus();
    if (!option) return;

    const text = PUB_CITATIONS[option.dataset.cite][option.dataset.format];
    try {
      await navigator.clipboard.writeText(text);
    } catch (err) {
      pubCopyFallback(text);
    }
    const label = option.closest(".pub-cite").querySelector(".pub-cite-label");
    label.textContent = "Copied!";
    setTimeout(() => { label.textContent = "Cite"; }, 1500);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") pubCloseMenus();
  });
</script>

<p style="text-align:left; font-size:0.8rem; margin-top:1.2rem;">
Codebase:
<a href="https://github.com/UW-SASWE/GRAIN/" target="_blank"><b>GRAIN GitHub Page</b></a>
</p>
