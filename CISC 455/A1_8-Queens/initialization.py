"""
My collection of initialization methods for different representations

Student number: Raghav Taneja
Student name: 20058783
"""

#imports
import numpy as np


def permutation (pop_size, chrom_length):
    """initialize a population of permutation"""

    population = []
    # student code begin

    # Add each chromosome as follows:
    # Each element represents the position of the queen in the corresponding column
    population = np.random.randint(0, chrom_length, (pop_size, chrom_length))

    #student code end
    
    return population                     

