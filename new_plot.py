# import all modules
from Airship import *
import random
import plotly.graph_objects as go
import numpy as np

# create a figure / canvas to plot on
fig = go.Figure(
    layout=go.Layout(
        title='Changes in Density of Various Gasses as it Relates to Changes in Temperature',
        xaxis={
            'title': 'Temperature, °C'
        },
        yaxis={
            'title': 'Density, kg.m^-3'
        },
        font={
            'family': "Courier New, monospace",
            'size': 22,
            'color': "#0000FF"
        }
    )
)

# define gases
gases = {
##    'CO2': CO2Mass,
    'Si': SilaneMass,
    'Air': AirMass,    
    'N2': N2Mass,
##    'H2O': H2OMass,
    'NH4': AmmoniaMass,
##    'He': HeliumMass,
    'H2O': H2OMass,
    'H2': H2Mass
}
temp_range = [x for x in range(0, 2500, 100)]
annotations = []
for g in gases:

    mass_range = []
    # loop through different range of temperature
    for t in temp_range:
        y = gas_mass(pascal(1.01325), 1, Kelvin(t), gases[g])
        mass_range.append(y)

        # add annotations
        fig.add_annotation(
            dict(
                font=dict(
                    color='rgba(0,0,200,0.8)'
                    ,size=12
                ),
                x=t,
                y=y,
                showarrow=False,
                text='{}, {:.2f}'.format(t, y),
                textangle=0,
                xanchor='left',     # marker would be on the left
                yanchor='bottom',   # marker would be on the bottom
                xref="x",
                yref="y"
            )
        )

    # add series
    fig.add_trace(
        go.Scatter(
            x=temp_range, 
            y=mass_range,
            textfont=dict(size=15, color='white'),
            textposition="top right",
            line_shape="spline",
            mode="lines+markers",
            name=g,
        )
    )

# update axis range and gridline/ticks spacing
fig.update_xaxes(
    range=[0, 2500], 
    dtick=100
)
fig.update_yaxes(
    range=[0, .9], 
    dtick=.1
)
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Red')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', gridcolor='Red')

# show figure
fig.show()
