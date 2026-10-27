import numpy as np

def neuron(inputs, weights, bias):
    weighted_sum = np.sum(inputs * weights) + bias
    output = max(0, weighted_sum)
    return weighted_sum, output


inputs = np.array([2, 4])
weights = np.array([-2.0, -1.0])

for bias in [0, 4, 8, 9, 10]:
    weighted_sum, output = neuron(inputs, weights, bias)

    print(f"Bias: {bias}")
    print(f"Weighted sum: {weighted_sum}")
    print(f"Neuron output: {output}")
    print("-" * 20)