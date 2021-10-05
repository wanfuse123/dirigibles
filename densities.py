from gaslaws import gas_mass, pascal
from temperature import Kelvin



# mass in kg of 1 mole of substance
CO2Mass = 0.04401  # kg/mole
O2Mass = 0.0320
N2Mass = 0.02802
SilaneMass = 0.03212 # SiH₄
AmmoniaMass = 0.017
AirMass = 0.0290  # Molecular weight of air. This must be artificial
HeliumMass = 0.00402
H2Mass = 0.00202
MethaneMass = 0.016043
H2OMass = 0.018016
AirDensity = 1.205 # kg/m3
CO2Density = 1.842 # kg/m3
BiglowB330Space = 330.0 # m3, diameter 6.7, Length 13.7. 0.46m hull thickness
BiglowB330Mass = 15000 # kg
SteelDensity = 7800 # kg/m3
NylonDensity = 1130
PolypropyleneDensity = 900
AluminiumDensity = 2700
IceDensity = 970
KevlarDensity = 1440
CarbonfibreCompositeDensity = 1600 # Not sure if this is right. Check it
MylarDensity = 1390                # Polyester film. Mylar is the DuPont trade name
WaterDensity = 1000



# 1 micron is 1/1e6 meter. Micron is often used to describe thickness of polymer films
# used as envelope for airships
def gas_mass_CO2(P, V, celsius):
    return gas_mass(P, V, celsius, CO2Mass)

def gas_mass_N2(P, V, celsius):
    return gas_mass(P, V, celsius, N2Mass)

def gas_mass(P, V, celsius):
    return gas_mass(P, V, celsius, O2Mass)

def earth_gas_mass(V, molecular_mass):
    return gas_mass(pascal(1), V, Kelvin(20), molecular_mass)

def gas_mass_CO2(P, V, celsius):
    return gas_mass(P, V, celsius, AirMass)

def gas_mass_CO2(P, V, celsius):
    return gas_mass(P, V, celsius, H2OMass)

def gas_mass_CO2(P, V, celsius):
    return gas_mass(P, V, celsius, AmmoniaMass)

def gas_mass_CO2(P, V, celsius):
    return gas_mass(P, V, celsius, SilaneMass)

def gas_mass_CO2(P, V, celsius):
    return gas_mass(P, V, celsius, MethaneMass)

def gas_mass_CO2(P, V, celsius):
    return gas_mass(P, V, celsius, HeliumMass)
