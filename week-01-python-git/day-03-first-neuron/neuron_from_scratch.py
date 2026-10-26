import numpy as np

def neuron(inputs, weights, bias):
    weighted_sum = np.sum(inputs * weights) + bias

    output = max(0, weighted_sum)

    return output


inputs = np.array([4, 2, 5])
weights = np.array([0.1, 0.5, 0.2])
bias = -1.0

print(neuron(inputs, weights, bias))