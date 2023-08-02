"""
My collection of parent selection methods

Student number: Raghav Taneja
Student name: 20058783
"""

# imports
import numpy as np




def MPS(fitness, mating_pool_size):
    """Multi-pointer selection (MPS)"""

    selected_to_mate = []

    # student code starts
    fit = np.array(fitness)
    
    # Get distribution and cumulative distribution
    dist = fit / fit.sum()
    cdist = np.cumsum(dist)

    # Start selection
    i = 0
    r = np.random.random() * (1 / mating_pool_size)
    while len(selected_to_mate) < mating_pool_size:
        while r <= cdist[i]:
            # Add to pool
            selected_to_mate.append(i)
            # Update r and current member
            r += (1 / mating_pool_size)
        i += 1

    selected_to_mate = selected_to_mate[:mating_pool_size]

    # student code ends
    
    return selected_to_mate


def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""

    selected_to_mate = []

    # student code starts
    n = len(fitness)

    while len(selected_to_mate) < mating_pool_size:
        # Select a tournament pool randomly
        indices = np.random.choice(np.arange(n), tournament_size, replace=False)
        
        # Get the corresponding fitness
        fit = np.array(fitness)[indices]

        # Add the best to the pool
        selected_to_mate.append(indices[np.argmax(fit)])



    # student code ends
    
    return selected_to_mate


def random_uniform (population_size, mating_pool_size):
    """Random uniform selection"""

    selected_to_mate = []

    # student code starts
    # Select random indices
    selected_to_mate = list(np.random.permutation(np.arange(population_size))[:mating_pool_size])

    # student code ends
    
    return selected_to_mate

