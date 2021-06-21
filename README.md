# Panel Demo
---

## Run: Docker

```shell
make run # -> http://localhost:5006/panel_app
```

## Install: Conda

```
conda env create -f environment.yml
conda activate panel_demo
```

## Run: Conda 

```
# Bokeh server:
panel serve --show src/panel_app.py

# Jupyter Lab:
jupyter lab
```

