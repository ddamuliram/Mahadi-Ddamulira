__author__ = 'mahadi'
from dimvaldate import *
from numpy import*


def calculate_perimeter_regular_hexagon(side_length: Number) -> Number:
    """
    Calculate perimeter of a regular hexagon.

    @param side: the side of a hexagon
    @return: the perimeter (same units as side)

    >>> calculate_perimeter_regular_hexagon(2)
    10
    """
    if dim_validate(side_length):
        return 6*side_length
    elif type(side_length) == str:
        raise TypeError("value is a string")
    else:
        raise ValueError("side is less than 0: "+str(side_length))
print(calculate_perimeter_regular_hexagon(5))


def calculate_perimeter_regular_pentagon(side_length):
    """
    calculates the perimeter of a regular pentagon given one of the sides.
    @param side:side of the pentagon
    @return:perimeter of a regular pentagon(same units as side)

    >>> calculate_perimeter_regular_pentagon(3)
    15
    """
    if dim_validate(side_length):
        return 5*side_length
    elif type(side_length) == str:
        raise TypeError("value is a string")
    else:
        raise ValueError("side is less than o:"+str(side_length))
print(calculate_perimeter_regular_pentagon(4))


def calculate_area_circle(radius):
    """
    calculates area of a circle given the radius of that circle.
    @param radius:radius of the circle
    @return:area of the circle(in square units)

    >>> calculate_area_circle(7)
    153.93804002589985
    """
    if dim_validate(radius):
        return pi *radius*radius
    elif type(radius) == str:
        raise TypeError("value is a string")
    else:
        raise ValueError("radius is less than0:"+str(radius))
print(calculate_area_circle(4))

def calculate_volume_sphere(radius):
    """
    calculates the volume of a sphere given its radius.
    @param radius:radius of the sphere
    @return:volume of the sphere(in cubic units)

    >>> calculate_volume_sphere(1)
    4.1887902047863905
    """
    if dim_validate(radius):
        return 4/3*pi*radius**3
    elif type(radius) == str:
        raise TypeError("value is a string")
    else:
        raise ValueError("radius is less than o:"+str(radius))
print(calculate_volume_sphere(3))

def calculate_area_rectangle(length, width):
    """
    calculates the area of a rectangle given length and width.
    @param length:length of the rectangle
    @param width:width of the rectangle
    @return:the area of a rectangle(in square units)

    >>> calculate_area_rectangle(5,6)
    30
    """
    if dim_validate(length, width):
        return length*width
    elif type(length) == str or type(width) == str:
        raise TypeError("value is a string")
    else:
        raise ValueError("length is less than 0:")
print(calculate_area_rectangle(4, 3))

def calculate_surface_area_cylinder(radius, height):
    """
    calculates the area of a cylinder provided the radius and the
    height are given.both variables should have the same unit.
    @param radius:radius of the cylinder
    @param height:height of the cylinder
    @return:the area of a triangle(in units squared)

    >>> calculate_surface_area_cylinder(7, 2)
    395.84067435231395
    """
    if dim_validate(radius, height):
        return 2*pi*radius*(radius + height)
    elif type(radius)==str or type(height) == str:
        raise TypeError("value is a string")
    else:
        raise ValueError("radius is less than 0:")
print(calculate_surface_area_cylinder(5, 10))

def calculate_area_right_angled_triangle(base, height):
    """
    calculates the area of a triangle given the base and height of that triangle.
    @param base: base of the triangle
    @param height: height of the triangle
    @return:area of triangle(in square units)

    >>> calculate_area_right_angled_triangle(4,8)
    16.0
    """
    if dim_validate(base, height):
        return base*height/2
    elif type(base)==str or type(height)==str:
        raise TypeError("value is a string")
    else:
        raise ValueError("base is less than o:")
print(calculate_area_right_angled_triangle(3, 2))


def calculate_surface_area_right_circular_cone(radius, height):
    """
    calculates the surface area of a cone given the radius and height.
    @param radius:radius of the cone
    @param height:height of the cone
    @return:surface area of the cone(in square units)

    >>> calculate_surface_area_right_circular_cone(7,4)
    331.2363480197146
    """
    if dim_validate(radius, height):
        return pi*radius*(radius+((height**2)+(radius**2))**0.5)
    elif type(radius)==str or type(height)==str:
        raise TypeError("value is a string")
    else:
        raise ValueError("radius is less than 0:")
print(calculate_surface_area_right_circular_cone(2, 3))

def calculate_volume_cuboid(length, width, height):
    """
    calculates the volume of a cuboid provided its length,width and height are given.
    @param length:length of the cuboid
    @param width: width of the cuboid
    @param height: height of the cuboid
    @return:volume of the the cuboid(in cubic units)

    >>> calculate_volume_cuboid(10,4,5)
    200
    """
    if dim_validate(length, width, height):
        return length*width*height
    elif type(length)==str or type(width)== str or type(height)==str:
        raise TypeError("value is a string")
    else:
        raise ValueError("length is less than 0:")
print(calculate_volume_cuboid(2, 4, 5))

def calculate_volume_right_pyramid(length=None, width=None, height=None):
    """
    calculates the volume of the pyramid provided the length,width and height of pyramid are given.
    @param length: length of the pyramid
    @param width: width of the pyramid
    @param height:height of the pyramid
    @return:volume of the pyramid(in cubic units)

    >>> calculate_volume_right_pyramid(10,20,30)
    2000.0
    """
    if dim_validate(length, width, height):
        return length*width*height/3
    elif type(length)==str or type(width)==str or type(height)==str:
        raise TypeError("value is a string")
    else:
        raise ValueError("length is less than 0:")
print(calculate_volume_right_pyramid(2,4,3))