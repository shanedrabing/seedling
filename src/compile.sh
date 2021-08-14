#!/bin/bash
g++ src/calc_dist.cpp src/utils_fasta.cpp src/dna_alignment.c -o bin/calc_dist;
g++ src/trim_region.cpp src/utils_fasta.cpp src/dna_alignment.c -o bin/trim_region;
