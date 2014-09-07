__author__ = 'mahadi'
from solids import*
from shapes import*
from objects import*
sdict = {'1': 'Circle', '2': 'Pentagon', '3': 'Hexagon', '4': 'Trapezium', '5': 'Rectangle', '6': 'Sphere', '7': 'Cylinder',
         '8': 'Cuboid', '9': 'Cone', '10': 'Pyramid','11': 'Equilateral_triangle'}
shapes_solids = {'Circle', 'Hexagon', 'Circle', 'Pentagon','Trapezium',  'Equilateral_triangle', 'Cylinder',
                 'Cuboid', 'Sphere', 'Cone', 'Pyramid'}
print('World of geometric figures')
print('or you can quit.')


def start():
    figure = input("What geometric figure do you want? 'quit' to stop:")
    if figure != "quit" and figure in sdict.get('1'):
        try:
            radius = float(input("What is the radius? 'quit' to stop:"))
            cir = Circle(radius)
            print(cir)
            cir.draw()
        except ValueError as err:
            print(err.args[0])
        finally:
            return start()
    elif figure != "quit" and figure in sdict.get('5'):
        try:
            side_length = float(input("What is the side_length? 'quit' to stop:"))
            pe = Pentagon(side_length)
            print(pe)
            pe.draw()
        except ValueError as err:
            print(err.args[0])
        finally:
            return start()

    elif figure != "quit" and figure in sdict.get('5'):
        try:
            side_length = float(input("What is the side_length? 'quit' to stop:"))
            Equ = Equilateral_triangle(side_length)
            print(Equ)
            Equ.draw()
        except ValueError as err:
            print(err.args[0])
        finally:
            return start()
    elif figure != "quit" and figure in sdict.get('2'):
        try:
            side_length = float(input("What is the side_length? 'quit' to stop:"))
            he= Hexagon(side_length)
            print(he)
            he.draw()
        except ValueError as err:
            print(err.args[0])
        finally:
            return start()

    elif figure != "quit" and figure in sdict.get('4'):
        try:
            length = float(input("What is the length? 'quit' to stop:"))
            width = float(input("What is the width? 'quit' to stop:"))
            rec = Rectangle(length, width)
            print(rec)
            rec.draw()
        except ValueError as err:
            print(err.args[0])
        finally:
            return start()

    elif figure != "quit" and figure in sdict.get('6'):
        try:
            radius = float(input("What is the radius? 'quit' to stop:"))
            sp = Sphere(radius)
            print(sp)
        except ValueError as err:
            print(err.args[0])
        finally:
            return start()

    elif figure != "quit" and figure in sdict.get('7'):
        try:
            radius = float(input("What is the radius? 'quit' to stop:"))
            height = float(input("what is the height? 'quit' to stop:"))
            cyl = Cylinder(radius, height)
            print(cyl)
        except ValueError as err:
            print(err.args[0])
        finally:
            return start()

    elif figure != "quit" and figure in sdict.get('8'):
        try:
            length = float(input("What is the length? 'quit' to stop:"))
            width = float(input("what is the width? 'quit' to stop:"))
            height = float(input("what is the height? 'quit' to stop:"))
            cub = Cuboid(length, width, height)
            print(cub)
        except ValueError as err:
            print(err.args[0])
        finally:
            return start()

    elif figure != "quit" and figure in sdict.get('9'):
        try:
            radius = float(input("What is the radius? 'quit' to stop:"))
            height = float(input("what is the height? 'quit' to stop:"))
            length = float(input("what is the height? 'quit' to stop:"))
            con = Cone(radius, height, length)
            print(con)
        except ValueError as err:
            print(err.args[0])
        finally:
            return start()

    elif figure != "quit" and figure in sdict.get('10'):
        try:
            length1 = float(input("What is the length1? 'quit' to stop:"))
            length2 = float(input("what is the length2? 'quit' to stop:"))
            height = float(input("what is the height? 'quit' to stop:"))
            tra = Trapezium(length1, length2, height)
            print(tra)
            tra.draw()
        except ValueError as err:
            print(err.args[0])
        finally:
            return start()

    elif figure != "quit" and figure in sdict.get('10'):
        try:
            length = float(input("What is the length? 'quit' to stop:"))
            width = float(input("what is the width? 'quit' to stop:"))
            height = float(input("what is the height? 'quit' to stop:"))
            slength = float(input("What is the slength? 'quit' to stop:"))
            pyr = Pyramid(length, width, height,slength)
            print(pyr)
        except ValueError as err:
            print(err.args[0])
        finally:
            return start()
    else:
        print('The available figures are \n Circle,Pentagon,Hexagon,Equilateral_triangle,Rectangle,Sphere,Cylinder,Cuboid,Cone,Pyramid')
        return start()
start()