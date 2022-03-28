import math

# "Volume of sphere with radius `r`"
def sphere_volume(r):
    return (4/3)*math.pi*r**3

# "Volume of an ellipsoid with radii `a`, `b` and `c`. This is like a rotated ellipse. Useful approximation to zepplins and flying saucers."
def ellipsoid_volume(a, b, c):
    return (4/3)*math.pi*a*b*c

# "Volume of cylinder with radius `r` and height `h`"
def cylinder_volume(r, h):
    return circle_area(r)*h

# "Surface area of a sphere"
def sphere_area(r):
    return 4*math.pi*r**2

# "Surface area of a cylinder of height `h` and radius `r`"
def cylinder_area(r, h):
    return 2*circle_area(r) + 2*math.pi*r*h

# "Area of a triangle"
def triangle_area(b, h):
    return b*h/2

# "Area of a circle with radius `r`"
def circle_area(r):
    return math.pi*r**2

# "Area of rectangle with height `h` and width `w`"
def rectangle_area(h, w):
    return h*w

"""
    oblate_spheroid_area(a, b)
Area of an ellipsoid which is disc shaped. That is, it is made from rotating an ellipse
around its minor axis (shortest axis).
`a` is the semi-minor axis and `b` the semi-major axis.
"""
def oblate_spheroid_area(a, b):
    alpha = math.acos(a/b)
    return 2*math.pi*(a**2 + (b**2/math.sin(alpha)) * math.log((1 + math.sin(alpha)/math.cos(alpha))) )

"""
    prolate_spheroid_area(a, b)
Area of an ellipsoid which is cigar shaped. That is, it is made from rotating an ellipse
around its major axis. Major axis is the longest axis.
`a` is the semi-minor axis and `b` the semi-major axis.
"""
def prolate_spheroid_area(a, b):
    alpha = math.acos(a/b)
    return 2*math.pi*(a**2 + a*b*alpha/math.sin(alpha))
