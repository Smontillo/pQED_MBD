#!/bin/bash

# Braden M. Weight, 2023

# Note: For single-point calculation, set MIN = MAX
B=3.2                                 # Initial bond lenght.
dx=0.16                               # Step size.
Bfin=$(echo "(8 - $B) / $dx" | bc )   # Number of steps to reach the final bond lenght.
Binf=$(echo "(25 - $B) / $dx" | bc )  # Number of steps to reach the reference energy (25 A for Ar).

# =============================================================================================================
# X POLARIZARIZATION
# =============================================================================================================
cd Calc_Res

for k in $(seq 0 20); do
echo "Geom$k"
cd Geom$k
mkdir X_pol 2>/dev/null
cd X_pol
rm data_PF/* 2>/dev/null
cp ../../../Pauli-Fierz_DdotE.py .
cp ../../../submit.polariton .

# This code takes as input the λ parameter as in 
# Flick et. al. https://doi.org/10.1103/PhysRevLett.134.073002
# A0 = λ / (2 * ωc)^(0.5)

WC_MIN="2.0"          # One frequency point
WC_MAX="2.0"
dWC="1.0"

lam_MIN='0.00'
lam_MAX='0.05'
dlam='0.05'

E_POL="100" # Electric field polarization. 
            # Input as three positive integers. 
            # Will normalize later.

NM=200      # Number of electronic states
NF=10       # Number of photonic Fock states

Nlam=$(printf %.0f $(echo "($lam_MAX-$lam_MIN)/$dlam" | bc -l))
NWC=$(printf %.0f $(echo "($WC_MAX-$WC_MIN)/$dWC" | bc -l))

for (( a=0; a<=Nlam; a++ )); do
        # A0=$( bc -l <<< $a*$dA0+$A0_MIN )
        lam=$( bc -l <<< $a*$dlam+$lam_MIN )
        sbatch submit.polariton ${lam} ${NM} ${NF} ${NWC} ${WC_MIN} ${WC_MAX} ${dWC} ${E_POL}
        # sbatch submit.polariton ${A0} ${NM} ${NF} ${NWC} ${WC_MIN} ${WC_MAX} ${dWC} ${E_POL}
done
cd ../../
done

# =============================================================================================================
# Z POLARIZARIZATION
# =============================================================================================================


for k in $(seq 0 20); do
echo "Geom$k"
cd Geom$k
mkdir Z_pol 2>/dev/null
cd Z_pol
rm data_PF/* 2>/dev/null
cp ../../../Pauli-Fierz_DdotE.py .
cp ../../../submit.polariton .

E_POL="001" # Electric field polarization. 
            # Input as three positive integers. 
            # Will normalize later.

NM=200      # Number of electronic states
NF=10       # Number of photonic Fock states

Nlam=$(printf %.0f $(echo "($lam_MAX-$lam_MIN)/$dlam" | bc -l))
NWC=$(printf %.0f $(echo "($WC_MAX-$WC_MIN)/$dWC" | bc -l))

for (( a=0; a<=Nlam; a++ )); do
        # A0=$( bc -l <<< $a*$dA0+$A0_MIN )
        lam=$( bc -l <<< $a*$dlam+$lam_MIN )
        sbatch submit.polariton ${lam} ${NM} ${NF} ${NWC} ${WC_MIN} ${WC_MAX} ${dWC} ${E_POL}
        # sbatch submit.polariton ${A0} ${NM} ${NF} ${NWC} ${WC_MIN} ${WC_MAX} ${dWC} ${E_POL}
done
cd ../../
done

# =============================================================================================================
# Y POLARIZARIZATION
# =============================================================================================================


for k in $(seq 0 20); do
echo "Geom$k"
cd Geom$k
mkdir Y_pol 2>/dev/null
cd Y_pol
rm data_PF/* 2>/dev/null
cp ../../../Pauli-Fierz_DdotE.py .
cp ../../../submit.polariton .

E_POL="010" # Electric field polarization. 
            # Input as three positive integers. 
            # Will normalize later.

NM=200      # Number of electronic states
NF=10       # Number of photonic Fock states

Nlam=$(printf %.0f $(echo "($lam_MAX-$lam_MIN)/$dlam" | bc -l))
NWC=$(printf %.0f $(echo "($WC_MAX-$WC_MIN)/$dWC" | bc -l))

for (( a=0; a<=Nlam; a++ )); do
        # A0=$( bc -l <<< $a*$dA0+$A0_MIN )
        lam=$( bc -l <<< $a*$dlam+$lam_MIN )
        sbatch submit.polariton ${lam} ${NM} ${NF} ${NWC} ${WC_MIN} ${WC_MAX} ${dWC} ${E_POL}
        # sbatch submit.polariton ${A0} ${NM} ${NF} ${NWC} ${WC_MIN} ${WC_MAX} ${dWC} ${E_POL}
done
cd ../../
done

