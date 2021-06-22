# Panel Demo [![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/danwild/panel-demo/main)

A PyViz [Panel](https://panel.holoviz.org/index.html) demo for C3DIS.

Notebooks:
- `1_bokeh_plot` - simple Bokeh plot example
- `2_panel_plot` - example of integrating Bokeh with a Panel app
- `3_panel_interactive` - example of Panel's declarative patterns for interactivity
- `4_panel_interactive` - move our logic to a python module

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

