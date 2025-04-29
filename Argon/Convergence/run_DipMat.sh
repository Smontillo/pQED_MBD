#!/bin/bash
source Parameters.txt
# GEOMETRY
Bfin=$(echo "($Bf0 - $B) / $dx" | bc )   # Number of steps to reach the final bond lenght.
Binf=$(echo "($Bref - $B) / $dx" | bc )  # Number of steps to reach the reference energy (25 A for Ar).
# ELECTRONIC STATES
nSteps=$(echo "($nStf - $nSt0) / $dSt" | bc )
# =============================================================================================================
# Goes to each geomtry folder and create dipole information.
# =============================================================================================================

cd Calc_Res

for k in $Bfin $Binf; do
echo "Geometry -> $k"
cd Geom$k
for m in $(seq 0 $nSteps); do     # Scan over the electronic states
echo "States -> $m"
cd nSt_$m
cp ../../../get_HAM_and_DIP_Matrix.py .  # Copies the file for the dipole information
cp ../../../submit.DIPOLES .
rm output.log 2>/dev/null
sbatch submit.DIPOLES

cd ../
done
cd ../
done