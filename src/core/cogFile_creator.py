import rasterio
import numpy as np
from rio_cogeo import cogeo, profiles
from rio_cogeo.profiles import cog_profiles
from pathlib import Path

src = Path("path_to_tif_file.tif")
dst = Path("output_path_for_cog_file.cog")

profile = cog_profiles.get("deflate")           # preset with DEFLATE + overviews
profile.update(dict(BLOCKSIZE=512))  

with rasterio.open(src) as src_ds:
    cogeo.cog_translate(
        src_ds,
        dst,
        profile,
        nodata=src_ds.nodata,
        overview_level=5,     # build down to 1/32 resolution
        web_optimized=False,  # leave False unless you need 256-pixel web tiles
    )

print("✔  COG written to", dst)