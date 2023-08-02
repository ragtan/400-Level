import csv
import random
import itertools
import numpy as np
import pandas as pd


fileName = "trainingSamples.txt"

'''
convert the given text file to a csv file
for readability and so we can easily utilize
the tools from the pandas library
'''

dataFrame = pd.read_csv(fileName, delimiter='\t')
dataFrame.columns = ['x1', 'x2', 'f(x1,x2)']
dataFrame.to_csv('trainingSamples.csv', index=None)

dataFrame = pd.read_csv("trainingSamples.csv")

'''
define constants, operands, and registers
'''
constants = [str(x) for x in range(1, 6)]
ops = ['add', 'sub', 'mul', 'mod']
src_regs = ['r0', 'r1', 'r2', 'r3', 'r4']

'''
generates a random instruction,
or calls random mov
'''
def rand_instruction():
    p_mov = 0.5

    # valid instructions:
    # mov src dst
    # op (r0 = r3 op r4)

    if random.random() < p_mov:
        # return a mov instruction
        return rand_mov()

    else:
        return random.choice(ops)

'''
generates a random mov
'''
def rand_mov():
    p_const = 0.5
    dst_regs = ['r3', 'r4']
    src = random.choice(constants) if random.random() < p_const else random.choice(src_regs)
    dst = random.choice(dst_regs)
    return ' '.join(['mov', src, dst])

'''
returns a random instruction in range of n
'''
def rand_program(n):
    return [rand_instruction() for _ in range(n)]

def print_program(prog):
    print('\n'.join(prog))

'''
executes a program by utilizing
the training data and operations
which are defined above
'''
def exec_program(prog, x1, x2):
    # r0 is r[0], etc
    r = [0, x1, x2, 0, 0]

    for instr in prog:
        op = instr[:3]
        if op == 'add':
            r[0] = r[3] + r[4]
        elif op == 'sub':
            r[0] = r[3] - r[4]
        elif op == 'mul':
            r[0] = r[3] * r[4]
        elif op == 'mod':
            r[0] = r[3] % r[4] if r[4] != 0 else 0
        else:
            mov, src, dst = instr.split()
            # if the src is a register get the value from that register
            if src in src_regs:
                src = r[int(src[1])]
            else:
                src = int(src)
            if dst == 'r3':
                r[3] = src
            else:
                r[4] = src

    return r[0]

'''
initialize population of 100 programs,
each of length 5-10
'''
def initialPop(n=100):
    return [rand_program(random.randint(5,10)) for _ in range(n)]

'''
finds fitness of an individual/program
by sum of squared errors
'''
def fitness(ind):
    sum = 0
    for index,row in dataFrame.iterrows():
        x = exec_program(ind, row['x1'], row['x2'])
        diff = x - row['f(x1,x2)']
        sum += diff**2
    return sum

'''
takes in population and the number of selections
to be made from the population (k) and performs
tournament selection on the contenders 
'''
def tournament(population, k):
    n = len(population)
    winner = population[np.random.randint(0, n-1)]
    for i in range(1, k):
        contender = population[np.random.randint(0, n-1)]
        if fitness(contender) <= fitness(winner):
            winner = contender
    return winner

'''
performs single point crossover by taking
in two parents, p1 and p2
'''
def crossover(p1, p2):
    p1 = list(p1)
    p2 = list(p2)
    k = np.random.randint(0, min(len(p1), len(p2))-1)

    for i in range(k):
        p1[i], p2[i] = p2[i], p1[i]

    return p1, p2

'''
peforms a micro or macro mutation,
rates are applied accordingly
'''
def mutate(c):
    microMutRate = 0.25
    macroMutRate = 1 - microMutRate
    p = random.random()
    n = len(c)
    #makes random operand or mov choice
    if p < microMutRate:
        k = np.random.randint(0,n-1)
        if c[k] in ops:
            c[k] = random.choice(ops)
        else:
            c[k] = rand_mov()
    #deletes a single instruction in child
    elif p < (microMutRate + (macroMutRate/2)):
        #delete
        k = np.random.randint(0,n-1)
        c = c[:k] + c[k+1:]
    #inserts a single instruction in child
    else:
        #insert
        k = np.random.randint(0, n - 1)
        inst = rand_instruction()
        c = c[:k] + [inst] + c[k:]
    return c

#main utilizes all the methods above
def main():
    numEvals = 0
    maxEvals = 10000
    popSize = 100
    population = initialPop(popSize)
    sortedPop = sorted(population, key=fitness)
    print(population)
    while numEvals < maxEvals:
        sortedPop = sorted(population, key=fitness)
        p1 = tournament(population, 3)
        p2 = tournament(population, 3)
        c1, c2 = crossover(p1, p2)
        c1 = mutate(c1)
        c2 = mutate(c2)
        population = sortedPop[:-2] + [c1, c2]
        numEvals += popSize
        print(fitness(sortedPop[0]))
    print(sortedPop[0])

if __name__ == '__main__':
    main()
