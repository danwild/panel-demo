# Panel Demo [![Binder](https://binder.pangeo.io/badge_logo.svg)](https://binder.pangeo.io/v2/gh/danwild/panel-demo/binder)

A PyViz [Panel](https://panel.holoviz.org/index.html) demo for C3DIS.

Notebooks:
- `bokeh_plot` - simple Bokeh plot example
- `panel_plot` - example of integrating Bokeh with a Panel app
- `panel_interactive` - example of Panel's declarative patterns for interactivity

## Build, run: Docker

```shell
make build
make run # -> http://localhost:5006/panel_app
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

