import math

def calc_angle(start_point, end_point):
    deg_to_rad = math.pi / 180
    latA = start_point[0] * deg_to_rad 
    latB = end_point[0] * deg_to_rad 
    lonA = start_point[1] * deg_to_rad 
    lonB = end_point[1] * deg_to_rad 

    delta_ratio = math.log(math.tan(latB/ 2 + math.pi / 4) / math.tan(latA/ 2 + math.pi / 4))
    delta_lon = abs(lonA - lonB)

    delta_lon %= math.pi
    bearing = math.atan2(delta_lon, delta_ratio)/deg_to_rad
    return bearing