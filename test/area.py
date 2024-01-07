""" Generalization of patterns """
from math import pi, sqrt

def area_square(r):
    return area(r,1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3*sqrt(3) / 2)

""" We are able to generalize all these functions by finding a common pattern"""
def area(r, shape_constant):
    assert r > 0, 'A length must be > 0'
    return r * r * shape_constant