# Panel Demo [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/danwild/panel-demo/HEAD)

A PyViz Panel demo for C3DIS.

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

