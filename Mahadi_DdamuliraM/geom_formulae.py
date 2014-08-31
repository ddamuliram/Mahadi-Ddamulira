__author__ = 'mahadi'
from numpy import*

def calculate_area_circle(radius):
    """
    calculate area of a circle from the radius
    @param the radius:
    @return:the area of the circle(in square units of radius)
    >>> calculate_area_circle(7)
    153.93804002589985
    """
    return math.pi * radius ** 2
if __name__ == '__main__':
 print("Area of circle is: ", calculate_area_circle(7))


def calculate_circumference_circle(radius):
    """
    calculate circumference of a circle from radius
    @param the radius of the circle:
    @return:the circumference of the circle(the same units as the radius)
    >>> calculate_circumference_circle(7)
    43.982297150257104
    """
    return math.pi*2*radius
if __name__ == '__main__':
  print("Circumference of circle is: ", calculate_circumference_circle(7))


def calculate_surface_area_sphere(radius):
    """
    calculate surface area of a sphere from radius
    @param the radius of the sphere:
    @return:surface area of the sphere( in square units of radius)
    >>> calculate_surface_area_sphere(7)
    615.7521601035994
    """
    return math.pi*4*radius**2
if __name__ == '__main__':
  print("Surface area of  sphere is: ",calculate_surface_area_sphere(7))


def calculate_volume_sphere(radius):
    """
    calculate volume of a sphere from radius
    @param  the radius of the sphere:
    @return:volume of the sphere (in cubic units of radius)
    >>>calculate_volume_sphere(7)
    1436.7550402417319
    """
    return math.pi*4/3*radius**3
if __name__ == '__main__':
  print("Volume of sphere is: ", calculate_volume_sphere(7))


def calculate_volume_cylinder(radius, height):
    """
    calculate the volume of the cylinder from its radius and height
    @param the radius of the cylinder circular end:
    @param the height of the cylinder:
    @return:volume of the cylinder( in cubic units of radius or height)
    >>>>calculate_volume_cylinder(7,8)
    1231.5043202071988
    """
    return math.pi*radius**2*height
if __name__ == '__main__':
 print("Volume of cylinder is: ", calculate_volume_cylinder(7, 8))

def calculate_surface_area_cylinder(radius,length):
    """
    calculate the surface area of the cylinder from its radius and length
    @param  the radius of the cylinder:
    @param the length or height of the cylinder:
    @return:surface area of the cylinder(in square units of radius)
    >>>>calculate_surface_area_cylinder(7,8)
    351.85837720205683
    """
    return math.pi*2*radius*length
if __name__ == '__main__':
  print("Surface area of cylinder is: ", calculate_surface_area_cylinder(7, 8))


def calculate_surface_area_right_circular_cone(radius,slating_length):
    """
    calculate the surface area of surface area of the right circular cone from its radius and slanting length
    @param radius:
    @param slating_length:
    @return:surface area of the cone (in square units of radius)
    >>>>calculate_surface_area_right_circular_cone(7,8)
    175.92918860102841
    """
    return math.pi*radius*slating_length
if __name__ == '__main__':
 print("Surface area of right circular cone is: ", calculate_surface_area_right_circular_cone(7, 8))


def calculate_volume_cone(radius,height):
    """
calculate the volume of the cone from its radius and height
    @param radius:
    @param height:
    @return:
    >>>>calculate_volume_cone(7,8)
    410.5014400690663
    """
    return math.pi*1/3*radius**2*height
if __name__ == '__main__':
 print("Volume of cone is: ", calculate_volume_cone(7,8))



def calculate_area_rectangle(length,breadth):
    """
calculate the area of a rectangle from its length and breadth
    @param length of the rectangle:
    @param breadth of the rectangle:
    @return:area of the rectangle(in square units of length or breadth)
    >>>>calculate_area_rectangle(5,8)
    40
    """
    return length*breadth
if __name__ == '__main__':
 print("Area of rectangle is: ", calculate_area_rectangle(5, 8))




def calculate_perimeter_rectangle(length,breadth):
    """
    @param length of the rectangle:
    @param breadth of the rectangle:
    @return:perimeter of rectangle in the same units as length
    >>>>calculate_perimeter_rectangle(5,8)
    26
    """
    return 2*length+2*breadth
if __name__ == '__main__':
 print("Perimeter of rectangle is: ", calculate_perimeter_rectangle(5,8))



def calculate_volume_right_pyramid(length,breadth,height):
    """
    @param length of the base of the pyramid:
    @param breadth of the base of the pyramid:
    @param height of the vertical:
    @return:volume of the pyramid in cubic units of length
    >>>>calculate_volume_right_pyramid(6,8,13)
    208
    """
    return 1/3*length*breadth*height
if __name__ == '__main__':
    print("Volume of right_pyramid is:", calculate_volume_right_pyramid(6,8,13))


def calculate_perimeter_regular_pentagon(side_length):
    """
    @param side_length of the pentagon:
    @return:Perimeter of the pentagon in the same units as side length
    >>>>calculate_perimeter_regular_pentagon(100)
    500
    """
    return 5*side_length
if __name__ == '__main__':
  print("Perimeter of regular pentagon is:",  calculate_perimeter_regular_pentagon(100))


def calculate_perimeter_regular_hexagon(side_length):
    """
    @param side_length of the hexagon:
    @return:perimeter of the hexagon in the same units as side length
    >>>> calculate_perimeter_regular_hexagon(8)
    48
    """
    return 6*side_length
if __name__ == '__main__':
   print("Perimeter of Regular hexagon is:", calculate_perimeter_regular_hexagon(8))

def calculate_area_right_angled_triangle(base,height):
    """
    @param base of the triangle:
    @param heightof the triangle:
    @return:area of the triangle in square units
    >>>>calculate_area_right_angled_triangle(4,15)
    30
    """
    return 1/2*base*height
if __name__ == '__main__':
    print("Area of triangle is:", calculate_area_right_angled_triangle(4, 15))

def calculate_volume_cuboid(length, width, height):
    """
    @param length of the cuboid:
    @param width of the cuboid:
    @param height of the cuboid:
    @return:volume of the cuboid in cubic units
    >>>>calculate_volume_cuboid(12, 4, 10)
    480
    """
    return length*width*height
if __name__ == '__main__':
  print("volume of the cuboid:", calculate_volume_cuboid(12, 4, 10))


def calculate_area_trapezium(shorter_side_length,longer_side_length,height):
     """
    @param shorter_side_length of the trapezium:
    @param longer_side_length of the trapezium:
    @param height of the trapezium:
    @return:area of the trapezium in square units
     """
     return 1/2*height*(shorter_side_length+longer_side_length)
if __name__ == '__main__':
  print("Area of trapezium is", calculate_area_trapezium(2,3,6))








