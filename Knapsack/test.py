#!/usr/bin/python

# Knapsack algorithm
import numpy as np
# This file describes a knapsack instance, and it has the following format:
#
# [knapsack_size][number_of_items]
# [value_1] [weight_1]
# [value_2] [weight_2]
#
# For example, the third line of the file is "50074 659", indicating that the second item has 
# value 50074 and size 659, respectively.
#
# You can assume that all numbers are positive. You should assume that item weights and the 
# knapsack capacity are integers.

# Get the value of the optimal solution.

# load contents of text file into a list numList
NUMLIST_FILENAME = "data/knapsack-1.txt" # optimal value: 2493893
# NUMLIST_FILENAME = "data/tests/knapsack-1.1.txt" # optimal value: 8
NUMLIST_FILENAME = "data/tests/knapsack-1.2.txt" # optimal value: 51
NUMLIST_FILENAME = "./test cases/input_random_6_10_10.txt" # optimal value: 141

inFile = open(NUMLIST_FILENAME, 'r')

knapsack_size = 0
number_of_items = False
items = []



for f in inFile:
    if(number_of_items == False):
        knapsack_size, number_of_items = map(int, f.split())
    else:
        value, weight = map(int, f.split())
        items.append([value, weight])

# initializing 
A = { 0:{} } 
for x in range(0, knapsack_size + 1):
    A[0][x] = 0

A = np.zeros(shape = (number_of_items + 1, knapsack_size + 1))

for i in range(1, number_of_items + 1):
    for x in range(0, knapsack_size + 1):
        option_a = A[i-1,x]
        value = items[i-1][0]
        weight = items[i-1][1]
        if x - weight >= 0 and x - weight <= knapsack_size:
            option_b = A[i-1,x-weight] + value
        else:
            option_b = 0
        if option_a >= option_b:
            A[i,x] = option_a
        else:
            A[i,x] = option_b

# optimal value
print ('Optimal Value: ' + str(A[number_of_items][knapsack_size]))
print (A.T)