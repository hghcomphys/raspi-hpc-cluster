#!/bin/sh

#SBATCH --mem=100mb
#SBATCH --tasks=2
#SBATH  --cpus-per-task=1 

module load OpenMPI


srun a.out 
