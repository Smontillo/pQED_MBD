#!/bin/bash
B=3.2                                 # Initial bond lenght.
dx=0.16                               # Step size.
Bfin=$(echo "(8 - $B) / $dx" | bc )   # Number of steps to reach the final bond lenght.
Binf=$(echo "(25 - $B) / $dx" | bc )  # Number of steps to reach the reference energy (25 A for Ar).

cd Calc_Res

# ==========================================================
# X POLARIZATION
# ==========================================================

for k in $(seq 0 20); do
echo "Geom$k"
cd Geom$k
cd X_pol
cp ../../../plot_polaritons.py .
rm output.log 2>/dev/null
rm -rf PLOTS_DATA/*

sed -i "s/EVEC_INTS = np.array([ 1,0,0 ])/EVEC_INTS = np.array([ 1,0,0 ])/g"  plot_polaritons.py

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

cd ../../
done

# ==========================================================
# Z POLARIZATION
# ==========================================================

for k in $(seq 0 20); do
echo "Geom$k"
cd Geom$k
cd Z_pol
cp ../../../plot_polaritons.py .
rm output.log 2>/dev/null
rm -rf PLOTS_DATA/*

sed -i "16c\    EVEC_INTS = np.array([ 0,0,1 ])"  plot_polaritons.py

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

cd ../../
done

# ==========================================================
# Y POLARIZATION
# ==========================================================

for k in $(seq 0 20); do
echo "Geom$k"
cd Geom$k
cd Y_pol
cp ../../../plot_polaritons.py .
rm output.log 2>/dev/null
rm -rf PLOTS_DATA/*

sed -i "16c\    EVEC_INTS = np.array([ 0,1,0 ])"  plot_polaritons.py

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

cd ../../
done