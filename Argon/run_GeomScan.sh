B=3.2                                 # Initial bond lenght.
dx=0.16                               # Step size.
Bfin=$(echo "(8 - $B) / $dx" | bc )   # Number of steps to reach the final bond lenght.
Binf=$(echo "(25 - $B) / $dx" | bc )  # Number of steps to reach the reference energy (25 A for Ar).

# =============================================================================================================
# Create a folder "Calc_Res" where all the single point caculations at different geometries are performed.
# =============================================================================================================

mkdir Calc_Res 2>/dev/null            
cd Calc_Res                   

for k in $(seq 0 $Bfin) $Binf; do     # Generates the geometries from B to Bfin and adds the geometry at Binf

mkdir Geom$k 2>/dev/null              # Creates the folder for each geometry
cd Geom$k
cp ../../geometry.com .
cp ../../run_Gaussian.sh .

B_i=$(echo "$B + $dx * $k" | bc -l)   # Calculates the bond lenght for geometry $k
Bf=$(printf "%.3f" "$B_i")            # Formats the lenght to 3 sig. figs.
echo "Step $k: B3 = $Bf"
sed -i "s/Ar         0.00000        0.00000       4.00000/Ar         0.00000        0.00000       $Bf/g"  geometry.com # Reads the input file and replaces the bond lenght. We need to find an efficient way to perform this for larger systems
sbatch run_Gaussian.sh   
cd ../

done