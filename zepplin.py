from densities import HeliumMass, H2Mass, AirMass
from volume import ellipsoid_volume, oblate_spheroid_area, prolate_spheroid_area, sphere_area, sphere_volume
from gaslaws import gas_mass, pascal



def lift(V, lift_gas_mass, displaced_gas_mas):
    T = 20
    P = pascal(1)
    return gas_mass(P, V, T, displaced_gas_mas) - gas_mass(P, V, T, lift_gas_mass)

"""
Calcuate how many kg an airship with oblate spheroid can lift on
earth like pressure and temperature,
if it has semi-minor axis `a`, semi-major axis `b` with an envelope of given
`thickness` and `density`. Example:
    oblate_spheroid_lift_earth(10/2, 150/2, 0.0015, MylarDensity)
Givens lift of airship with diameter 150 m, height 10 m encased in a mylar envelope
1.5 mm thick.
"""
def oblate_spheroid_lift(a, c, thickness, density, liftgas = HeliumMass, displaced_gas_mas = AirMass):
    V = ellipsoid_volume(a, a, c)
    A = oblate_spheroid_area(a, c)
    l = lift(V, liftgas, displaced_gas_mas)
    return l -  A*thickness*density

def prolate_spheroid_lift(a, c, thickness, density, liftgas = H2Mass, displaced_gas_mas = AirMass):
    V = ellipsoid_volume(a, a, c)
    A = prolate_spheroid_area(a, c)
    l = lift(V, liftgas, displaced_gas_mas)
    return l - A*thickness*density

def sphere_lift(radius, thickness, density, liftgas = HeliumMass, displaced_gas_mas = AirMass):
    V = sphere_volume(radius)
    A = sphere_area(radius)
    l = lift(V, liftgas, displaced_gas_mas)
    return l - A*thickness*density
