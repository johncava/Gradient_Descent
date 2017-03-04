from __future__ import division
import numpy as np

def derivative(x):
    return 2*x

def gradient(x, learning_rate, max_iterations):
    for iterations in xrange(max_iterations):
        g = derivative(x)
        x = x - learning_rate*g
        if (iterations % 10 == 0):
            print x

a = np.array([[1000,2500,1050],[2600,1502,200]])
gradient(a, 0.1, 100)