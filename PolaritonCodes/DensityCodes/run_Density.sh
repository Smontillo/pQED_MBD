#!/bin/bash
#SBATCH -p  polariton #reserved --reservation=phuo_20250312 #debug
#SBATCH -J OPT
#SBATCH -o output.slurm
#SBATCH -t 1:00:00
#SBATCH -N 1
#SBATCH --ntasks-per-node=12
#SBATCH --mem 10GB

python compute_properties.py



