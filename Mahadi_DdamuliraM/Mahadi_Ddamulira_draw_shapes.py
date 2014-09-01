__author__ = 'mahadi'
import turtle

def draw_circle(radius):
    i=0
    while i<100:
        turtle.forward(radius)
        turtle.left(4)
        i=i+1
    turtle.done()

if __name__== "__main__":
    draw_circle(10)


def draw_regular_hexagon(side_length):
    i = 0
    while i < 6:
        turtle.forward(side_length)
        turtle.left(60)
        i = i+1
    turtle.done()
if __name__ == "__main__":
    draw_regular_hexagon(200)



def draw_regular_pentagon(side_length):
    i = 0
    while i < 5:
        turtle.forward(side_length)
        turtle.left(72)
        i = i+1
    turtle.done()

if __name__ == "__main__":
    draw_regular_pentagon(200)


def draw_rectangle(length,width):
    i = 0
    while i < 2:
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        i = i+1
    turtle.done()


if __name__ == "__main__":
    draw_rectangle(400,200)

def draw_equilateral_triangle(side_length):
    i=0
    while i < 3:
        turtle.forward(side_length)
        turtle.left(120)
        i=i+1
    turtle.done()

if __name__ == "__main__":
    draw_equilateral_triangle(200)


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from itertools import product, combinations
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

#draw cube
r = [-1, 1]
for s, e in combinations(np.array(list(product(r,r,r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax.plot3D(*zip(s,e), color="b")

#draw sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x=np.cos(u)*np.sin(v)
y=np.sin(u)*np.sin(v)
z=np.cos(v)
ax.plot_wireframe(x, y, z, color="r")

#draw a point
ax.scatter([0],[0],[0],color="g",s=100)

#draw a vector
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

a = Arrow3D([0,1],[0,1],[0,1], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
ax.add_artist(a)
plt.show()























