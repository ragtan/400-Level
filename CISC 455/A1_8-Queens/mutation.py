"""
My colleciton of mutation methods

Student number: Raghav Taneja
Student name: 20058783
"""

# imports
import numpy as np


def permutation_swap (individual):
    """Mutate a permutation"""

    mutant = individual.copy()
    
    # student code starts

    # Choose two different positions to swap
    pos1, pos2 = np.random.choice(np.arange(len(individual)), 2, replace=False)
    # swap the values
    mutant[pos1] = individual[pos2]
    mutant[pos2] = individual[pos1]

   
    # student code ends
    
    return mutant
