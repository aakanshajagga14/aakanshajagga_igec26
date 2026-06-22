# Renewables AI Inequity Figures

This repository reproduces the figures used in the paper *Renewables, Algorithms, and Inequity: How Biased AI Shapes Energy Access in a Global Context*.

## Important note
These figures are synthetic and illustrative. They are not empirical deployment evidence.

## Structure
- `data/` — CSV inputs for each figure
- `scripts/` — figure generation code
- `figures/` — exported PNG outputs

## Setup
```bash
pip install -r requirements.txt
```

## Generate figures
```bash
python scripts/make_figures.py
```

## Output
The script writes:
- `figures/figure01.png`
- `figures/figure02.png`
- `figures/figure03.png`
- `figures/figure04.png`

Each PNG also has a sidecar `.meta.json` file for captioning and accessibility.

## Reproducibility
All numbers used in the plots are synthetic and stored in the `data/` folder so the figures can be regenerated exactly.
