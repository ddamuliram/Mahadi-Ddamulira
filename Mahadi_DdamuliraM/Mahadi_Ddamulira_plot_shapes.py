__author__ = 'mahadi'
from pylab import *
from geom_formulae import *

v_calculate_area_circle = np.vectorize(calculate_area_circle)
v_calculate_circumference_circle= np.vectorize(calculate_circumference_circle)

S = np.linspace(0,10) # our radii

A = v_calculate_area_circle(S)  # the areas
C = v_calculate_circumference_circle(S)  # the circumferences

plot(S, A, '-r', label="Area")
plot(S, C, ':b', label="Circumference")

xlabel('Radius')
ylabel('geo values')
title('Circle Geo Properties')
legend(loc='upper left')

show()




v_calculate_surface_area_sphere = np.vectorize(calculate_surface_area_sphere)
v_calculate_volume_sphere = np.vectorize(calculate_volume_sphere)

S = np.linspace(0,10) # our radii

SA = v_calculate_surface_area_sphere(S)  # the  surface areas
V = v_calculate_volume_sphere(S)  # the Volumes

plot(S, SA, '-r', label=" Surface Area")
plot(S, V, ':b', label="Volume")

xlabel('Radius')
ylabel('geo values')
title('Sphere Geo Properties')
legend(loc='upper left')

show()



v_calculate_perimeter_regular_pentagon = np.vectorize(calculate_perimeter_regular_pentagon)
S = np.linspace(0,10) # our side lengths
P = v_calculate_perimeter_regular_pentagon(S)  # the  surface perimeters

plot(S, P, '-r', label=" Perimeter")

xlabel('Side length')
ylabel('Perimeter')
title('Regular Pentagon Geo Properties')
legend(loc='upper left')

show()




v_calculate_perimeter_regular_hexagon = np.vectorize(calculate_perimeter_regular_hexagon)
S = np.linspace(0,10) # our side lengths
P = v_calculate_perimeter_regular_hexagon(S)  # the  surface perimeters

plot(S, P, '-r', label=" Perimeter")

xlabel('Side length')
ylabel('Perimeter')
title('Regular Hexagon Geo Properties')
legend(loc='upper left')

show()

v_calculate_surface_area_cylinder = np.vectorize(calculate_surface_area_cylinder)
v_calculate_volume_cylinder= np.vectorize(calculate_volume_cylinder)
S = np.linspace(0,10) # our radii

SA = v_calculate_surface_area_cylinder(S,20)  # the areas
C = v_calculate_volume_cylinder(S,20)  # the circumferences

plot(S, SA, '-r', label="Surface Area")
plot(S, V, ':b', label="Volume")

xlabel('Radius')
ylabel('geo values')
title('Cylinder Geo Properties')
legend(loc='upper left')

show()

v_calculate_surface_area_right_circular_cone = np.vectorize(calculate_surface_area_right_circular_cone)
v_calculate_volume_cone= np.vectorize(calculate_volume_cone)
S = np.linspace(0,10) # our radii

SA = v_calculate_surface_area_right_circular_cone(S,20)  # the  surface areas
V= v_calculate_volume_cone(S,20)  # the volumes

plot(S, SA, '-r', label="Surface Area")
plot(S, V, ':b', label="Volume")

xlabel('Radius')
ylabel('geo values')
title('Cone Geo Properties')
legend(loc='upper left')

show()



v_calculate_area_rectangle = np.vectorize(calculate_area_rectangle)
v_calculate_perimeter_rectangle= np.vectorize(calculate_perimeter_rectangle)
S = np.linspace(0,10) # our lengths

A = v_calculate_area_rectangle(S,5)  # the areas
P= v_calculate_perimeter_rectangle(S,20)  # the Perimeters

plot(S, A, '-r', label="Area")
plot(S, V, ':b', label="Perimeter")

xlabel('Length')
ylabel('geo values')
title('Rectangle Geo Properties')
legend(loc='upper left')

show()


v_calculate_area_right_angled_triangle = np.vectorize(calculate_area_right_angled_triangle)
S = np.linspace(0,10) # our bases

A = v_calculate_area_right_angled_triangle(S,5)  # the areas


plot(S, A, '-r', label="Area")


xlabel('Base')
ylabel('geo values')
title('Right_angled Geo Properties')
legend(loc='upper left')

show()
