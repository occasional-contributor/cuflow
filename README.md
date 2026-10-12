# cuflow

CuFlow ("Copper Flow") is an experimental procedural PCB layout program.

It's a Python package that, given a description of a board, generates all the
outputs for a PCB:

 * Gerbers
 * drill file
 * BOM
 * PnP definitions
 * POVRay renderings
 * SVGs for laser cut mockups

The Gameduino 3X Dazzler was designed with CuFlow.

![Image of Dazzler PCB](images/dazzler-pcb.png)

## Layout

```
src/cuflow/     the library (import cuflow as cu)
examples/       board and demo scripts built on the library
tests/          regression suite (pytest)
tools/          repository tooling: preflight, assembly and topology checks
hardware/       EAGLE .lbr libraries used by some boards
assets/         STEP/WRL/STL models and artwork used by the web viewer
webviewer/      npm sidecar that renders the interactive 3D preview
preflight/      per-board manufacturing preflight profiles
```

## Install

CuFlow targets Python 3.9+.

```sh
python -m pip install -e '.[dev]'
```

`.[dev]` adds `pytest` and `ruff`. The optional grid router in `cuflow.router`
additionally needs `scipy`:

```sh
python -m pip install -e '.[router]'
```

## Generating boards

Board scripts live in `examples/` and are run **from the repository root**, so
their outputs (Gerbers, drills, previews) land in the repository root:

```sh
python examples/dazzler.py
python examples/arduino_dazzler.py
python examples/td2e2.py
```

## Tools

To fetch the STEP and WRL models for every LCSC code in a generated BOM:

```sh
python tools/fetch_bom_models.py spiq_a-bom.csv
```

Models are deduplicated by LCSC part number and written to `assets/step/`, for
example `assets/step/C25100.step` and `assets/step/C25100.wrl`. Existing model
pairs are left untouched unless `--overwrite` is supplied. The command keeps
successful downloads and exits nonzero if any BOM entry has no available model.
It also records EasyEDA's footprint transforms in `assets/step/models.json`.

To refresh the browser-ready mesh cache after fetching models:

```sh
npm --prefix webviewer run convert:models
```

STL assets can be converted to the same browser-ready mesh format. STL has no
standard units or material data, so the converter assumes millimetres and
accepts an optional RGB color:

```sh
node webviewer/convert-stl.js input.stl output.mesh.json [RRGGBB]
```

For the SPIQ LCD bezel:

```sh
npm --prefix webviewer run convert:bezel
```

## Testing and linting

```sh
python -m pytest
python -m ruff check src tools
```

## PCB manufacturing preflight

Before submitting a board, run the deterministic preflight checks from the
repository root:

```sh
python tools/pcb_preflight.py <board-name>
```

See `.agents/skills/pcb-manufacturing-preflight/SKILL.md` for the full process.

Some notes on the theory and the practice:

 * [Motivation](https://excamera.substack.com/p/how-would-bob-ross-lay-out-a-pcbhtml)
 * [The geometry of river routing](https://excamera.substack.com/p/the-geometry-of-river-routinghtml)
 * [The Dazzler PCB](https://excamera.substack.com/p/gameduino-dazzler-pcb-first-pictureshtml)
 * [laser cut mockups](https://excamera.substack.com/p/the-map-is-not-the-territoryhtml)

![POVRay rendering of Dazzler PCB](images/dazzler-spin000.png)
![Actual Dazzler PCB](images/dazzler-proto.jpg)
