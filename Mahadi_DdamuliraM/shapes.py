__author__ = 'mahadi'
import turtle
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

class Circle(Shape):
    """a class representation of circle"""
    circles_created = 0
    def __init__(self, radius: (int, float)):
        super(Circle, self).__init__(radius=radius)
        self.circles_created += 1
        self.radius = radius
        self.area = pi*self.radius**2
        self.perimeter = pi*self.radius*2

    def __str__(self):
        return super(Circle, self).__str__()+\
               "; radius: "+str(self.radius)

    def __cmp__(self, other):
        if not isinstance(other, Circle):
            raise TypeError
        else:
            return self.radius - other.radius

    def draw(self):
            turtle.circle(self.radius)
            turtle.done()

if __name__ == "__main__":
    cir=Circle(100)
    print(cir)
    cir.draw()

    try:
        cir2 = Circle("a string")
    except TypeError as err:
        print(err.args[0], cir.shapes_created, cir.circles_created)


class Pentagon(Shape):
    """a class representation of square"""
    pentagons_created = 0
    def __init__(self, side_length:(int,float)):
        super(Pentagon, self).__init__(side_length=side_length)
        self.pentagons_created += 1
        self.side_length = side_length
        self.area = 1/4*sqrt(5*(5 + 2*sqrt(5)))*self.side_length**2
        self.perimeter = self.side_length*5

    def __str__(self):
        return super(Pentagon, self).__str__()+\
               "; side length: "+str(self.side_length)

    def __cmp__(self, other):
        if not isinstance(other, Pentagon):
            raise TypeError
        else:
            return self.side_length - other.side_length

    def draw(self):
        for i in range(0,5):
            turtle.forward(self.side_length)
            turtle.left(72)
        turtle.done()

if __name__ == "__main__":
    pe = Pentagon(100)
    print(pe)
    pe.draw()

    try:
        he2 = Pentagon("a string")
    except TypeError as err:
        print(err.args[0], pe.shapes_created, pe.pentagons_created)


class Hexagon(Shape):
    """a class representation of square"""
    hexagons_created = 0
    def __init__(self, side_length:(int,float)):
        super(Hexagon, self).__init__(side_length=side_length)
        self.hexagons_created += 1
        self.side_length = side_length
        self.area = 3/2*sqrt(3)*self.side_length**2
        self.perimeter = self.side_length*6

    def __str__(self):
        return super(Hexagon, self).__str__()+\
               "; side length: "+str(self.side_length)

    def __cmp__(self, other):
        if not isinstance(other, Hexagon):
            raise TypeError
        else:
            return self.side_length - other.side_length

    def draw(self):
        for i in range(0,6):
            turtle.forward(self.side_length)
            turtle.left(60)
        turtle.done()
if __name__ == "__main__":
    he = Hexagon(100)
    print(he)
    he.draw()

    try:
        pe2 = Hexagon("a string")
    except TypeError as err:
        print(err.args[0], he.shapes_created, he.hexagons_created)

class Trapezium(Shape):
    """a class representation of trapezium"""
    trapeziums_created = 0
    def __init__(self, b1: (int,float), b2: (int,float), height: (int,float)):
        super(Trapezium, self).__init__(b1=b1,b2=b2, height=height)
        self.trapeziums_created += 1
        self.b1 = b1
        self.b2 = b2
        self.height = height
        self.area = 0.5*((self.b1 +self.b2)*self.height)
        self.perimeter = (self.b1+self.b2+self.height +sqrt(self.height**2 +abs(self.b1-self.b2)**2))

    def __str__(self):
        return super(Trapezium, self).__str__()+ "; b1: "+str(self.b1)+",b2: "+str(self.b2)+",height: "+str(self.height)


    def __cmp__(self, other):
        if not isinstance(other, Trapezium):
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
if __name__ == "__main__":
    tra  = Trapezium(70,42, 62)
    print(tra)
    tra.draw()

    try:
        pe2 = Hexagon("a string")
    except TypeError as err:
        print(err.args[0], tra.shapes_created, tra.trapeziums_created)

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

if __name__ == "__main__":
    rec = Rectangle(70,42)
    print(rec)
    rec.draw()

    try:
        rec2 = Rectangle("a string")
    except TypeError as err:
        print(err.args[0], rec.shapes_created, rec.rectangles_created)





