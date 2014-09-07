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
class Solid(object):
    solids_created = 0
    def __init__(self, **kwargs):
        dim_checker(**kwargs)
        self.solids_created += 1

    def __str__(self):
        return self.__class__.__name__ +\
               "; surface_area : "+str(self.surface_area)+\
               "; volume: "+str(self.volume)


class Cylinder(Solid):
    """a class representation of cylinder"""
    cylinders_created = 0
    def __init__(self, radius: (int,float), height: (int,float)):
        super(Cylinder, self).__init__(radius=radius, height=height)
        self.cylinders_created += 1
        self.radius = radius
        self.height = height
        self.surface_area = 2*math.pi*(self.radius *self.radius *self.height)
        self.volume = pi*self.radius**2*self.height

    def __str__(self):
        return super(Cylinder, self).__str__()+ "; radius: "+str(self.radius)+", height: "+str(self.height)


    def __cmp__(self, other):
        if not isinstance(other, Cylinder):
            raise TypeError
        else:
            return self.radius - other.radius


if __name__ == "__main__":
    cyl = Cylinder(28, 78)
    print(cyl)

    try:
        cyl2 = Cylinder("a string")
    except TypeError as err:
        print(err.args[0], cyl.solids_created, cyl.cylinders_created)


class Cone(Solid):
    """a class representation of cuboid"""
    cones_created = 0
    def __init__(self, radius: (int,float), height: (int,float),length:(int,float)):
        super(Cone, self).__init__(radius=radius, height=height, length=length)
        self.cones_created += 1
        self.radius = radius
        self.height = height
        self.length = length
        self.surface_area = 2*math.pi*(self.radius *self.radius *self.length)
        self.volume = 1/3*pi*self.radius**2*self.height

    def __str__(self):
        return super(Cone, self).__str__()+ "; radius: "+str(self.radius)+", height: "+str(self.height)+", length: "+str(self.length)


    def __cmp__(self, other):
        if not isinstance(other, Cone):
            raise TypeError
        else:
            return self.radius - other.radius


if __name__ == "__main__":
    con = Cone(28, 78, 45)
    print(con)

    try:
        con2 = Cone("a string")
    except TypeError as err:
        print(err.args[0], con.solids_created, con.cones_created)


class Cuboid(Solid):
    """a class representation of cuboid"""
    cuboids_created = 0
    def __init__(self, length: (int,float), height: (int,float), width: (int,float)):
        super(Cuboid, self).__init__(length=length, height=height, width=width)
        self.cuboids_created += 1
        self.length = length
        self.height = height
        self.width = width
        self.surface_area = 2*(length*width +length*height +width*height)
        self.volume = length*width*height

    def __str__(self):
        return super(Cuboid, self).__str__()+ "; length: "+str(self.length)+", height: "+str(self.height)+", width: "+str(self.width)


    def __cmp__(self, other):
        if not isinstance(other, Cone):
            raise TypeError
        else:
            return self.length - other.length


if __name__ == "__main__":
    cub = Cuboid(80, 78, 40)
    print(cub)

    try:
        cub2 = Cuboid("a string")
    except TypeError as err:
        print(err.args[0], cub.solids_created, cub.cuboids_created)


class Sphere(Solid):
    """a class representation of Sphere"""
    spheres_created = 0
    def __init__(self, radius: (int, float)):
        super(Sphere, self).__init__(radius=radius)
        self.spheres_created += 1
        self.radius = radius
        self.surface_area = 4*pi*self.radius**2
        self.volume = pi*self.radius**3

    def __str__(self):
        return super(Sphere, self).__str__()+\
               "; radius: "+str(self.radius)

    def __cmp__(self, other):
        if not isinstance(other, Sphere):
            raise TypeError
        else:
            return self.radius - other.radius


if __name__ == "__main__":
    sp = Sphere(100)
    print(sp)

    try:
        sp2 = Sphere("a string")
    except TypeError as err:
        print(err.args[0], sp.solids_created, sp.spheres_created)

class Pyramid(Solid):
    """a class representation of pyramid"""
    pyramids_created = 0
    def __init__(self, length: (int,float), height: (int,float), width: (int,float), slength):
        super(Pyramid, self).__init__(length=length, height=height, width=width, slength=slength)
        self.pyramids_created += 1
        self.length = length
        self.height = height
        self.width = width
        self.slength = slength
        self.surface_area = 2*(1/2*length*slength +1/2*width*slength)
        self.volume = 1/3*length*width*height

    def __str__(self):
        return super(Pyramid, self).__str__()+ "; length: "+str(self.length)+", height: "+str(self.height)+", width: "+str(self.width)+", slength: "+str(self.slength)


    def __cmp__(self, other):
        if not isinstance(other, Pyramid):
            raise TypeError
        else:
            return self.length - other.length


if __name__ == "__main__":
    pyr = Pyramid(80, 78, 40, 130)
    print(pyr)

    try:
        cub2 = Pyramid("a string")
    except TypeError as err:
        print(err.args[0], pyr.solids_created, pyr.pyramids_created)
