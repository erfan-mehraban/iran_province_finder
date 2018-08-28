from .provinces_polygons import *
from shapely.geometry import Point

def find(latitude, longtitude):
    """ return name of province correspond to longtitude and latitude """
    point = Point(_convert_x(longtitude), _convert_y(latitude))
    for polygon, name in province:
        if polygon.contains(point):
            return name
    return NOT_FOUND

def _convert_x(longtitude):
    """ convert longtitude to x """
    return 59.171632911 * longtitude + -2574.341811146

def _convert_y(latitude):
    """ convert latitude to y """
    return -68.75659401 * latitude + 2782.239846283