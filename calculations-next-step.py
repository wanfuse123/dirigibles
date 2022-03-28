# import all modules
from Airship import *
import inquirer

"""
Example Zeppelin calculations to test that all functions are working
"""
# Zeppelin volume calculations
zeppelin_volume = ellipsoid_volume(3000.0/2, 300/2, 300/2)
print("Hindenburg Volume for compairison to our 3km round balloon: ", zeppelin_volume)

# Zeppelin lift calculations
print("Air Mass = volume of the air displaced * density of air" )
print("Air Mass equals 4/3PiR3 = 4/3 * 3.14159 * 3000  113097335529.23 m3")

def convert(list):
    return tuple(list)

air_mass = gas_mass(pascal(1), zeppelin_volume, Kelvin(5), AirMass)
questions = [
  inquirer.List('Gas', 
              message="Which Gas Mass do you want?:/n ",
              choices=['MassCO2', 'MassO2', 'MassN2', 'MassSilane', 'MassAmmonia', 'MassAir', 'MassHelium', 'MassH2', 'MassMethane', 'MassH2O' ],
             ),
]

selectedgas = convert(Gas)

hydrogen_mass = gas_mass(pascal(1), 0, Kelvin(5), globals()[selectedgas])


# adjust lift capacity after envelope weight
lift_capacity = lift_capacity - envelope_weight
print("lift_capacity (kg)(lift capacity - envelope weight: ", lift_capacity)

# all other weight parameters
airship_frame = 49_000
print ("airship_frame(kg):",airship_frame)
airship_crew = 5_400
print("airship_crew weight (kg): ",airship_crew)
airship_provisions = 3_000
print("airship_provisions weight(kg): ", airship_provisions)
airship_fuel = 58_880
print("airship_fuel (kg): ", airship_fuel)
airship_oil = 4_000
print("airship_oil(kg): ", airship_oil)
airship_ballast = 7_950
print("airship_ballast(kg): ",airship_ballast)
airship_misc = 9_120
print("airship_misc(kg): ", airship_misc)




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
