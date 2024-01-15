# 100_Prisoners_Problem

## Problem:

 - 100 prisoners are assigned unique numbers from 1 to 100.
 - Each prisoner is given 50 opportunities to open drawers.
 - Each drawer contains a number from 1 to 100, chosen randomly.
 - If a prisoner opens a drawer with their number, they are free to go. Otherwise, they are executed.

## Goal:

 - Find a strategy that maximizes the probability of all 100 prisoners being freed.

## Optimal Strategy:

 - Each prisoner opens their assigned drawer, and then follows the sequence of numbers in that drawer. 
 - This creates a loop, and if all prisoners follow the loop, they will all be freed.

## Experiment:

 - Conduct n experiments, where each experiment consists of:
        - Assigning unique numbers from 1 to 100 to the 100 prisoners.
        - Randomly selecting numbers from 1 to 100 for the drawers.
        - Each prisoner opening drawers until they find their number or they run out of opportunities.
 - Calculate the probability of all 100 prisoners being successful in each experiment.
 - The overall probability of success is the average of the probabilities of success from the n experiments.
