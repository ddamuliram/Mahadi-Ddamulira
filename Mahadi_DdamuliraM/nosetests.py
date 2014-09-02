__author__ = 'mahadi'
from geom_formulae import *
from nose.tools import *

def test_pentagon_perimeter_int():
    assert pentagon_perimeter(2)==10
    assert pentagon_perimeter(4)==20
    side=6
    assert pentagon_perimeter(side*2)==2*pentagon_perimeter(6)

def test_hexagon_perimeter_():
    assert hexagon_perimeter(2)==12
    assert hexagon_perimeter(3)==18
    side=4
    assert hexagon_perimeter(side*2)==2*hexagon_perimeter(4)

def triangle_area_():
    assert triangle_area(2,2)==2
    assert triangle_area(4,6)==12
    assert triangle_area(6*8*2)==5*triangle_area(6*8)

def circle_area_():
    assert circle_area(1)==22/7
    assert circle_area(0.5)==11/14
    side=7
    assert circle_area(side*2)==4*circle_area(7)

def rectangle_area():
    assert rectangle_area(2,2)==4
    assert rectangle_area(3,4)==12
    assert rectangle_area(2*6*2)==2*rectangle_area(2*6)

def sphere_volume():
    assert sphere_volume(3)==792/7
    assert sphere_volume(1)==88/21
    assert sphere_volume(side*2)==8*sphere_volume(0.5)