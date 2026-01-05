#!/bin/bash
#SBATCH -p polariton
#SBATCH -J TransDens
#SBATCH -o output.slurm
#SBATCH -t 1:00:00
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH --mem 1GB

cp /Multiwfn_3.7_bin_Linux_noGUI/settings.ini .
# Generate ground state density: T_{00}
/Multiwfn_3.7_bin_Linux_noGUI/Multiwfn << EOF
../geometry.fchk
5
1
1
2
0
0
0
0
0
0
0
EOF

for state in {1..432}; do

echo "Generating first transition density for transition state ${state}."

/Multiwfn_3.7_bin_Linux_noGUI/Multiwfn << EOF
../geometry.fchk
18
1
../geometry.out
${state}
1
1
13
0
0
0
0
0
0
0
EOF
echo "Transition density for state ${state} generated."
mv transdens.cub trans-0_${state}.cube

done