# AI From Scratch — Progress Log

## Day 1 — 24 October 2026

### Completed

* Verified Python 3.11.9, Git 2.53.0, and pip.
* Created a Python virtual environment.
* Installed NumPy.
* Created the GitHub repository and pushed the initial project.
* Learned array creation, shape, indexing, addition, and multiplication.
* Practised element-wise operations and exponentiation.
* Created the first NumPy experiment.

### Key Learnings

* NumPy arrays store numerical data and support efficient element-wise operations.
* `shape` describes an array's dimensions and sizes.
* Array indexing provides access to individual elements.

## Day 2 — 25 October 2026

### Completed

* Practised 1D, 2D, and 3D arrays.
* Learned `ndim` and `shape`.
* Practised row and column indexing.
* Used `reshape()` to change array dimensions.
* Compared element-wise addition and multiplication.
* Learned the difference between element-wise multiplication (`*`) and matrix multiplication (`@`).
* Calculated weighted sums using NumPy.

### Key Learnings

* `ndim` returns the number of dimensions.
* `shape` returns the size of each dimension.
* Element-wise multiplication and matrix multiplication perform different calculations.
* Weighted sums combine inputs with their corresponding weights.

## Day 3 — 26 October 2026

### Completed

* Reviewed the weighted-sum calculation used by an artificial neuron.
* Introduced bias as an additional parameter.
* Learned the ReLU activation function.
* Implemented a reusable neuron function using Python and NumPy.
* Tested the neuron with positive and negative weighted sums.
* Verified that ReLU returns zero for negative inputs and preserves positive inputs.

### Key Learnings

An artificial neuron can calculate its weighted sum and bias using:

`z = sum(inputs * weights) + bias`

The ReLU activation function is:

`ReLU(z) = max(0, z)`

The neuron's output is calculated by applying ReLU to the weighted sum.

The implementation performs a forward calculation. It does not yet train or learn weights automatically.

## Day 4 — 27 October 2026

**Topic:** Experimenting with Artificial Neurons

### Completed

* Experimented with different weights and biases.
* Observed how weights affect the weighted sum.
* Studied how bias shifts the weighted sum.
* Tested ReLU with negative, zero, and positive values.
* Created a reusable neuron function returning both the weighted sum and output.
* Tested biases 0, 4, 8, 9, and 10.

### Key Learning

The neuron calculates a weighted sum, adds bias, and applies ReLU. Increasing the bias can change the output from zero to a positive value.

The neuron is not learning automatically yet; its weights and bias are still manually selected.

## Next Steps

* Experiment with different inputs, weights, and bias values.
* Investigate how each parameter changes the neuron's output.
* Explore additional activation functions.
* Progress toward understanding how neural networks learn.

This log records completed work and the concepts learned during the 60-day AI journey.