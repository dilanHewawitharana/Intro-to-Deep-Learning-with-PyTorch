import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    ce = 0
    for index in range(len(Y)):
        if Y[index] == 1:
            ce += -np.log(P[index])
        elif Y[index] == 0:
            ce += -np.log(1-P[index])
    
    return ce
