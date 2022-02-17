import math
from math import radians, cos, sin, asin, sqrt
'''
文件说明:
计算gps点距离 & 计算卡口camera与路线之间的垂直距离函数
'''

from geopy.distance import distance
import geopy
def geodistance2(lng1,lat1,lng2,lat2):

    coords_1 = (float(lat1), float(lng1))
    coords_2 = (float(lat2), float(lng2))
    from geographiclib.geodesic import Geodesic
    #以M为单位显示

    #print(geopy.distance.geodesic(coords_1, coords_2).m)
    #以KM为单位显示
    #print(geopy.distance.geodesic(coords_1, coords_2).km)
    ret = float(geopy.distance.geodesic(coords_1, coords_2).m)
    return ret


import math


def geodistance1(lon1,lat1,lon2,lat2):


    R = 6372800  # Earth radius in meters

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2

    #print(2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a)))
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))



# 计算两点之间线段的距离
def __line_magnitude(x1, y1, x2, y2):
    lineMagnitude = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    return lineMagnitude


def point_to_line_distance(px, py,x1,y1,x2,y2):

    lng1=px
    lat1=py
    lng2=x1
    lat2=y1
    lng3=x2
    lat3=y2
    a = geodistance1(lng1,lat1,lng2,lat2)
    b = geodistance1(lng1, lat1, lng3, lat3)
    c = geodistance1(lng2, lat2, lng3, lat3)
    if c==0.0:
        c=0.00000001
    # print(a)
    # print(b)
    # print(c)

    cos_b=(c*c+a*a-b*b)/(2*a*c)

    cos_c=(b*b+c*c-a*a)/(2*b*c)

    if cos_b>=0 and cos_c>=0:

        line_magnitude = __line_magnitude(x1, y1, x2, y2)
        if line_magnitude==0:
            line_magnitude=0.00000001
        u1 = (((px - x1) * (x2 - x1)) + ((py - y1) * (y2 - y1)))
        u = u1 / (line_magnitude * line_magnitude)
        ix = x1 + u * (x2 - x1)
        iy = y1 + u * (y2 - y1)
        distance = __line_magnitude(px, py, ix, iy) *100000


    else:
        distance = 1000000
        # 投影点在线段内部, 计算方式同点到直线距离, u 为投影点距离x1在x1x2上的比例, 以此计算出投影点的坐标

    return distance





#dis = getDisPointToLine([1,-10],[0,0],[0,5])

if __name__ == '__main__':
    print(point_to_line_distance( 117.25568,31.774458000000003, 117.2555808,31.7743712, 117.2539123,
                            31.7761975) )
    # print(point_to_line_distance( 117.25568,31.774458000000003, 117.2555808,31.7743712, 117.256832,
    #                         31.7729989) )
    # print(getDisPointToLine([117.25568,31.774458000000003],[117.2555808,31.7743712],[117.2539123,31.7761975])*100000)
    # #print(__line_magnitude(117.3224344,31.7334405,117.3241534,31.7334386)*100000)
    # print(geodistance(117.3224344, 31.7334405, 117.3241534, 31.7334386))
    #
    # geodistance1(117.3224344, 31.7334405, 117.3241534, 31.7334386)