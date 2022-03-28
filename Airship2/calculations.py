# import all modules
from Airship import *


"""
Example Zeppelin calculations to test that all functions are working
"""
# Zeppelin volume calculations
zeppelin_volume = ellipsoid_volume(245.0/2, 41.2/2, 41.2/2)
print("elipsoid Volume Parameters: ", "245m x 41.2 m x 41.2m")

print("zepplin_volume: ",zeppelin_volume)

# Zeppelin lift calculations
air_mass = gas_mass(pascal(1), 200000, Kelvin(5), AirMass)
hydrogen_mass = gas_mass(pascal(1), 200000, Kelvin(5), H2Mass)
lift_capacity = air_mass - hydrogen_mass
print("Air Mass: ", air_mass, "Hydrogen Mass: ",hydrogen_mass, "Lift Capacity: ",lift_capacity)

# Weight of envelope
# Goodyear Zeppelin has 1.5 mm thick polyester envelope. Polyester (mylar) has a density of 1390 kg/m³
envelope_area = prolate_spheroid_area(41.2/2, 245.0/2)
envelope_thickness = 0.0015
envelope_density = 1390
envelope_weight = envelope_area * envelope_thickness * envelope_density
print("Envelope Area: ", envelope_area, "Envelope_Weight: ",envelope_weight)

# adjust lift capacity after envelope weight

# all other weight parameters
airship_frame = 49_000
airship_crew = 5_400
airship_provisions = 3_000
airship_fuel = 58_880
airship_oil = 4_000
airship_ballast = 7_950
airship_misc = 9_120

print("lift capacity is defined as lift_capacity -envelope_weight -airship_frame -airship_crew -airship_provisions - airship_fuel -airship_oil -airship_ballast -airship_misc ")
print(" ")
Adjusted_lift_capacity = lift_capacity -envelope_weight -airship_frame -airship_crew -airship_provisions - airship_fuel -airship_oil -airship_ballast -airship_misc

print("Adjusted Lift Capacity: ",Adjusted_lift_capacity)





#**********************************
# Our large airship



"Example Zeppelin calculations to test that all functions are working"

# Zeppelin volume calculations
zeppelin_volume = ellipsoid_volume(3000/2, 500/2, 500/2)
print("elipsoid Volume Parameters: ", "3000m x 500 m x 500m")

print("zepplin_volume: ",zeppelin_volume)

# Zeppelin lift calculations
air_mass = gas_mass(pascal(1), 200000, Kelvin(5), AirMass)
helium_mass = gas_mass(pascal(1), 200000, Kelvin(5), HeliumMass)
lift_capacity = air_mass - hydrogen_mass
print("Air Mass: ", air_mass, "Helium Mass: ",helium_mass, "Lift Capacity: ",lift_capacity)

# Weight of envelope
# Goodyear Zeppelin has 1.5 mm thick polyester envelope. Polyester (mylar) has a density of 1390 kg/m³
envelope_area = prolate_spheroid_area(41.2/2, 245.0/2)
envelope_thickness = 0.0015
envelope_density = 1390
envelope_weight = envelope_area * envelope_thickness * envelope_density
print("Envelope Area: ", envelope_area, "Envelope_Weight: ",envelope_weight)

# adjust lift capacity after envelope weight

# all other weight parameters
airship_frame = 49_000
airship_crew = 5_400
airship_provisions = 3_000
""" Each reactor should be an HTR with high-assay low-enriched uranium (HALEU) TRISO fuel and produce a threshold power of 1-10 MWe for at least three years without refuelling. It must weigh less than 40 tonnes and be sized for transportability by truck, ship, and C-17 aircraft. Designs must be "inherently safe", ensuring that a meltdown is "physically impossible" in various complete failure scenarios such as loss of power or cooling, and must use ambient air as their ultimate heat sink, as well as being capable of passive cooling. The reactor must be capable of being installed to the point of "adding heat" within 72 hours and of completing a planned shutdown, cool down, disconnect and removal of transport in under seven days. The DOD announced its preparation of an environmental impact statement for the reactor in March 2020, and awarded $12-14 million contracts to three companies for initial design work. Then BWXT Advanced Technologies and X-energy were selected in March 2021 to develop a final engineering design by March 2022. Westinghouse has dropped out, and one of the two companies may be commissioned in 2022 to build a prototype reactor.
"""
nuclear_fuel = 5000
airship_MSR = 50000
airship_ballast = 7_950
airship_misc = 9_120
print("From google: Each module weighs less than 50 tons. It has both active and passive safety features. ")

print(" ")

print("Adjusted_lift_capacity = lift_capacity -envelope_weight -airship_frame -airship_crew -airship_provisions - nuclear_fuel -airship_MSR -airship_ballast -airship_misc ")

Adjusted_lift_capacity = lift_capacity -envelope_weight -airship_frame -airship_crew -airship_provisions - nuclear_fuel -airship_MSR -airship_ballast -airship_misc


print("Adjusted Lift Capacity: ",Adjusted_lift_capacity)





def nested_for():
    result_array = []
    
    # loop through different gases
    for m in [CO2Mass, H2Mass, O2Mass, N2Mass]:
        
        # loop through different range of temperature
        for t in range(0, 101, 10):
            result_array.append([
                CO2Mass, 
                t,
                gas_mass(pascal(1), 1, Kelvin(t), m)
            ])

    return result_array


print(nested_for())



import plotly.graph_objects as go
import numpy as np

# pressure array
pres = np.array([x for x in range(1, 11, 1)])

# volume array
vol = np.array([gas_volume(1, Kelvin(20), x) for x in range(1, 11, 1)])

# create a figure / canvas to plot on
fig = go.Figure(layout=go.Layout(
    title='Title',
    xaxis={
        'title': 'X'
    },
    yaxis={
        'title': 'Y'
    }
))

# linear / line chart
fig.add_trace(
    go.Scatter(
        x=vol, 
        y=pres, 
        name="linear",  # legend
        line_shape='linear' # line type
    )
)

# spline / poly chart
fig.add_trace(
    go.Scatter(
        x=vol, 
        y=pres + 1, # just to shift the 2 curves apart to see the different line types :) 
        name="spline",  # legend
        line_shape='spline' # line type
    )
)

# show figure
fig.show()
