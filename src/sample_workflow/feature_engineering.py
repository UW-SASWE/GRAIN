#all imports
from shapely.geometry import LineString, MultiLineString
import numpy as np
import math
import traceback

def vertex_per_length(geom):
    """
    Compute the number of vertices per 100m of a LineString or MultiLineString

    Parameters:
    geom (shapely.geometry.LineString or shapely.geometry.MultiLineString): The input geometry

    Returns:
    float: The number of vertices per 100m of the input geometry, or np.nan if the input geometry is not supported

    """
    try:
        if geom.geom_type == 'LineString':
            num_vertices = len(geom.coords)
            length = geom.length
        elif geom.geom_type == 'MultiLineString':
            num_vertices = sum(len(part.coords) for part in geom.geoms)
            length = geom.length
        else:
            return np.nan  # for unsupported types

        return num_vertices / (length / 100) if length > 0 else np.nan

    except Exception:
        return np.nan


def get_straightness_ratio(geom):
    """
    Compute the straightness ratio (or sinuosity) of a LineString or MultiLineString.

    The straightness ratio is defined as the ratio of the simplified length (the length of the line connecting the start and end points) to the total length of the line.

    Parameters:
    geom (shapely.geometry.LineString or shapely.geometry.MultiLineString): The input geometry

    Returns:
    float: The straightness ratio of the input geometry, or np.nan if the input geometry is not supported

    """
    try:
        # Handle MultiLineString by combining all coordinates
        if geom.geom_type == 'MultiLineString':
            # print("MultiLineString")
            coords = [pt for line in geom.geoms for pt in line.coords]
            # print(coords)
        else:
            coords = list(geom.coords)

        if len(coords) > 3:
            start = coords[0]
            end = coords[-1]
            mid = coords[len(coords) // 2]

            # print(start, mid, end)

            dist1 = math.dist(start, mid)
            dist2 = math.dist(mid, end)
            simplified_length = dist1 + dist2
        else:
            start = coords[0]
            end = coords[1]
            simplified_length = math.dist(start, end)
        
        total_length = geom.length
        # print(total_length)
        sinousity = simplified_length / total_length # if total_length > 0 else np.nan
        
        # print("Simplified length:", simplified_length, "Total length:", total_length, "Sinousity:", sinousity)
        return sinousity

    except Exception as e:
        # print(f"Error: {e}")
        return np.nan


def mean_turning_angle(geom):
    """
    Compute the mean turning angle of a LineString or MultiLineString.

    The mean turning angle is the average of all angles between consecutive segments of the input geometry.

    Parameters:
    geom (shapely.geometry.LineString or shapely.geometry.MultiLineString): The input geometry

    Returns:
    float: The mean turning angle of the input geometry, or np.nan if the input geometry is not supported
    """
    
    def angle_at_b(a, b, c):
        """
        Compute the angle between two vectors ba and bc.

        Parameters:
        a (tuple): Coordinates of the first point
        b (tuple): Coordinates of the second point
        c (tuple): Coordinates of the third point

        Returns:
        float: The angle in degrees between the two vectors
        """
        ba = (a[0] - b[0], a[1] - b[1])
        bc = (c[0] - b[0], c[1] - b[1])
        dot = ba[0]*bc[0] + ba[1]*bc[1]
        det = ba[0]*bc[1] - ba[1]*bc[0]
        angle = math.atan2(abs(det), dot)
        return (180 - angle*180/math.pi)

    try:
        if geom.geom_type == "MultiLineString":
            coords = [pt for line in geom.geoms for pt in line.coords]
            coords = [coords[i] for i in range(len(coords)) if i == 0 or coords[i] != coords[i-1]]

        else:
            coords = list(geom.coords)

        if len(coords) < 3:
            return 0

        angles = [
            angle_at_b(coords[i - 1], coords[i], coords[i + 1])
            for i in range(1, len(coords) - 1)
        ]
        mean_turn_angle = np.mean(angles) if len(angles) > 0 else 0
        # print(mean_turn_angle)
        return mean_turn_angle
        
    except Exception:
        return np.nan


def get_curvature_index(geom):
    

    """
    Compute the curvature index of a LineString or MultiLineString.

    The curvature index is the sum of all angles between consecutive segments of the input geometry,
    divided by the total length of the input geometry in 100m units.

    Parameters:
    geom (shapely.geometry.LineString or shapely.geometry.MultiLineString): The input geometry

    Returns:
    float: The curvature index of the input geometry, or np.nan if the input geometry is not supported
    """
    
    def angle_at_b(a, b, c):
        # Convert to vectors
        """
        Compute the angle between two vectors ba and bc.

        Parameters:
        a (tuple): Coordinates of the first point
        b (tuple): Coordinates of the second point
        c (tuple): Coordinates of the third point

        Returns:
        float: The angle in degrees between the two vectors
        """
        ba = (a[0] - b[0], a[1] - b[1])
        bc = (c[0] - b[0], c[1] - b[1])
        # Dot and cross products
        dot = ba[0]*bc[0] + ba[1]*bc[1]
        det = ba[0]*bc[1] - ba[1]*bc[0]

        # Angle in radians
        angle = math.atan2(abs(det), dot)
        # print(angle)
        return(180 - angle*180/math.pi)
        # return angle  # Always positive

    try:
        # Flatten coords
        if geom.geom_type == "MultiLineString":
            coords = [pt for line in geom.geoms for pt in line.coords]
            #removing duplicates
            coords = [coords[i] for i in range(len(coords)) if i == 0 or coords[i] != coords[i-1]]
            # print(coords)
            # print(len(coords))
            # print(type(coords))
        else:
            # print("LineString")
            coords = list(geom.coords)
            # print(coords)
            # print(type(coords))
        

        if len(coords) < 3:
            return 0

        angles = [
            angle_at_b(coords[i - 1], coords[i], coords[i + 1])
            for i in range(1, len(coords) - 1)
        ]
        # print(angles)
        total_angle_change = sum(angles)
        if geom.geom_type == 'LineString':
            num_vertices = len(geom.coords)
        elif geom.geom_type == 'MultiLineString':
            # num_vertices = sum(len(part.coords) for part in geom.geoms)
            num_vertices = len(coords)
            
        line_length_100m = geom.length / 100  # assuming EPSG:3857
        # print(line_length_100m)
        # return total_angle_change / (num_vertices-1)
        return total_angle_change / line_length_100m if line_length_100m > 0 else 0

    except Exception as e:
        print("Error: {}".format(e))
        traceback.print_exc()
        return np.nan


