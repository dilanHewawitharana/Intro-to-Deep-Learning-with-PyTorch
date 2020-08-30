import numpy as np
import math

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    exp_list = [math.exp(i) for i in L]
    sum_of_exp = sum(exp_list)
    
    return ([i/sum_of_exp for i in exp_list])
    