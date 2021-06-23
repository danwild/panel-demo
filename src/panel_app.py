"""
This is the main entrypoint to run the Panel Demo application.
"""

import panel as pn
from panel_plot import get_controls, get_plot

pn.extension()
pn.config.sizing_mode = 'stretch_width'

bootstrap = pn.template.BootstrapTemplate(
    title='Panel Demo',
    header_background='#004B87'
)

bootstrap.sidebar.append(get_controls())
bootstrap.main.append(get_plot())

bootstrap.servable()
