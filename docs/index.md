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

  /* Dataset version history popup next to the Zenodo link */
  .grain-versions {
    position: relative;
    display: inline-block;
    vertical-align: middle;
  }
  .md-typeset .grain-versions-toggle {
    display: inline-flex;
    padding: 0.1rem;
    color: #a8a8a8;
    cursor: pointer;
    transition: color 0.2s;
  }
  .md-typeset .grain-versions-toggle:hover,
  .md-typeset .grain-versions-toggle[aria-expanded="true"] {
    color: #808080;
  }
  .grain-versions-toggle svg {
    width: 0.85rem;
    height: 0.85rem;
    fill: currentColor;
  }
  .grain-versions-menu {
    position: absolute;
    right: 0;
    top: calc(100% + 0.25rem);
    z-index: 10;
    display: block;
    min-width: 17rem;
    padding: 0.5rem 0.8rem;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.2rem;
    background: var(--md-default-bg-color);
    box-shadow: var(--md-shadow-z2);
    text-align: left;
    font-size: 0.65rem;
    font-style: normal;
    line-height: 1.5;
    white-space: nowrap;
  }
  .grain-versions-menu[hidden] {
    display: none;
  }
  .grain-versions-head {
    display: block;
    margin-bottom: 0.3rem;
    font-weight: 700;
  }
  .grain-versions-row {
    display: flex;
    gap: 0.8rem;
    padding: 0.15rem 0;
  }
  .grain-versions-row b {
    min-width: 2.2rem;
  }
  .grain-versions-date {
    color: var(--md-default-fg-color--light);
  }

  /* Visualizer preview card shown when hovering the "GRAIN Visualizer" link */
  .viz-hover {
    position: relative;
    display: inline-block;
  }
  .viz-hover-card {
    position: absolute;
    top: calc(100% + 0.4rem);
    left: 0;
    z-index: 20;
    width: 26rem;
    max-width: 80vw;
    aspect-ratio: 1905 / 912;
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.8rem;
    overflow: hidden;
    background: var(--md-default-fg-color--lightest);
    box-shadow: var(--md-shadow-z3);
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.2s, visibility 0.2s;
  }
  /* Invisible strips over the gap above and below the link, so moving the pointer
     from the link into the card doesn't close it */
  .viz-hover:hover::before,
  .viz-hover:hover::after {
    content: "";
    position: absolute;
    left: 0;
    right: 0;
    height: 0.6rem;
  }
  .viz-hover:hover::before {
    bottom: 100%;
  }
  .viz-hover:hover::after {
    top: 100%;
  }
  /* Set by the script when there isn't room below the link */
  .viz-hover-card--above {
    top: auto;
    bottom: calc(100% + 0.4rem);
  }
  .viz-hover:hover .viz-hover-card,
  .viz-hover:focus-within .viz-hover-card {
    opacity: 1;
    visibility: visible;
    transition-delay: 0.15s;
  }
  .viz-hover-card img {
    display: block;
    width: 100%;
    height: 100%;
  }
  .md-typeset .viz-hover-label {
    position: absolute;
    left: 50%;
    bottom: 0.6rem;
    transform: translateX(-50%);
    padding: 0.25rem 0.8rem;
    border-radius: 1rem;
    background: rgba(0, 0, 0, 0.65);
    color: #fff;
    font-size: 0.6rem;
    font-weight: 600;
    white-space: nowrap;
  }

  /* Light grey "NEW" notice box under the hero image */
  .md-typeset .admonition.success {
    border-color: var(--md-default-fg-color--lightest);
    background-color: rgba(0, 0, 0, 0.035);
    box-shadow: none;
  }

  /* Publication cards: whole card links to the paper */
  /* Light grey hover shades for the publication cards */
  :root {
    --pub-hover-border: rgba(0, 0, 0, 0.14);
    --pub-hover-bg: rgba(0, 0, 0, 0.035);
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
<a href="https://doi.org/10.5281/zenodo.23067127" target="_blank">10.5281/zenodo.23067127</a>
<span class="grain-versions">
<button type="button" class="grain-versions-toggle" aria-haspopup="true" aria-expanded="false" title="Version history"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.5 8H12v5l4.28 2.54.72-1.21-3.5-2.08V8M13 3a9 9 0 0 0-9 9H1l3.96 4.03L9 12H6a7 7 0 0 1 7-7 7 7 0 0 1 7 7 7 7 0 0 1-7 7c-1.93 0-3.68-.79-4.94-2.06l-1.42 1.42A8.896 8.896 0 0 0 13 21a9 9 0 0 0 9-9 9 9 0 0 0-9-9Z"/></svg></button>
<span class="grain-versions-menu" hidden>
<span class="grain-versions-head">Version history</span>
<span class="grain-versions-row"><b>v.1.1</b><span class="grain-versions-date">2026-09-30</span><a href="https://doi.org/10.5281/zenodo.23067127" target="_blank">10.5281/zenodo.23067127</a></span>
<span class="grain-versions-row"><b>v.1.0</b><span class="grain-versions-date">2025-08-09</span><a href="https://doi.org/10.5281/zenodo.16786488" target="_blank">10.5281/zenodo.16786488</a></span>
</span>
</span></span>
</p>

!!! success ""
    <span style="font-size:0.8rem;"><span style="color:#c00000; font-weight:700;">NEW:</span> The <span class="viz-hover"><a href="https://uw-saswe.github.io/GRAIN-Visualizer/" target="_blank"><strong>GRAIN Visualizer</strong></a><a class="viz-hover-card" href="https://uw-saswe.github.io/GRAIN-Visualizer/" target="_blank" tabindex="-1" aria-hidden="true"><img data-src="./images/grain_visualizer_preview.webp" alt=""><span class="viz-hover-label">Click to visit ↗</span></a></span> website is now LIVE.</span>

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

  // Visualizer hover card: the animation is only downloaded on the first hover
  document.querySelectorAll(".viz-hover").forEach((wrap) => {
    const card = wrap.querySelector(".viz-hover-card");
    const img = card.querySelector("img");
    const show = () => {
      if (!img.getAttribute("src")) img.src = img.dataset.src;
      vizPlaceCard(wrap, card);
    };
    wrap.addEventListener("mouseenter", show);
    wrap.addEventListener("focusin", show);
  });

  // Keep the whole card on screen: open above the link when there's no room below,
  // shift it sideways off the window edges, and shrink it if neither side has room.
  // The sticky header and footer count as off-screen.
  function vizPlaceCard(wrap, card) {
    const margin = 8;
    const ratio = 1905 / 912;
    card.style.width = "";
    card.style.left = "";
    card.classList.remove("viz-hover-card--above");

    const link = wrap.getBoundingClientRect();
    const header = document.querySelector(".md-header");
    const footer = document.querySelector(".md-footer");
    const top = (header ? header.getBoundingClientRect().bottom : 0) + margin;
    const bottom = Math.min(window.innerHeight, footer ? footer.getBoundingClientRect().top : Infinity) - margin;
    const spaceBelow = bottom - link.bottom;
    const spaceAbove = link.top - top;

    const above = card.offsetHeight > spaceBelow && spaceAbove > spaceBelow;
    card.classList.toggle("viz-hover-card--above", above);
    const space = (above ? spaceAbove : spaceBelow) - margin;
    if (card.offsetHeight > space) card.style.width = Math.max(space, 0) * ratio + "px";

    const right = document.documentElement.clientWidth - margin;
    let shift = 0;
    if (link.left + card.offsetWidth > right) shift = right - (link.left + card.offsetWidth);
    if (link.left + shift < margin) shift = margin - link.left;
    card.style.left = shift + "px";
  }

  // Dataset version history popup: toggle on the icon, close on any click outside it
  function grainCloseVersions() {
    document.querySelectorAll(".grain-versions").forEach((box) => {
      box.querySelector(".grain-versions-menu").hidden = true;
      box.querySelector(".grain-versions-toggle").setAttribute("aria-expanded", "false");
    });
  }

  document.addEventListener("click", (event) => {
    const toggle = event.target.closest(".grain-versions-toggle");
    if (toggle) {
      const menu = toggle.closest(".grain-versions").querySelector(".grain-versions-menu");
      const opening = menu.hidden;
      grainCloseVersions();
      menu.hidden = !opening;
      toggle.setAttribute("aria-expanded", String(opening));
      return;
    }
    if (!event.target.closest(".grain-versions-menu")) grainCloseVersions();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      pubCloseMenus();
      grainCloseVersions();
    }
  });
</script>

<p style="text-align:left; font-size:0.8rem; margin-top:1.2rem;">
Codebase:
<a href="https://github.com/UW-SASWE/GRAIN/" target="_blank"><b>GRAIN GitHub Page</b></a>
</p>
