# Panel Demo [![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/danwild/panel-demo/main)

A PyViz [Panel](https://panel.holoviz.org/index.html) demo for C3DIS:

[But can it do X? A software journey to be all things to all people, starring: Python, Jupyter, and Panel](http://www.c3dis.com/events/but-can-it-do-x-a-software-journey-to-be-all-things-to-all-people-starring-python-jupyter-and-panel)

---

Notebooks:
- `1_bokeh_plot` - simple Bokeh plot example
- `2_panel_plot` - example of integrating Bokeh with a Panel app
- `3_panel_interactive` - example of Panel's declarative patterns for interactivity
- `4_modularize` - move our logic to a python module

## Build, run: Docker

```shell
# see Makefile for cmd's if not using make
make build
make run # -> http://localhost:5006/panel_app
make stop
```

## Install: Conda

```
conda env create -f environment.yml
conda activate panel_demo
```

## Run: Conda 

```shell
# Bokeh server:
panel serve --show src/panel_app.py # -> http://localhost:5006/panel_app

# Jupyter Lab:
jupyter lab
```

## Links

- [Panel's comparisons](https://panel.holoviz.org/about/comparisons.html)
- [Stephen Kilcommins, Streamlit vs Dash vs Voilà vs Panel — Battle of The Python Dashboarding Giants](https://medium.datadriveninvestor.com/streamlit-vs-dash-vs-voil%C3%A0-vs-panel-battle-of-the-python-dashboarding-giants-177c40b9ea57)
- [Jupyter Dashboarding — some thoughts on Voila, Panel and Dash](https://medium.com/informatics-lab/jupyter-dashboarding-some-thoughts-on-voila-panel-and-dash-b84df9c9482f)
- [Original "Research Impact Pathway" graphic](https://www.nature.com/articles/s41467-019-12020-z)


