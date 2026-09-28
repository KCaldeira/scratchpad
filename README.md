# scratchpad

Small one-off figures and scripts, one folder each.

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Contents

- `utility-function/` — CRRA utility U(c) = c^(1-η)/(1-η) with η = 1.5, showing marginal utility as tangent slopes at two consumption levels. Run `.venv/bin/python utility-function/utility_fig.py` to regenerate the PNG/PDF.
