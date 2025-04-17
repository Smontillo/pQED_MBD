# pQED - MBD

Repository to carry on pQED calculations with Many Body Dispersion corrections along a given coordinate. This reprository aims to reproduce the results presented by:

C. Tasci, L. A. Cunha and J. Flick on https://doi.org/10.1103/PhysRevLett.134.073002

## Tutorial (?)

### 1- Create the Gaussian input file.
The file must be named as **geometry.log**. This code is able to scan along a given coordinate for *Z-Matrix* input files (this must be change to work with a most general approach).

### 2- Run **run_GeomScan.sh**
A "Calc_Res" folder is created, inside of it a Geom folder for each of the geometries is created and the single TDDFT calculation is performed.

**Specify** 
 - B $\rightarrow$ Initial "bond lenght".
 - dx $\rightarrow$ Step size at which the bond will be vary. 

### 3- Run **run_DipMat.sh** 
Runs the "*get_HAM_and_DIP_Matrix.py*" at each geometry and creates the dipole data.

*IMPORTANT!!!* $\rightarrow$ Make sure that the path in the
function "**get_user_Globals()**" of "**get_HAM_and_DIP_Matrix.py**" matches the one in which your "*multiwfn*" is located.

**Specify** 
 - B $\rightarrow$ Initial "bond lenght".
 - dx $\rightarrow$ Step size at which the bond will be vary. 

### 4- Run **run_Polaritons.sh**
Creates the Pauli-Fierz hamiltonian and diagonalizes it to obtain the polaritonic energies at each geometry.

**Specify** 
 - B $\rightarrow$ Initial "bond lenght".
 - dx $\rightarrow$ Step size at which the bond will be vary. 
 - wc_MIN, wc_MAX $\rightarrow$ Cavity frequency, in Flick's paper, only one frequency is evaluated, so wc_MIN = wc_MAX.
 - lam_MIN, lam_MAX $\rightarrow$ Cavity coupling strength.
 - dlam $\rightarrow$ Step size of the cavity coupling strength.
 - EPOL $\rightarrow$ Polarization direction [X,Y,Z].
 - NM $\rightarrow$ Number of electronic states.
 - NF $\rightarrow$ Number of Fock states.
 
### 5- Run **run_PlotPolaritons.sh**

**Specify** 
 - B $\rightarrow$ Initial "bond lenght".
 - dx $\rightarrow$ Step size at which the bond will be vary. 
 - wc_LIST $\rightarrow$ List with one value.
 - lam_MIN, lam_MAX $\rightarrow$ Cavity coupling strength.
 - dlam $\rightarrow$ Step size of the cavity coupling strength.
 - EPOL $\rightarrow$ Polarization direction [X,Y,Z].

 ### 6- Run **Extract_data.py**

 Create a directory named "images".

 **Specify** 
 - B0 $\rightarrow$ Initial "bond lenght".
 - dx $\rightarrow$ Step size at which the bond will be vary. 
 - direc $\rightarrow$ Polarization direction.
 - λmin, λmax, dλ $\rightarrow$ Cavity coupling strength and step size.