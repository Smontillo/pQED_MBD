# =============================================================================================================
# Create a folder "Calc_Res" where all the single point caculations at different geometries are performed.
# =============================================================================================================
points=$(python GenGeom.py)
echo "Total Geometries -> $points"
cd Calc_Res                   

for k in $(seq 0 $points); do     # Generates the geometries from B to Bfin and adds the geometry at Binf
echo "Step $k"
cd Geom$k
cp ../../run_Gaussian.sh .
# sbatch run_Gaussian.sh   
cd ../

done