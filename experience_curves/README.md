# experience_curves

Analysis of the technology experience-curve (learning-rate) data described in:

> Carlino, A., Wongel, A., Duan, L., Virgüez, E., Davis, S. J., Edwards, M. R., & Caldeira, K. (2025).
> Variability of technology learning rates. *Advances in Applied Energy*, 20, 100252.
> https://doi.org/10.1016/j.adapen.2025.100252

- Paper page: https://ciunit.org/publications/carlino-2025-technology-learning-rates.html
- Data (Zenodo): https://doi.org/10.5281/zenodo.17179225

## Data

`data/input/ExpCurves.csv` has unit cost against cumulative production for 87
technologies from the Performance Curve Database (1,707 rows). It is the file from
the authors' code release v4.0 on Zenodo (`carnegie/clab_experience_curve-v4.0.zip`),
MD5 `0e662032b72c644073d02f7d92d28829`, redistributed under the MIT licence in
`data/input/LICENSE`. Its cumulative production already includes the paper's
correction to initial production.

| Column | Meaning |
| --- | --- |
| `Tech` | Technology name, e.g. `Wind_Turbine_2_(Germany)` |
| `Cumulative production` | Cumulative production to date |
| `Year` | Year of observation |
| `Unit cost` | Unit cost |
| `Normalized cumulative production` | Cumulative production divided by its first value |
| `Normalized unit cost` | Unit cost divided by its first value |

An earlier copy here came from the authors' v1.0 release (2023), whose
cumulative-production values differ and give noticeably different learning rates
(unweighted median 22.7% instead of 17.9%). Don't use it.

The maintained version of this analysis is in the `ciunit.github.io` repo, under
`additional_analyses/carlino-2025-technology-learning-rates/`. It has the same script
and data, and this folder's outputs match it.

The paper PDF (with supplement) is kept in this folder for reference but is
gitignored.

## Analysis

`scripts/learning_rates.py` fits Wright's model (paper Eqs. 1–3) to each
technology:

    log(C) = log(alpha) + beta * log(P)        LR = 100 * (1 - 2**beta)

`beta` is the learning exponent and `LR` the learning rate (% cost decline per
doubling of cumulative production). Each technology gets one constant `beta`,
fit by ordinary least squares on all of its points.

Run from this folder:

    ../.venv/bin/python scripts/learning_rates.py

It prints summary statistics and writes to `data/output/`:

| File | Contents |
| --- | --- |
| `learning_rates_by_tech.csv` | Per technology: number of points, `log10_P_range` (log10 of last minus first cumulative production), `beta`, `LR_percent` |
| `learning_rate_summary.csv` | Mean and std of `beta`, and the learning rates implied at the mean `beta` and at mean ± 1 std. Four columns: unweighted and weighted by `log10_P_range`, each with and without `Nuclear_Electricity` |
| `learning_rates_vs_production_range.png` | `beta` and `LR` for each technology against `log10_P_range` |

Notes:

- Nuclear electricity is a strong outlier (`beta` ≈ +1.03, LR ≈ −104%), which is
  why the summary is also given without it.
- Unweighted std uses n − 1; weighted std is the population form.
- These single-fit statistics are not the paper's pooled values (mean −0.33,
  std 0.35; Supplementary Table 2), which come from the segments of its
  piecewise fits.
