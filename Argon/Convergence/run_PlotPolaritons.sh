#!/bin/bash
source Parameters.txt
# GEOMETRY
Bfin=$(echo "($Bf0 - $B) / $dx" | bc )   # Number of steps to reach the final bond lenght.
Binf=$(echo "($Bref - $B) / $dx" | bc )  # Number of steps to reach the reference energy (25 A for Ar).
# ELECTRONIC STATES
nSteps=$(echo "($nStf - $nSt0) / $dSt" | bc )

cd Calc_Res
# ==========================================================
# X POLARIZATION
# ==========================================================
for k in $Bfin $Binf; do
echo "Geom$k"
cd Geom$k
for m in $(seq 0 $nSteps); do     # Scan over the electronic states
cd nSt_$m
cd X_pol
cp ../../../../plot_polaritons.py .
rm output.log 2>/dev/null
rm -rf PLOTS_DATA/*

sed -i "16c\    EVEC_INTS = np.array([ 1,0,0 ])"  plot_polaritons.py
nSt=$(echo "$nSt0 + $dSt * $m" | bc)
sed -i "13c\    NM        = $nSt"  plot_polaritons.py

cat << Eof > sbatch_HEOM.sh
#!/bin/bash
#SBATCH -p debug
#SBATCH -o output.log
#SBATCH --mem=1GB
#SBATCH --time=1:00:00
#SBATCH --cpus-per-task=1
#SBATCH --job-name=plot
#SBATCH --open-mode=append

python3 plot_polaritons.py

Eof

chmod +x sbatch_HEOM.sh
sbatch sbatch_HEOM.sh

cd ../..
done
cd ../
done

# # ==========================================================
# # Z POLARIZATION
# # ==========================================================
for k in $Bfin $Binf; do
echo "Geom$k"
cd Geom$k
for m in $(seq 0 $nSteps); do     # Scan over the electronic states
cd nSt_$m
cd Z_pol
cp ../../../../plot_polaritons.py .
rm output.log 2>/dev/null
rm -rf PLOTS_DATA/*

sed -i "16c\    EVEC_INTS = np.array([ 0,0,1 ])"  plot_polaritons.py
nSt=$(echo "$nSt0 + $dSt * $m" | bc)
sed -i "13c\    NM        = $nSt"  plot_polaritons.py

cat << Eof > sbatch_HEOM.sh
#!/bin/bash
#SBATCH -p debug
#SBATCH -o output.log
#SBATCH --mem=1GB
#SBATCH --time=1:00:00
#SBATCH --cpus-per-task=1
#SBATCH --job-name=plot
#SBATCH --open-mode=append

python3 plot_polaritons.py

Eof

chmod +x sbatch_HEOM.sh
sbatch sbatch_HEOM.sh

cd ../..
done
cd ../
done

# # ==========================================================
# # Y POLARIZATION
# # ==========================================================
for k in $Bfin $Binf; do
echo "Geom$k"
cd Geom$k
for m in $(seq 0 $nSteps); do     # Scan over the electronic states
cd nSt_$m
cd Y_pol
cp ../../../../plot_polaritons.py .
rm output.log 2>/dev/null
rm -rf PLOTS_DATA/*

sed -i "16c\    EVEC_INTS = np.array([ 0,1,0 ])"  plot_polaritons.py
nSt=$(echo "$nSt0 + $dSt * $m" | bc)
sed -i "13c\    NM        = $nSt"  plot_polaritons.py

cat << Eof > sbatch_HEOM.sh
#!/bin/bash
#SBATCH -p debug
#SBATCH -o output.log
#SBATCH --mem=1GB
#SBATCH --time=1:00:00
#SBATCH --cpus-per-task=1
#SBATCH --job-name=plot
#SBATCH --open-mode=append

python3 plot_polaritons.py

Eof

chmod +x sbatch_HEOM.sh
sbatch sbatch_HEOM.sh

cd ../..
done
cd ../
done