#!/bin/bash
B=3.2                                 # Initial bond lenght.
dx=0.16                               # Step size.
Bfin=$(echo "(8 - $B) / $dx" | bc )   # Number of steps to reach the final bond lenght.
Binf=$(echo "(25 - $B) / $dx" | bc )  # Number of steps to reach the reference energy (25 A for Ar).

cd Calc_Res

for k in $(seq 0 $Bfin) $Binf; do
echo "Geom$k"
cd Geom$k
cd PF_run
cp ../../../plot_polaritons.py .
rm output.log 2>/dev/null
rm -rf PLOTS_DATA/*

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