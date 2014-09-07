__author__ = 'mahadi'

import turtle
import math
from numpy import*

def dim_checker(**kwargs):
    errmsg = "All given arguments must be positive numbers; provided :"\
             + \
             str({k: v for k, v in kwargs.items() if v is not None})
    for name, arg in kwargs.items():
        if arg is None:
            pass # ignore nones, only checking provided arguments here
        elif not isinstance(arg, (int, float)):
            raise TypeError(errmsg)
        elif not arg >= 0:
            raise ValueError(errmsg)


class Shape(object):
    shapes_created = 0
    def __init__(self, **kwargs):
        dim_checker(**kwargs)
        self.shapes_created += 1

    def __str__(self):
        return self.__class__.__name__ +\
               "; area : "+str(self.area)+\
               "; perimeter: "+str(self.perimeter)

class Rectangle(Shape):
    """a class representation of rectangle"""
    rectangles_created = 0
    def __init__(self, length: (int,float), width: (int,float)):
        super(Rectangle, self).__init__(length=length, width=width)
        self.rectangles_created += 1
        self.length = length
        self.width = width
        self.area = self.length * self.width
        self.perimeter = (self.length+self.width)*2

    def __str__(self):
        return super(Rectangle, self).__str__()+ "; length: "+str(self.length)+", width: "+str(self.width)


    def __cmp__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError
        else:
            return self.length - other.length

    def draw(self):
        for i in range(0,2):
            turtle.forward(self.length)
            turtle.left(90)
            turtle.forward(self.width)
            turtle.left(90)
        turtle.done()

Rectan = Rectangle(160, 80)
print(Rectan)
Rectan.draw()




class Triangle (Shape):
    """a class representation of triangle"""
    triangle_created = 0
    def __init__(self, base: (int,float), height: (int,float)):
        super(Triangle, self).__init__(base=base, height=height)
        self.triangle_created += 1
        self.base = base
        self.height = height
        self.area = 0.5*(self.base * self.height)
        self.perimeter = (self.base+self.height)*2

    def __str__(self):
        return super(Triangle, self).__str__()+ "; base: "+str(self.base)+", height: "+str(self.height)


    def __cmp__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError
        else:
            return self.base - other.base

    def draw(self):
        for i in range(0,3):
            turtle.forward(self.base)
            turtle.left(120)
        turtle.done()

Triangle = Triangle(50, 80)
Triangle.draw()




class Square(Shape):
    """a class representation of square"""
    squares_created = 0
    def __init__(self, side: (int,float)):
        super(Square, self).__init__(side=side)
        self.squares_created += 1
        self.side = side
        self.area = self.side**2
        self.perimeter = self.side*4


    def __str__(self):
        return super(Square, self).__str__()+\
               "; side length: "+str(self.side)


    def __cmp__(self, other):
        if not isinstance(other, Square):
            raise TypeError
        else:
            return self.side - other.side

    def draw(self):
        for i in range(0,4):
            turtle.forward(self.side)
            turtle.left(90)
        turtle.done()
Square = Square(70)
#print(Square)
Square.draw()



class Cylinder(Shape):
    """a class representation of cylinder"""
    cylinders_created = 0
    def __init__(self, radius: (int,float), height: (int,float)):
        super(Cylinder, self).__init__(radius=radius, height=height)
        self.cylinders_created += 1
        self.radius = radius
        self.height = height
        self.area = 2*math.pi*(self.radius *self.radius *self.height)
        self.perimeter = (self.radius+self.height)*2

    def __str__(self):
        return super(Cylinder, self).__str__()+ "; radius: "+str(self.radius)+", height: "+str(self.height)


    def __cmp__(self, other):
        if not isinstance(other, Cylinder):
            raise TypeError
        else:
            return self.radius - other.radius



Cylinder = Cylinder(20, 9)








class Circle(Shape):
    """a class representation of circle"""
    circle_created = 0
    def __init__(self, radius: (int,float)):
        super(Circle, self).__init__(radius=radius)
        self.circle_created += 1
        self.radius = radius
        self.area = math.pi*(self.radius)**2
        self.perimeter = (self.radius)*2

    def __str__(self):
        return super(Circle, self).__str__()+ "; radius: "+str(self.radius)


    def __cmp__(self, other):
        if not isinstance(other, Circle):
            raise TypeError
        else:
            return self.radius - other.radius

    def draw(self):
        turtle.circle(self.radius)
        turtle.done()

Circle = Circle(100)
Circle.draw()



class Trapezim(Shape):
    """a class representation of trapezim"""
    Trapezim_created = 0
    def __init__(self, b1: (int,float), b2: (int,float), height: (int,float)):
        super(Trapezim, self).__init__(b1=b1,b2=b2, height=height)
        self.Trapezim_created += 1
        self.b1 = b1
        self.b2 = b2
        self.height = height
        self.area = 0.5*((self.b1 +self.b2)*self.height)
        self.perimeter = (self.b1+self.b2+self.height)*2

    def __str__(self):
        return super(Trapezim, self).__str__()+ "; b1: "+str(self.b1)+",b2: "+str(self.b2)+",height: "+str(self.height)


    def __cmp__(self, other):
        if not isinstance(other, Trapezim):
            raise TypeError
        else:
            return self.radius - other.radius

    def draw(self):

        turtle.forward(self.b1)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward(self.b2)
        turtle.goto(0,0)
        turtle.done()

Trapezim = Trapezim(200,102 ,90)
Trapezim.draw()


class Cone(Shape):
    """a class representation of cone"""
    Cone_created = 0
    def __init__(self, radius: (int,float), height: (int,float)):
        super(Cone, self).__init__(radius=radius, height=height)
        self.Cone_created += 1
        self.radius = radius
        self.height = height
        self.surface_area = 4/3*(self.radius *self.radius *self.height)
        self.perimeter = (self.radius+self.height)*2

    def __str__(self):
        return super(Cone, self).__str__()+ "; radius: "+str(self.radius)+", height: "+str(self.height)


    def __cmp__(self, other):
        if not isinstance(other, Cone):
            raise TypeError
        else:
            return self.radius - other.radius



Cone = Cone(7, 16)



class Pentagon(Shape):
    """a class representation of a pentagon"""
    Pentagon_created = 0
    def __init__(self, side: (int,float)):
        super(Pentagon, self).__init__(side=side)
        self.Pentagon_created += 1
        self.side = side
        self.area = 1/4*sqrt(5*(5+2*sqrt(5)))*side**2
        self.perimeter = 5*side

    def __str__(self):
        return super(Pentagon, self.side)


    def __cmp__(self, other):
        if not isinstance(other, Pentagon):
            raise TypeError
        else:
            return self.side - other.side

    def draw(self):
        for i in range(0,5):
            turtle.forward(self.side)
            turtle.left(72)
        turtle.done()

Pentagon = Pentagon(200)
Pentagon.draw()