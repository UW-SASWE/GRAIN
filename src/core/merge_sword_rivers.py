import geopandas as gpd
import os
import pandas as pd
import networkx as nx
import networkx as nx

from shapely.geometry import LineString, MultiLineString, GeometryCollection
from shapely.ops import unary_union, linemerge
from shapely import box

def merge_lines(geoms):
    """Return one LineString (or MultiLineString) from a listlike of lines."""
    u = unary_union(list(geoms))          # may be LineString OR MultiLineString

    if isinstance(u, LineString):
        return u                          # already a single continuous line
    elif isinstance(u, MultiLineString):
        return linemerge(u)               # stitch connected pieces
    elif isinstance(u, GeometryCollection):
        # keep only the linear parts, then merge
        lines = [g for g in u.geoms if isinstance(g, (LineString, MultiLineString))]
        return linemerge(lines)
    else:
        raise ValueError(f"Unexpected geometry type: {u.geom_type}")

def str2list(cell):
    return [] if pd.isna(cell) else [x for x in str(cell).split() if x.lower() != "nan"]

def merge_sword_rivers(sword_data):
    DG = nx.DiGraph()
    for _, row in sword_data.iterrows():
        rid = str(row["reach_id"])
        DG.add_node(rid, **row.to_dict())

        for dn in str2list(row["rch_id_dn"]):
            DG.add_edge(rid, dn)      # direction: upstream -> downstream

    # outlets: nodes with out-degree 0
    outlets = [n for n in DG if DG.out_degree(n) == 0]

    records = []
    for o in outlets:
        river_nodes = nx.ancestors(DG, o) | {o}
        sub = sword_data[sword_data["reach_id"].astype(str).isin(river_nodes)]

        merged_geom = merge_lines(sub.geometry.values)   # ← use helper

        records.append({
            "outlet_id":  o,
            "reach_ids":  list(river_nodes),
            "mean_width": sub["width"].mean(),
            "mean_slope": sub["slope"].mean(),
            "tot_length": sub["reach_len"].sum(),
            "geometry":   merged_geom
        })

    river_gdf = gpd.GeoDataFrame(records, crs=sword_data.crs)

    return river_gdf
