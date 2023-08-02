"""
My collection of fitness evaluation methods

Student number: Raghav Taneja
Student name: 20058783
"""

#imports
import numpy as np


def fitness_8queen (individual): 
    """Compute fitness of an invidual for the 8-queen puzzle (maximization)"""    

    fitness = 0
    # student code begin

    # Get the size
    n = len(individual)

    non_conflicts = 0
    
    for row in range(n):
    	col = individual[row]
    	
    	for row_x in range(n):
    		col_x = individual[row_x]
    		
    		# Check for same point and row/col conflict
    		if (row_x == row) or (col_x == col):
    			continue

    		# Check for diagonal conflicts
    		if (row_x + col_x == row + col) or (row_x - col_x == row - col):
    			continue

    		non_conflicts += 1

    fitness = non_conflicts/2

    # student code end
    
    return fitness


