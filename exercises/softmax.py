import numpy as np
import math
# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    leny = len(L)
    summed_exps = sum([math.exp(j) for j in range(leny)])
    for i in range(leny):
        L[i] = math.exp(i)/summed_exps
    return L