# import all modules
from Airship import *


"""
Example Zeppelin calculations to test that all functions are working
"""
# Zeppelin volume calculations
zeppelin_volume = ellipsoid_volume(245.0/2, 41.2/2, 41.2/2)
print(zeppelin_volume)

# Zeppelin lift calculations
air_mass = gas_mass(pascal(1), 200_000, Kelvin(5), AirMass)
hydrogen_mass = gas_mass(pascal(1), 200_000, Kelvin(5), H2Mass)
lift_capacity = air_mass - hydrogen_mass
print(air_mass, hydrogen_mass, lift_capacity)

# Weight of envelope
# Goodyear Zeppelin has 1.5 mm thick polyester envelope. Polyester (mylar) has a density of 1390 kg/m³
envelope_area = prolate_spheroid_area(41.2/2, 245.0/2)
envelope_thickness = 0.0015
envelope_density = 1390
envelope_weight = envelope_area * envelope_thickness * envelope_density
print(envelope_area, envelope_weight)

# adjust lift capacity after envelope weight
lift_capacity = lift_capacity - envelope_weight
print(lift_capacity)

# all other weight parameters
airship_frame = 49_000
airship_crew = 5_400
airship_provisions = 3_000
airship_fuel = 58_880
airship_oil = 4_000
airship_ballast = 7_950
airship_misc = 9_120



"""
Example function with nested FOR loops
"""
def nested_for():
    result_array = []
    
    # loop through different gases
    for m in [CO2Mass, H2Mass, O2Mass, N2Mass, SilaneMass, AmmoniaMass, AirMass, H2OMass]:
        
        # loop through different range of temperature
        for t in range(0, 101, 10):
            result_array.append([
                CO2Mass, 
                t,
                gas_mass(pascal(1.01325), 1, Kelvin(t), m)
            ])

    return result_array


print(nested_for())



"""
Example plot
"""
import plotly.graph_objects as go
import numpy as np

# create a figure / canvas to plot on
fig = go.Figure(layout=go.Layout(
    title='Title',
    xaxis={
        'title': 'Temperature, °C'
    },
    yaxis={
        'title': 'Density, kg.m^-3'
    }
))

# loop through different gases
gases = {
    'CO2': CO2Mass, 
    'H2': H2Mass,
    'O2': O2Mass, 
    'N2': N2Mass,
    'Si': SilaneMass,
    'NH4': AmmoniaMass,
    'Air': AirMass,
    'H2O': H2OMass
}
temp_range = [x for x in range(0, 2500, 10)]
for g in gases:

    mass_range = []    
    # loop through different range of temperature
    for t in temp_range:
        mass_range.append(gas_mass(pascal(1.01325), 1, Kelvin(t), gases[g]))

    # plot trace / series
    fig.add_trace(
        go.Scatter(
            x=temp_range, 
            y=mass_range,  
            name=g,  # legend
            line_shape='spline' # line type
        )
    )

# show figure
fig.show()
