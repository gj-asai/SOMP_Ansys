# from mpi4py import MPI

from pathlib import Path
import numpy as np
import time

from python.optimization import TopOpt3D
from python.postprocessor import Post3D

ANSYS_path = Path('C:/Program Files/ANSYS Inc/v202/ansys/bin/winx64/MAPDL.exe')
script_dir = Path('python/')
res_dir    = Path('results/3d/')
mod_dir    = Path('models/')
TopOpt3D.load_paths(ANSYS_path, script_dir, res_dir, mod_dir)
TopOpt3D.set_processors(2)

# Ex   = 113.6e3 # MPa
# Ey   = 9.65e3 # MPa
# Gxy  = 6e3 # MPa
# nuxy = 0.334

# fiber: bamboo
rhofiber  = 700e-12 # t/mm^3
Efiber    = 17.5e3 # MPa
vfiber    = 0.04
CO2fiber  = 1.0565 # kgCO2/kg

# matrix: cellulose
rhomatrix = 990e-12 # t/mm^3
Ematrix   = 3.25e3
vmatrix   = 0.355 # MPa
CO2matrix = 3.8 # kgCO2/kg

Vfiber  = 0.5
Vmatrix = 1-Vfiber

Gfiber  = Efiber/(2*(1+vfiber))
Gmatrix = Ematrix/(2*(1+vmatrix))

Ex   = Efiber*Vfiber + Ematrix*Vmatrix
Ey   = Efiber*Ematrix / (Efiber*Vmatrix + Ematrix*Vfiber)
Gxy  = Gfiber*Gmatrix / (Gfiber*Vmatrix + Gmatrix*Vfiber)
nuxy = vfiber*Vfiber + vmatrix*Vmatrix
rho  = rhofiber*Vfiber + rhomatrix*Vmatrix

CO2mat = (rhofiber*Vfiber*CO2fiber + rhomatrix*Vmatrix*CO2matrix)/rho # kgCO2/kg
CO2veh = 1030 * 25 * 3.83 # kg_fuel/kg_transported/year * years * kgCO2/kg_fuel = kgCO2/kg

# t0 = MPI.Wtime()
t0 = time.time()

# comm = MPI.COMM_WORLD
# rank = comm.Get_rank()
# size = comm.Get_size()
rank = 0
size = 1

# size should be odd to include 0 degrees
theta0 = np.linspace(-70, 90, num=size)

solver = TopOpt3D(inputfile='mbb3d', Ex=Ex, Ey=Ey, nuxy=nuxy, nuyz=nuxy, Gxy=Gxy, volfrac=0.3, r_rho=6, r_theta=16, theta0=theta0[rank], jobname=str(int(theta0[rank])))
solver.set_optim_options(max_iter=1, move_rho=0.4, move_theta=5.)
solver.optim()
print('\n{} - Elasped time: {:.2f}s'.format(rank, solver.time))
print('{} - FEA time: {:.2f}s'.format(rank, solver.mma.fea_time))
print('{} - Derivation time: {:.2f}s'.format(rank, solver.mma.deriv_time))
print('{} - Variable updating time: {:.2f}s\n'.format(rank, solver.mma.iter_time))

post = Post3D(solver)
post.plot_convergence()
# post.animate()
post.plot()
post.animate_layer(layer=0)
post.plot_layer(layer=1)

# comp  = comm.gather(solver.comp_hist[-1])
# niter = comm.gather(solver.mma.iter)
# dt    = comm.gather(solver.time)
comp  = [solver.comp_hist[-1]]
niter = [solver.mma.iter]
dt    = [solver.time]

if rank == 0:
    print('\n theta0      comp    iter    time')
    for i in range(size):
        print('{:7.1f}  {:7.2f} {:7d} {:7.2f}'.format(theta0[i],comp[i],niter[i],dt[i]))

    # import os, glob
    # for filename in glob.glob('*.bat'): os.remove(filename)
    # for filename in glob.glob('*.err'): os.remove(filename)
    # for filename in glob.glob('*.log'): os.remove(filename)
    # for filename in glob.glob('*.out'): os.remove(filename)
    
    print('\nTotal elapsed time: {:.2f}s'.format(time.time()-t0))

