__author__ = 'mahadi'
import turtle
from numpy import*

class Square(object):
    """a class representation of square"""
    squares_created = 0
    def __init__(self, side_length:(int,float)):
        self.squares_created += 1
        self.side_length = side_length
        self.area = self.side_length**2
        self.perimeter = self.side_length*4

    def __str__(self):
        return "Square, side length: "+str(self.side_length)

    def __cmp__(self, other):
        if not isinstance(other, Square):
            raise TypeError
        else:
            return self.side_length - other.side_length

    def draw(self):
        for i in range(0,4):
            turtle.forward(self.side_length)
            turtle.left(90)
        turtle.done()

sq = Square(50)

import math
print(math.sin)
print(sq,sq.area,sq.perimeter)
sq.draw()

class Circle(object):
    """a class representation of a circle"""
    circles_created=0
    def __init__(self,radius:(int,float)):
        self.circles_created += 1
        self.radius = radius
        self.area = pi*radius**2
        self.circumference = 2*pi*radius

    def __str__(self):
        return "Circle, radius:" + str(self.radius)
    def __cmp__(self,other):
        if not isinstance(other,Circle):
            raise TypeError
        else:
            return self.radius - other.radius
    def draw(self):
        turtle.circle(self.radius)
        turtle.done()
cir = Circle(100)
print(cir,cir.area,cir.circumference)
cir.draw()

class Equilateral_triangle(object):
    """ a class representation of an equilateral triangle"""
    equilateral_triangles_created = 0
    def __init__(self,side_length:(int,float)):
        self.equilateral_triangles_created += 1
        self.side_length = side_length
        self.area = 1/2*side_length**2*sqrt(3)/2
        self.perimeter = 3*side_length
    def __str__(self):
        return "Equilateral_triangle, side_length:" +str(self.side_length)
    def __cmp__(self, other):
        if not isinstance(other, Equilateral_triangle):
            raise TypeError
        else:
            return self.side_length - other.side_length
    def draw(self):
        for i in range (0,3):
            turtle.forward(self.side_length)
            turtle.left(120)
            turtle.done

Equ = Equilateral_triangle(140)
print(Equ,Equ.area, Equ.perimeter)
Equ.draw()

class Regular_pentagon(object):
    """ a class representation of a regular pentagon"""
    regular_pentagons_created = 0
    def __init__(self,side_length:(int, float)):
        self.side_length = side_length
        self.area= 1/4*sqrt(5*(5+2*sqrt(5)))*side_length**2
        self.perimeter = 5*side_length
    def __str__(self):
        return "Regular_pentagon, side_length:" + str(self.side_length)
    def __cmp__(self,other):
        if not isinstance(other,Regular_pentagon):
            raise TypeError
        else:
                 return self.side_length - other.side_length
    def draw(self):
        for i in range (0,5):
            turtle.forward(self.side_length)
            turtle.left(72)
            turtle.done

Rep= Regular_pentagon(160)
print(Rep, Rep.area, Rep.perimeter)
Rep.draw()

class Regular_hexagon(object):
    """ a class representation of a regular pentagon"""
    regular_pentagons_created = 0
    def __init__(self,side_length:(int, float)):
        self.side_length = side_length
        self.area= 3/2*sqrt(3)*self.side_length**2
        self.perimeter = 5*side_length
    def __str__(self):
        return "Regular_hexagon, side_length:" + str(self.side_length)
    def __cmp__(self,other):
        if not isinstance(other,Regular_hexagon):
            raise TypeError
        else:
                 return self.side_length - other.side_length
    def draw(self):
        for i in range (0,6):
            turtle.forward(self.side_length)
            turtle.left(60)
            turtle.done

Reh= Regular_hexagon(130)
print(Reh, Reh.area, Reh.perimeter)
Rep.draw()

class Rectangle(object):
    """a class representation of a rectangle"""
    rectangles_created = 0
    def __init__(self, length:(int, float),breadth:(int, float)):
        self.rectangles_created += 1
        self.length = length
        self.breadth = breadth
        self.area = length*breadth
        self.perimeter = 2*(length + breadth)
    def __str__(self):
        return super(Rectangle, self).__str__() + "; length: " + str(self.length) + ", breadth: "+str(self.breadth)
    def __cmp_(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError
        else:
            return self.length - other.length
    def draw(self):
        for i in range(0,4):
            turtle.forward(self.length)
            turtle.left(90)
            turtle.forward(self.breadth)
            turtle.left(90)
        turtle.done()

rec = Rectangle(120,80)
print(rec,rec.area,rec.perimeter)
rec.draw()


class Trapezium(object):
    """a class representation of a trapezium"""
    rectangles_created = 0
    def __init__(self, length1:(int, float),length2:(int, float), height:(int,float)):
        self.rectangles_created += 1
        self.length1 = length1
        self.length2 = length2
        self.height = height
        self.area = 1/2*height*(length1+length2)
        self.perimeter = length1 + length2 + height + sqrt(height**2 + abs(length2-length1)**2)
    def __str__(self):
        return super(Trapezium, self).__str__() + "; length1: " + str(self.length1) + ",length2: "+str(self.length2) +",height: "+str(self.height)
    def __cmp_(self, other):
        if not isinstance(other, Trapezium):
            raise TypeError
        else:
            return self.length1 - other.length1
    def draw(self):
        turtle.forward(self.length1)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward(self.length2)
        turtle.goto(0,0)
        turtle.done()

tra = Trapezium(20, 70, 80)
print(tra,tra.area,tra.perimeter)
tra.draw()

