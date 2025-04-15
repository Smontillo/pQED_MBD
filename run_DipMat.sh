#!/bin/bash
B=3.2                                 # Initial bond lenght.
dx=0.16                               # Step size.
Bfin=$(echo "(8 - $B) / $dx" | bc )   # Number of steps to reach the final bond lenght.
Binf=$(echo "(25 - $B) / $dx" | bc )  # Number of steps to reach the reference energy (25 A for Ar).

# =============================================================================================================
# Goes to each geomtry folder and create dipole information.
# =============================================================================================================

cd Calc_Res

for k in $(seq 0 $Bfin) $Binf; do
cd Geom$k
cp ../../get_HAM_and_DIP_Matrix.py .  # Copies the file for the dipole information
cp ../../submit.DIPOLES .
rm output.log 2>/dev/null
sbatch submit.DIPOLES

cd ../

done