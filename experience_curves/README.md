# experience_curves

Analysis of the technology experience-curve (learning-rate) data described in:

> Carlino, A., Wongel, A., Duan, L., Virgüez, E., Davis, S. J., Edwards, M. R., & Caldeira, K. (2025).
> Variability of technology learning rates. *Advances in Applied Energy*, 20, 100252.
> https://doi.org/10.1016/j.adapen.2025.100252

- Paper page: https://ciunit.org/publications/carlino-2025-technology-learning-rates.html
- Data (Zenodo): https://doi.org/10.5281/zenodo.17179225

## Data

`data/input/ExpCurves.csv` has unit cost against cumulative production for 87
technologies, drawn from the Performance Curve Database. The file has 1,707 rows
and these columns:

| Column | Meaning |
| --- | --- |
| `Tech` | Technology name, e.g. `Wind_Turbine_2_(Germany)` |
| `Cumulative production` | Cumulative production to date |
| `Year` | Year of observation |
| `Unit cost` | Unit cost |
