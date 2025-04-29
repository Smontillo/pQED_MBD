cp Parameters.py Parameters.txt
source Parameters.txt
# GEOMETRY
Bfin=$(echo "($Bf0 - $B) / $dx" | bc )   # Number of steps to reach the final bond lenght.
Binf=$(echo "($Bref - $B) / $dx" | bc )  # Number of steps to reach the reference energy (25 A for Ar).
# ELECTRONIC STATES
nSteps=$(echo "($nStf - $nSt0) / $dSt" | bc )
# =============================================================================================================
# Create a folder "Calc_Res" where all the single point caculations at different geometries are performed.
# =============================================================================================================

mkdir Calc_Res 2>/dev/null            
cd Calc_Res                   

for k in $Bfin $Binf; do     # Generates the geometries from B to Bfin and adds the geometry at Binf

mkdir Geom$k 2>/dev/null              # Creates the folder for each geometry
cd Geom$k
cp ../../geometry.com .
cp ../../run_Gaussian.sh .

B_i=$(echo "$B + $dx * $k" | bc -l)   # Calculates the bond lenght for geometry $k
Bf=$(printf "%.3f" "$B_i")            # Formats the lenght to 3 sig. figs.
echo "Step $k: B3 = $Bf"
sed -i "s/Ar         0.00000        0.00000       4.00000/Ar         0.00000        0.00000       $Bf/g"  geometry.com # Reads the input file and replaces the bond lenght. We need to find an efficient way to perform this for larger systems

# =============================================================================================================
# TDDFT nstates modifications.
# =============================================================================================================
for m in $(seq 0 $nSteps); do     # Scan over the electronic states
mkdir nSt_$m 2>/dev/null
cd nSt_$m
cp ../geometry.com .
cp ../run_Gaussian.sh .

nSt=$(echo "$nSt0 + $dSt * $m" | bc)
echo "  Number of El. St. -> $nSt"
sed -i "6c\#p TD=(singlets,nstates=$nSt) IOp(6/8=3) IOp(9/40=4)"  geometry.com
sbatch run_Gaussian.sh   
cd ../
done
cd ../
done