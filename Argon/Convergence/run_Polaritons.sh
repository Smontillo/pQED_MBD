#!/bin/bash

# Braden M. Weight, 2023

# Note: For single-point calculation, set MIN = MAX
source Parameters.txt
# GEOMETRY
Bfin=$(echo "($Bf0 - $B) / $dx" | bc )   # Number of steps to reach the final bond lenght.
Binf=$(echo "($Bref - $B) / $dx" | bc )  # Number of steps to reach the reference energy (25 A for Ar).
# ELECTRONIC STATES
nSteps=$(echo "($nStf - $nSt0) / $dSt" | bc )
# CAVITY PARAMETERS
# This code takes as input the λ parameter as in 
# Flick et. al. https://doi.org/10.1103/PhysRevLett.134.073002
# A0 = λ / (2 * ωc)^(0.5)

cd Calc_Res
# =============================================================================================================
# X POLARIZARIZATION
# =============================================================================================================
echo "X POLARIZATION ----> 100"
E_POL="100" # Electric field polarization. 
for k in $Bfin $Binf; do
echo "Geometry -> $k"
for m in $(seq 0 $nSteps); do     # Scan over the electronic states
cd Geom$k
cd nSt_$m
mkdir X_pol 2>/dev/null
cd X_pol
rm data_PF/* 2>/dev/null
cp ../../../../Pauli-Fierz_DdotE.py .
cp ../../../../submit.polariton .

nSt=$(echo "$nSt0 + $dSt * $m" | bc)
echo "Number of El. St. -> $nSt" 
NM=$nSt      # Number of electronic states

Nlam=$(printf %.0f $(echo "($lam_MAX-$lam_MIN)/$dlam" | bc -l))
NWC=$(printf %.0f $(echo "($WC_MAX-$WC_MIN)/$dWC" | bc -l))

for (( a=0; a<=Nlam; a++ )); do
        lam=$( bc -l <<< $a*$dlam+$lam_MIN )
        sbatch submit.polariton ${lam} ${NM} ${NF} ${NWC} ${WC_MIN} ${WC_MAX} ${dWC} ${E_POL}
done
cd ../../../
done
done

# =============================================================================================================
# Z POLARIZARIZATION
# =============================================================================================================
echo "Z POLARIZATION ----> 001"
E_POL="001" # Electric field polarization. 
for k in $Bfin $Binf; do
echo "Geometry -> $k"
for m in $(seq 0 $nSteps); do     # Scan over the electronic states
cd Geom$k
cd nSt_$m
mkdir Z_pol 2>/dev/null
cd Z_pol
rm data_PF/* 2>/dev/null
cp ../../../../Pauli-Fierz_DdotE.py .
cp ../../../../submit.polariton .

nSt=$(echo "$nSt0 + $dSt * $m" | bc)
echo "Number of El. St. -> $nSt" 
NM=$nSt      # Number of electronic states

Nlam=$(printf %.0f $(echo "($lam_MAX-$lam_MIN)/$dlam" | bc -l))
NWC=$(printf %.0f $(echo "($WC_MAX-$WC_MIN)/$dWC" | bc -l))

for (( a=0; a<=Nlam; a++ )); do
        lam=$( bc -l <<< $a*$dlam+$lam_MIN )
        sbatch submit.polariton ${lam} ${NM} ${NF} ${NWC} ${WC_MIN} ${WC_MAX} ${dWC} ${E_POL}
done
cd ../../../
done
done

# =============================================================================================================
# Y POLARIZARIZATION
# =============================================================================================================
echo "Y POLARIZATION ----> 010"
E_POL="010" # Electric field polarization. 
for k in $Bfin $Binf; do
echo "Geometry -> $k"
for m in $(seq 0 $nSteps); do     # Scan over the electronic states
cd Geom$k
cd nSt_$m
mkdir Y_pol 2>/dev/null
cd Y_pol
rm data_PF/* 2>/dev/null
cp ../../../../Pauli-Fierz_DdotE.py .
cp ../../../../submit.polariton .

nSt=$(echo "$nSt0 + $dSt * $m" | bc)
echo "Number of El. St. -> $nSt" 
NM=$nSt      # Number of electronic states

Nlam=$(printf %.0f $(echo "($lam_MAX-$lam_MIN)/$dlam" | bc -l))
NWC=$(printf %.0f $(echo "($WC_MAX-$WC_MIN)/$dWC" | bc -l))

for (( a=0; a<=Nlam; a++ )); do
        lam=$( bc -l <<< $a*$dlam+$lam_MIN )
        sbatch submit.polariton ${lam} ${NM} ${NF} ${NWC} ${WC_MIN} ${WC_MAX} ${dWC} ${E_POL}
done
cd ../../../
done
done