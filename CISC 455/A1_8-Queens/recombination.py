"""
My collection of recombination methods
 
Student number: Raghav Taneja
Student name: 20058783
"""

# imports
import numpy as np


def permutation_cut_and_crossfill(parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []

    # student code begin

    # Get a random index to cut things
    ind = np.random.randint(len(parent1))

    # Combine for offspring 1
    offspring1 = list(parent1[:ind]) + list(parent2[ind:])

    # And for offspring 2
    offspring2[:ind] = list(parent2[:ind]) + list(parent1[ind:])

    # student code end

    return offspring1, offspring2
