"""
This is the main entrypoint to run the Panel Demo application.
"""

import panel as pn
from panel_plot import get_controls, get_plot

pn.extension()

app_name = 'Panel Demo'

# extends https://panel.holoviz.org/api/panel.template.html#panel.template.base.BasicTemplate
bootstrap = pn.template.BootstrapTemplate(
    title=app_name,
    header_background='#004B87'
)
pn.config.sizing_mode = 'stretch_width'

bootstrap.sidebar.append(get_controls())
bootstrap.main.append(get_plot())

bootstrap.servable()
