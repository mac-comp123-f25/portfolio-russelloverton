from math import ceil

def estimate_green_roof(wid, len, sqf_cost):
    area = rect_area(wid, len)
    cost = roof_cost(area, sqf_cost)
    print(" Area =", area)
    print(" Cost =", cost)

def rect_area(wid, len):
    return ceil(wid) * ceil(len)

def roof_cost(area, sqf_cost):
    return area * sqf_cost

estimate_green_roof(54.25, 32.8, 35)