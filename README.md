# Quantum Geometry at the Monkey Saddle in Biased Bernal Bilayer Graphene

M.Sc. thesis project, School of Physical Sciences, NISER Bhubaneswar (2026).
Author: Rajat Shuvra Saha. Guide: Dr Kush Saha.

## What this is about

In Bernal bilayer graphene, a perpendicular gate bias reshapes the bottom of the
conduction band. Near **V_c = 40 meV** three ordinary van Hove saddles merge into one
cubic "monkey" saddle, and the density of states diverges as |E − E_c|^(−1/3).

Recent work (Kitamura, Daido, Yanase 2024) showed that the **quantum metric** of the
Bloch states can, on its own, push the spin response towards ferromagnetism, but only
at a saddle where two bands touch and the metric diverges. Here the band stays gapped
and the metric is finite. This project asks:

> At the monkey saddle, are the ferromagnetic fluctuations caused by the band's
> geometry, or just by the shape of the band?

## Main results

- **Exact density of states** at V_c:
  ν(E) = B(1/2, 1/6) / (12π²) · A^(−2/3) |E − E_c|^(−1/3),
  giving χ⁰(0) ∝ T^(−1/3). This matches the four-band numerics to within 1%.
- **Closed-form quantum geometry** at the saddle. The two channels whose sum sets the
  k² coefficient α(V) add in the metric g and cancel in the Berry curvature Ω:
  g = 5.44 nm², and Ω_xy = 0 at V ≈ 0.995 V_c.
- **Split of the spin susceptibility curvature**, χ_e = χ_geom + χ_mass. Checked against a
  direct finite-q bubble and against a control model with the same energies but trivial
  wavefunctions; the two agree to better than 1%.
- **Where geometry wins.** Near the saddle energy, the band shape sets the sign of χ_e.
  Geometry decides for μ − V/2 ≳ 4.2 meV at every bias, and at the saddle itself only
  for V > V_c and T ≲ 5 K.
- **Caveat.** In those regions q = 0 is only a local maximum of χ⁰(q). The largest
  response sits at q ≈ 0.28 nm⁻¹, so within RPA a finite-q instability would come first.

In one line: the monkey saddle realises the geometric mechanism in a gapped,
gate-tunable band, but only as a correction to a response that is mostly set by the
band shape.

## Model

Four-band continuum Hamiltonian for valley K, basis (A1, B1, A2, B2), with π = k_x + i k_y:

```
H = | V/2      v π†     0        v3 π  |
    | v π      V/2      γ1       0     |
    | 0        γ1      −V/2      v π†  |
    | v3 π†    0        v π     −V/2   |
```

Parameters: v = 0.658 eV·nm, γ1 = 0.40 eV, v3 = 0.1 v.
Because H is linear in k, all velocity matrix elements and band curvatures are exact
sums over the four states, with no finite differences.

## Methods

- Critical points found on the mirror lines by Brent root finding, with exact Hessians.
- Brillouin-zone integrals over a 60° wedge (×6 by C3 symmetry and mirrors), using
  Gauss–Legendre polar grids refined near the saddle region.
- Full Fermi functions on all four bands. The Fermi-sea tail is extrapolated in 1/k_max.
- Convergence: raising the inner cutoff from 0.6 to 0.8 nm⁻¹, or adding one third more
  angular points, changes none of the quoted digits.
- Benchmark: the gapped band-touching saddle model of Kitamura et al., which this code
  reproduces.



## Reproducing the figures

Access the wolfram and jupyter notebooks uploaded in the repository.

## Limitations

- Bare bubble only. Interactions enter only through RPA, and vertex corrections could
  change whether q = 0 or q ≈ 0.28 nm⁻¹ wins.
- One valley and one spin. Intervalley (isospin) channels are not included.
- Minimal hoppings (v, γ1, v3). Adding γ4 and Δ′ shifts V_c.

## Key references

- T. Kitamura, A. Daido, Y. Yanase, Phys. Rev. Lett. (2024); arXiv:2304.11536
- N. F. Q. Yuan, H. Isobe, L. Fu, Nat. Commun. 10, 5769 (2019)
- A. Shtyk, G. Goldstein, C. Chamon, Phys. Rev. B 95, 035137 (2017)
- H. Zhou et al., Science 375, 774 (2022)
- A. M. Seiler et al., Nature 608, 298 (2022)
- S. C. de la Barrera et al., Nat. Phys. 18, 771 (2022)
- S. Peotta, P. Törmä, Nat. Commun. 6, 8944 (2015)
- E. McCann, M. Koshino, Rep. Prog. Phys. 76, 056503 (2013)

## Acknowledgements

I thank Dr Kush Saha and Akash Dey (SPS, NISER) for their help with this project.

## Citation

If you use this code or the results, please cite the thesis:

```
R. S. Saha, "Quantum Geometric Effects at the Monkey Saddle Lifshitz Point in
Biased Bernal Bilayer Graphene", M.Sc. thesis, NISER Bhubaneswar (2026).
```
