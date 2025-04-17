#!/bin/bash
#SBATCH -p debug
#SBATCH -o output.log
#SBATCH --mem=1GB
#SBATCH --time=1:00:00
#SBATCH --cpus-per-task=1
#SBATCH --job-name=plot
#SBATCH --open-mode=append

python3 plot_polaritons.py

