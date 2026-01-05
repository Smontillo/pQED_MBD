import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
# import subprocess as sp
import os

def get_globals():
    global NM, NF, WC_LIST, lam_LIST
    global EVEC_INTS, EVEC_NORM, EVEC_OUT
    global DATA_DIR, NPOL, NWC, EMAX, Nlam

    ##### MAIN USER INPUT SECTION #####
    NM        = 432                  # Number of Electronic States (including ground state)
    NF        = 20                   # Number of Fock Basis States
    EMAX      = 1                   # Maximum Energy for plot (eV)
    EVEC_INTS = np.array([ 1,0,0 ])
    
    lam_MIN  =0.0
    lam_MAX  =0.1
    dlam     =0.025
    NA    = int((lam_MAX - lam_MIN)/dlam) + 1
    lam_LIST = [lam_MIN + x * dlam for x in range(NA)]
    print(lam_LIST)
    WC_LIST  = [2.0] #np.arange( 0.0, 20+1.0, 1.0 )
    ##### END USER INPUT SECTION  #####



    ##### DO NOT MODIFY BELOW HERE #####
    NPOL = 1 #NM * NF
    Nlam = len(lam_LIST)
    NWC  = len(WC_LIST)

    EVEC_NORM = EVEC_INTS / np.linalg.norm(EVEC_INTS)
    EVEC_OUT = "_".join(map(str,EVEC_INTS))

    DATA_DIR = "PLOTS_DATA"
    # sp.call(f"mkdir -p {DATA_DIR}", shell=True) # Not good for Windows OS
    try: os.mkdir("PLOTS_DATA")
    except FileExistsError: pass

def get_energies():

    EPOL = np.zeros(( NPOL, Nlam, NWC ))

    for A0IND, lam in enumerate( lam_LIST ):
        for WCIND, WC in enumerate( WC_LIST ):
            lam = round( lam, 5 )
            WC = round( WC, 5 )
            EPOL[0, A0IND, WCIND]  = np.loadtxt(f"data_PF/E_{EVEC_OUT}_lam_{lam}_WC_{WC}_NF_{NF}_NM_{NM}.dat")
    # np.save(f"{DATA_DIR}/EPOL.dat.npy", EPOL)
    return EPOL



def plot_A0SCAN_WCFIXED( EPOL, PHOT ):

    EZERO = EPOL[0,0,0]
    cmap=mpl.colors.LinearSegmentedColormap.from_list('rg',[ "red", "darkred", "black", "darkgreen", "palegreen" ], N=256)
    #cmap=mpl.colors.LinearSegmentedColormap.from_list('rg',[ "black", "grey", "red", "orange", "yellow" ], N=256)
    for WCIND, WC in enumerate( WC_LIST ):
        WC = round( WC, 5 )
        print(f"Plotting WC = {WC} eV")
        mask = (EPOL[:,:,WCIND] - EZERO) < EMAX
        VMAX = np.max(PHOT[mask,WCIND])
        for state in range( NPOL ):
            plt.scatter( lam_LIST, EPOL[state,:,WCIND] - EZERO, s=25, cmap=cmap, c=PHOT[state,:,WCIND], vmin=0.0, vmax=VMAX )
        
        plt.colorbar(pad=0.01,label="Average Photon Number")
        plt.xlim(lam_LIST[0], lam_LIST[-1])
        plt.ylim(-0.01, EMAX)
        plt.xlabel( "Coupling Strength, $A_0$ (a.u.)", fontsize=15 )
        plt.ylabel( "Polariton Energy (eV)", fontsize=15 )
        plt.savefig( f"{DATA_DIR}/EPOL_A0SCAN_WC_{WC}.jpg", dpi=600 )
        plt.clf()
        print(EZERO)
        np.savetxt('Polariton_data.dat', np.c_[lam_LIST, EPOL[0,:,0]])

def main():
    get_globals()
    EPOL = get_energies()
    # PHOT = get_average_photon_number()
    np.savetxt('Polariton_data.dat', np.c_[lam_LIST, EPOL[0,:,0]])
    # plot_A0SCAN_WCFIXED( EPOL, PHOT )
    # plot_WCSCAN_A0FIXED( EPOL, PHOT )
    


if __name__ == "__main__":
    main()