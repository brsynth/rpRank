# rpRank

Rank a list of pathways according to their global score.

## Input

Positional arguments:
* **pathways**: (list of string) Paths to pathway (rpSBML) files

Optional arguments:
* **delimiter**: (string) CSV delimiter character

# Installation Guide

## Overview

`rprank` depends on `rplibs`, which depends on `cobra`, which requires `python-libsbml`.
On Apple Silicon (`arm64`) macOS, `python-libsbml` is not available as a native Conda package.

Therefore, installation must be done using an **Intel (`osx-64`) Conda environment under Rosetta**.

---

## General case
```bash
conda install -c conda-forge rprank
```

---

## Apple Silicon macOS (M1/M2/M3)

### 1. Install Rosetta 2

```bash
softwareupdate --install-rosetta --agree-to-license
```

### 2. Install rpRank

```bash
CONDA_SUBDIR=osx-64 conda install -c conda-forge rprank
```

Or with mamba:

```bash
CONDA_SUBDIR=osx-64 mamba install -c conda-forge rprank
```

### 3. Persist platform setting

```bash
conda config --env --set subdir osx-64
```

### 4. Verify installation

```bash
python -c "import rprank; print('rprank installed successfully')"
```

### 5. (Optional) Dev installation

```bash
CONDA_SUBDIR=osx-64 conda env create -f environment.yaml
```

---

## Troubleshooting

### Solver fails on Apple Silicon

Make sure you are using:

```bash
CONDA_SUBDIR=osx-64
```

### Wrong architecture environment

Check:

```bash
conda config --show subdir
```

Expected output:

```bash
subdir: osx-64
```

## Run

**From Python code**
```python
from rplibs import rpPathway
from rprank import rank

pathways = {}
for pathway_fname in ["pathway_1.xml", "pathway_2.xml"]:
    pathway = rpPathway(infile=pathway_fname)
    pathways[pathway.get_id()] = {"pathway": pathway, "filename": pathway_fname}

sorted_pathways = rank(pathways)
```
**From CLI**
```sh
python -m rprank --pathways <pathway_1> <pathway_2> ...
```

## Tests
Test can be run with the following commands:

### Natively
```bash
cd tests
pytest -v
```

## CI/CD
For further tests and development tools, a CI toolkit is provided in `ci` folder (see [ci/README.md](ci/README.md)).

## Authors

* **Jean-Loup Faulon**
* **Joan Hérisson**

## Acknowledgments

* Thomas Duigou

## Licence
rpRank is released under the MIT licence. See the LICENSE file for details.
