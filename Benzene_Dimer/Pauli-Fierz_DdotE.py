import numpy as np
from numpy import kron as kron_prod
import sys
# import subprocess as sp # Not good for Windows OS
import os

##### Braden M. Weight #####
#####  April 17, 2023  #####

# SYNTAX: python3 Pauli-Fierz_DdotE.py NM NF A0 WC EVEC_INTS

def get_globals():
    global NM, NF, A0, wc_eV, wc_AU, λ
    global EVEC_INTS, EVEC_NORM, EVEC_OUT
    global RPA, WRITE_WFNS, do_CS, PATH_TO_TDDFT

    PATH_TO_TDDFT = "../" # Path to where the TDDFT was run and where {PATH_TO_TDDFT}/PLOTS_DATA is located.

    NM         = int( sys.argv[1] )  # Number of Electronic States (including ground state)
    NF         = int( sys.argv[2] )  # Number of Fock Basis States
    RPA        = True                # If True, look for TD-DFT/RPA data rather than TD-DFT/TDA data
    WRITE_WFNS = False                # If True, writes <alpha,n|\Phi_j> -- All polaritonic wfns in full adiabatic-Fock basis
                                     # (NM=50,NF=50) --> WF ~ 48 MB
    do_CS      = True                # If True, perform Coherent State shift: \\hat{mu} --> \\hat{mu} - \\mu_{00} I_{el}
    λ          = float( sys.argv[3] ) # a.u.
    wc_eV      = float( sys.argv[4] ) # eV
    EVEC_INTS  = [ int(j) for j in sys.argv[5] ] # e.g., "111", "001" # Cavity Polarization Vector (input as integers without normalizing)
    
    wc_AU     = wc_eV / 27.2114
    A0         = λ / (2 * wc_AU)**(0.5)
    EVEC_NORM = EVEC_INTS / np.linalg.norm(EVEC_INTS)
    EVEC_OUT = "_".join(map(str,EVEC_INTS))

    #sp.call("mkdir -p data_PF", shell=True) # Not good for Windows OS
    try: os.mkdir("data_PF")
    except FileExistsError: pass

def get_a_op(nf):
    a = np.zeros((nf,nf))
    for m in range(1,nf):
        a[m,m-1] = np.sqrt(m)
    return a.T

def get_H_PF(EAD, MU):
    """
    Input: HAD,   Adiabatic hamiltonian (diagonal) energies from electronic structure
    Output: H_PF, Pauli-Fierz Hamiltonian using Adiabatic-Fock basis states
    """

    print (f"Dimension = {(NM*NF)}")

    I_ph = np.identity(NF)
    I_el = np.identity(NM)
    a_op = get_a_op(NF)
    q_op = a_op.T + a_op
    MU   = np.einsum("d,JKd->JK", EVEC_NORM[:], MU[:,:,:] )
    if ( do_CS == True ):
        MU = MU - MU[0,0] * I_el # Subtract off the shift from the diagonal

    H_EL = np.diag( EAD )
    H_PH = np.diag( np.arange(NF) * wc_AU )

    H_PF   = kron_prod(H_EL, I_ph)                        # Matter
    H_PF  += kron_prod(I_el, H_PH)                        # Photon

    H_PF  += kron_prod(MU, q_op) * wc_AU * A0             # Interaction
    H_PF  += kron_prod(MU @ MU, I_ph) * wc_AU * A0**2     # Dipole Self-Energy

    if ( H_PF.size * H_PF.itemsize * 10 ** -9 > 0.5 ): # If H_PF larger than 0.5 GB, tell the user but do nothing.
        print(f"\tWARNING!!! Large Matrix" )
        print(f"\tMemory size of numpy array in (MB, GB): ({round(H_PF.size * H_PF.itemsize * 10 ** -6,2)},{round(H_PF.size * H_PF.itemsize * 10 ** -9,2)})" )

    return H_PF

def get_ADIABATIC_DATA():

    EAD  = np.zeros(( NM ))
    MU  = np.zeros(( NM,NM,3 ))

    if ( RPA == True ):
        EAD += np.loadtxt(f"{PATH_TO_TDDFT}/PLOTS_DATA/ADIABATIC_ENERGIES_RPA.dat")[:NM] # in AU
        MU  += np.load(f"{PATH_TO_TDDFT}/PLOTS_DATA/DIPOLE_RPA.dat.npy")[:NM,:NM] # in AU
    else:
        EAD += np.loadtxt(f"{PATH_TO_TDDFT}/PLOTS_DATA/ADIABATIC_ENERGIES_TDA.dat")[:NM] # in AU
        MU  += np.load(f"{PATH_TO_TDDFT}/PLOTS_DATA/DIPOLE_TDA.dat.npy")[:NM,:NM] # in AU

    return EAD, MU

def SolvePlotandSave(H_PF,EAD,MU):

        # Diagonalize Hamiltonian
        E, U = np.linalg.eigh( H_PF ) # This is exact solution --> Should we ever try Davidson diagonalization ?
        
        # Save Data
        np.savetxt( f"data_PF/E_{EVEC_OUT}_lam_{round(λ,6)}_WC_{round(wc_eV,6)}_NF_{NF}_NM_{NM}.dat", [E[0] * 27.2114] )
        # np.savetxt( f"data_PF/E_{EVEC_OUT}_A0_{round(A0,6)}_WC_{round(wc_eV,6)}_NF_{NF}_NM_{NM}.dat", E * 27.2114 )
        if ( WRITE_WFNS ):
            #np.savetxt( f"data_PF/U_{EVEC_OUT}_A0_{round(A0,6)}_WC_{round(wc_eV,6)}_NF_{NF}_NM_{NM}.dat", U ) # These can be large
            np.save( f"data_PF/U_{EVEC_OUT}_A0_{round(A0,6)}_WC_{round(wc_eV,6)}_NF_{NF}_NM_{NM}.dat.npy", U ) # Binary is smaller

        print ( "Finished (A0, wc):", A0, wc_eV )

        # Save original EAD and MU for convenience
        np.savetxt( f"data_PF/EAD.dat", EAD * 27.2114 )
        np.save( f"data_PF/MU.dat", MU )

def main():
    get_globals()

    EAD, MU = get_ADIABATIC_DATA() 
    H_PF    = get_H_PF( EAD, MU )
    SolvePlotandSave( H_PF, EAD, MU)

    


if __name__ == "__main__":
    main()