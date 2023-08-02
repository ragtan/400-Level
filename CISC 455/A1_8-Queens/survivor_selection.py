"""
My collection of survivor selection methods

Student number: Raghav Taneja
Student name: 20058783
"""

# imports
import numpy as np


def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """mu+lambda selection"""
    population = []
    fitness = []

    # student code starts
    current_pop = np.array(current_pop)
    offspring = np.array(offspring)

    all_together = np.concatenate([current_pop, offspring])
    fit_together = np.concatenate([current_fitness, offspring_fitness])

    # Concatenate everything together and sort
    chromo_fit = np.concatenate(
        [all_together, fit_together.reshape((-1, 1))], -1)

    latest = np.array(
        sorted(list(chromo_fit), key=lambda x: x[-1], reverse=True))[:len(current_pop)]

    population, fitness = latest[:, :-1], latest[:, -1]

    # student code ends

    return population, fitness


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""

    population = []
    fitness = []

    # student code starts
    to_remove = np.argsort(current_fitness)[:len(offspring)]

    population = np.array(current_pop).copy()
    population[to_remove] = np.array(offspring)

    fitness = np.array(current_fitness).copy()
    fitness[to_remove] = np.array(offspring_fitness)

    # student code ends

    return population, fitness


def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    """random uniform selection"""
    population = []
    fitness = []

    # student code starts
    current_pop = np.array(current_pop)
    offspring = np.array(offspring)

    all_together = np.concatenate([current_pop, offspring])
    fit_together = np.concatenate([current_fitness, offspring_fitness])

    # Concatenate everything together and sort
    chromo_fit = np.concatenate(
        [all_together, fit_together.reshape((-1, 1))], -1)

    indices = np.random.permutation(np.arange(len(chromo_fit)))[
        :len(current_pop)]
    population, fitness = chromo_fit[indices, :-1], chromo_fit[indices, -1]

    # student code ends

    return population, fitness
