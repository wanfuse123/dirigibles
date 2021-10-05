# import all modules
from Airship import *
import random
import numpy as np


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
    for m in [CO2Mass, H2Mass, O2Mass, N2Mass, SilaneMass, AmmoniaMass, AirMass, H2OMass, HeliumMass]:
        
        # loop through different range of temperature
        for t in range(0, 1500, 100):
            result_array.append([
                m, 
                t,
                #gas_mass(pascal(1.01325), 1, Kelvin(t), m)
                gas_mass(pascal(5.06625), 1, Kelvin(t), m)

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
    title="Title",
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
    'He' : HeliumMass,
    'H2O': H2OMass
}
temp_range = [x for x in range(0, 2500, 100)]
for g in gases:

    mass_range = []    
    # loop through different range of temperature
    x=0
    for t in temp_range:
        x=x+1
        plotpointsX[x]= mass_range.append(gas_mass(pascal(1.01325), 1, Kelvin(t), gases[g]))
        plotpointsY[x]= t
    # plot trace / series
    fig.add_trace(
        go.Scatter(
             x=temp_range, 
             y=mass_range,  
            name=g,  # legend
            line_shape='spline' # line type
        )
    )
#    fig.add_trace(
#        go.Scatter( 
#        x=temp_range[t],y=mass_range[g], #np.array(mass_range),
#        x=plotpointsX[x],y=mass_range[g] 
#        text=(plotpointsX,mass_range[g]) 
#        textfont=dict(size=15,color='white'), 
#        textposition="top right",
#        line_shape='spline',
#        hoverinfo=text, mode='lines+markers',
#        hoverinfo='text+name', mode='lines+markers', 
#        show_grid='True',
#        name=g )) 

fig.update_traces(textposition='top center')
fig.update_layout(title=go.layout.Title(text="Changes in Density of Various Gasses as it Relates to Changes in Temperature", font=dict(
                family="Courier New, monospace",
                size=22,
                color="#0000FF"
            )))
#fig.update_traces(hoverinfo='text+name', mode='lines+markers')

# show figure
fig.show()


"""
3D plot
"""

# Generate graph using Figure Constructor
#layout = go.Layout(
#    title="Historic Prices",
#    xaxis_title="time",
#    yaxis_title="price"
#)
# create a figure / canvas to plot on



fig = go.Figure(layout=go.Layout(
    title= "Title",
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
    'He' : HeliumMass,
    'H2O': H2OMass
}
#temp_range = [x for x in range(100, 2500, 100)]
#pres_range = [x for x in np.arange(1, 6, .25)]
#for g in gases:

#    mass_range = []    
    # loop through different range of temperature
#    for t in temp_range:
#        mass_range.append([])
        # loop through different range of pressure
#        for p in pres_range:
#            mass_range[-1].append(gas_mass(pascal(p), 1, Kelvin(t), gases[g]))
#    fig = go.Figure(layout=go.Layout(
#	title='My Title goes here',
#        xaxis={
#            'title': 'Temperature, *C'
#        },
#	yaxis={
#            'title': 'Density, kg.m^-3'
#        }
#    ))

#    fig.add_trace(
#        go.Surface(
#            x=temp_range, 
#            y=pres_range,  
#            z=mass_range,
#            name=g,  # legend
#        )
#    )

# # update layout
fig.update_layout(
    scene = {
        'xaxis': {
            'title': 'Temperature, °C'
        },
        'yaxis': {
            'title': 'Pressure, bar'
        },
        'zaxis': {
            'title': 'Density, kg.m^-3'
        },
    }
)

# show figure
fig.show()
