__author__ = 'mahadi'
from geom_formulae import *
from nose.tools import *

def test_calculate_area_circle_int():
    assert calculate_area_circle(7) == 153.93804002589985
    assert calculate_area_circle(14) == 615.7521601035994
    s = 7
    assert calculate_area_circle(s*2) == 4*calculate_area_circle(s)


eps = 1e-6
def test_calculate_area_circle_double():
    assert 25/4 - eps < calculate_area_circle(2.5) < 25/4 + eps

@raises(TypeError)
def test_calculate_area_circle_other():
    calculate_area_circle("a string")

def calculate_circumference_circle_int():
    s = 7
    assert calculate_circumference_circle(s) == 43.982297150257104
    assert calculate_circumference_circle(4*s) == calculate_circumference_circle(s)*4


def test_fail_calculate_circumference_circle():
    assert calculate_circumference_circle_int(4) == 20



def test_calculate_surface_area_sphere_int():
    assert calculate_surface_area_sphere(7) == 153.93804002589985
    assert calculate_surface_area_sphere(14) == 615.7521601035994
    s = 7
    assert calculate_surface_area_sphere(s*2) == 4*calculate_surface_area_sphere(s)


eps = 1e-6
def test_calculate_surface_area_sphere_double():
    assert 25/4 - eps < calculate_surface_area_sphere(2.5) < 25/4 + eps

@raises(TypeError)
def test_calculate_surface_area_sphere_other():
    calculate_surface_area_sphere("a string")

def calculate_circumference_circle_int():
    s = 7
    assert calculate_volume_sphere(s) == 43.982297150257104
    assert calculate_volume_sphere(4*s) == calculate_volume_sphere*4

