import numpy as np
import math
# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    ce = 0
    for i in range(len(Y)):
        if Y[i]:
            ce += math.log(P[i])
        else:
            ce += math.log(1-P[i])
    ce *= -1
    return ce