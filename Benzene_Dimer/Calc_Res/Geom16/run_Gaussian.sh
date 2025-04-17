#!/bin/bash
#SBATCH -p reserved --reservation=phuo_20250312 #debug
#SBATCH -x bhd0005,bhc0024,bhd0020,bhd0001,bhd0007
#SBATCH -J OPT
#SBATCH -o output.slurm
#SBATCH -t 1-00:00:00
#SBATCH -N 1
#SBATCH --ntasks-per-node=24
#SBATCH --mem 10GB

module load gaussian

export OMP_NUM_THREADS=24
export MKL_NUM_THREADS=24

# ADD THIS TO ALL GAUSSIAN JOBS
export GAUSS_SCRDIR=/local_scratch/$SLURM_JOB_ID

g16 < geometry.com > geometry.out
formchk geometry.chk



