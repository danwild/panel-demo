import panel as pn
import numpy as np
import pandas as pd
import param
import holoviews as hv
from bokeh.plotting import figure, show
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput

pn.extension()

# DO DATA, SCIENCE
N = 200
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))

# DO PLOT
plot = figure(
    plot_height=400, 
    plot_width=400, 
    title="Dan's amazing sine wave",
    tools="hover,crosshair,pan,reset,save,wheel_zoom",
    x_range=[0, 4*np.pi], 
    y_range=[-2.5, 2.5]
)
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

class InputParams(param.Parameterized): 
    phase = param.Number(0.0, bounds=(0, 2 * np.pi), step=0.1)
    frequency = param.Number(1.0, bounds=(0, 5), step=0.1)

input_params = InputParams()

@pn.depends(input_params.param.phase, input_params.param.frequency)
def data_source(phase, frequency):
    x = np.linspace(0, 4 * np.pi, N)
    y = np.sin(frequency*x + phase)
    source.data = dict(x=x, y=y)

# AMAZE ME
bokeh_pane = pn.pane.Bokeh(plot)


def get_controls():
  return pn.Column(
    input_params.param.phase, 
    input_params.param.frequency, 
)

def get_plot():
  return pn.Column(
    bokeh_pane, 
    data_source
  )