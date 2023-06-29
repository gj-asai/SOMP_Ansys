# SOMP_Ansys

## Auxiliar files

- `2dstiff.py`: symbolic calculation to determine the expression for $\frac{\partial c}{\partial \theta}$, writes `python/dkdt2d.py`. Not used in the optimization
- `3dstiff.py`: symbolic calculation to determine the expression for $\frac{\partial c}{\partial \theta}$, writes `python/dkdt3d.py`. Not used in the optimization
- `SimpleExample.ipynb`: Jupyter notebook with an example of 2D and 3D optimizations
- `bridge.py`: example of a complete 2D optimization. Uses MPI to launch parallel processes with different initial orientations
- `global3d.py`: example of a complete 3D optimization. Uses MPI to launch parallel processes with different initial orientations and volume fraction constraints

## Usage 

### Ansys configuration

- `TopOpt.load_paths(ANSYS_path, script_dir, res_dir, mod_dir)`: vonfigures the paths to be used by all `TopOpt` objects
  - `ANSYS_path : pathlib.Path`: MAPDL executable path
  - `script_dir : pathlib.Path`: folder with .py files and .txt APDL scripts
  - `res_dir : pathlib.Path`: folder to store results. Individual job results can be stored in subfolders of it
  - `mod_dir : pathlib.Path`: folder with the .db file (geometry, mesh, constraints, loads)

### Model files

- For 2D optimization: use 4-node 2D quad elements (PLANE182) in a rectangular domain, with KEYOPT(3) = 3 (plane stress with thk)
- For 3D optimization: use 8-node 3D hex elements (SOLID185) in a cuboid domain

### Class `TopOpt`

- `TopOpt(inputfile, Ex, Ey, nuxy, nuyz, Gxy, volfrac, r_rho, r_theta, theta0, max_iter, move_rho, move_theta, dim, jobname, echo)`
  - `inputfile`: name of the model file (without .db)
  - `Ex`, `Ey`, `nuxy`, `nuyz`, `Gxy`: material properties (considered transverse isotropic, symmetry plane $yz$)
  - `volfrac`: volume fraction constraint for the optimization
  - `r_rho`: radius of the density filter (adjusts minimum feature size)
  - `r_theta`: radius of the orientation filter (adjusts fiber curvature)
  - `max_iter`: number of iterations
  - `move_rho`: move limit for densities
  - `move_theta`: move limit for orientations, in degrees
  - `theta0`: initial orientation of the fibers, in degrees
  - `dim`: optimization type, `'2D'` or `'3D'`
  - `jobname`: optional. Subfolder of `TopOpt.res_dir` to store results for this optim. Defaults to no subfolder, stores results directly on `TopOpt.res_dir`
  - `echo`: boolean. Print compliance at each iteration?

- `TopOpt.set_solid_elem(self, solid_elem)`: list of elements whose densities will be fixed on 1. Indexing starting at 0

- `TopOpt.optim(self)`: runs the optimization and returns the density `rho` and the orientation `theta` of each element as separate `numpy.array`

### Class `PostProcessor`

- `Post2D(solver)`, `Post3D(solver)`
- `CO2_footprint(self, rho, CO2mat, CO2veh)`: returns the CO2 footprint for the final design
  - `rho`: density
  - `CO2mat`: mass CO2 emmited per mass material (material production)
  - `CO2veh`: mass CO2 emitted per mass material during life (use in a vehicle) = mass fuel per mass transported per lifetime * service life * mass CO2 emmited per mass fuel
- `plot_convergence(self, starting_iteration=0)`: plots the convergence history
- `plot(self, iteration=-1, filename=None, save=True, fig=None, ax=None)`: plots the configuration (densities and orientations)
- `plot_layer(self, iteration=-1, layer=0, filename=None, save=True, fig=None, ax=None)`: only for 3D. Plots layer `layer` as a 2D plot, easier to visualise
