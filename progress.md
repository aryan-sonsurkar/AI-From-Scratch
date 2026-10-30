# AI From Scratch — Progress Log

## Day 1 — 24 October 2026

### Completed

* [x] Verified Python 3.11.9, Git 2.53.0, and pip.
* [x] Created a Python virtual environment.
* [x] Installed NumPy.
* [x] Created the GitHub repository and pushed the initial project.
* [x] Learned array creation, shape, indexing, addition, and multiplication.
* [x] Practised element-wise operations and exponentiation.
* [x] Created the first NumPy experiment.

### Key Learnings

* NumPy arrays store numerical data and support efficient element-wise operations.
* `shape` describes an array's dimensions and sizes.
* Array indexing provides access to individual elements.

## Day 2 — 25 October 2026

### Completed

* [x] Practised 1D, 2D, and 3D arrays.
* [x] Learned `ndim` and `shape`.
* [x] Practised row and column indexing.
* [x] Used `reshape()` to change array dimensions.
* [x] Compared element-wise addition and multiplication.
* [x] Learned the difference between element-wise multiplication (`*`) and matrix multiplication (`@`).
* [x] Calculated weighted sums using NumPy.

### Key Learnings

* `ndim` returns the number of dimensions.
* `shape` returns the size of each dimension.
* Element-wise multiplication and matrix multiplication perform different calculations.
* Weighted sums combine inputs with their corresponding weights.

## Day 3 — 26 October 2026

### Completed

* [x] Reviewed the weighted-sum calculation used by an artificial neuron.
* [x] Introduced bias as an additional parameter.
* [x] Learned the ReLU activation function.
* [x] Implemented a reusable neuron function using Python and NumPy.
* [x] Tested the neuron with positive and negative weighted sums.
* [x] Verified that ReLU returns zero for negative inputs and preserves positive inputs.

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

* [x] Experimented with different weights and biases.
* [x] Observed how weights affect the weighted sum.
* [x] Studied how bias shifts the weighted sum.
* [x] Tested ReLU with negative, zero, and positive values.
* [x] Created a reusable neuron function returning both the weighted sum and output.
* [x] Tested biases `0`, `4`, `8`, `9`, and `10`.

### Key Learning

The neuron calculates a weighted sum, adds bias, and applies ReLU. Increasing the bias can change the output from zero to a positive value.

The neuron is not learning automatically yet; its weights and bias are still manually selected.

## Day 5 — 28 October 2026

**Focus:** Loss Functions and Model Evaluation

### Completed

* [x] Understood prediction errors.
* [x] Learned squared error.
* [x] Understood Mean Squared Error (MSE).
* [x] Calculated squared errors manually.
* [x] Compared prediction errors using MSE.
* [x] Implemented `squared_error()` in Python.
* [x] Implemented `mean_squared_error()` in Python.
* [x] Tested the implementation with sample price predictions.

### Experiment Results

Actual values: `[30, 30, 30]`

Predicted values: `[25, 29, 40]`

Squared errors: `[25, 1, 100]`

MSE calculation:

`MSE = (25 + 1 + 100) / 3 = 42.0`

### What I Learned

A loss function measures how far predictions are from actual values.

Squared error is calculated as:

`Squared Error = (predicted - actual) ** 2`

Mean Squared Error calculates the average of the squared errors. Squaring makes errors non-negative and gives larger errors a greater influence on the final result.

When evaluating models on the same dataset, a lower MSE indicates smaller average squared prediction errors.

Calculating loss does not automatically train a model. The model's parameters must be adjusted through an optimization process to reduce that loss.

### What I Built

`week-01-python-git/day-05-loss-functions/loss_function.py`

Implemented:

* `squared_error(predicted, actual)`
* `mean_squared_error(predictions, actuals)`

### Time Spent

Update with actual time.

### Blockers

None reported.

### Next Step

Explore how model parameters can be adjusted to reduce loss, introducing optimization and gradient descent.

**Status:** Complete.

## Day 6 — 29 October 2026

**Focus:** Gradient Descent and Training a Simple Model

### Completed

* [x] Reviewed predictions and squared error.
* [x] Experimented with how changing a weight affects prediction and loss.
* [x] Compared different weights to identify which produced lower loss.
* [x] Learned that the gradient indicates how loss changes as a parameter changes.
* [x] Used a learning rate to control the size of weight updates.
* [x] Implemented a gradient-based weight update in Python.
* [x] Repeated the update over 100 iterations.
* [x] Compared training with learning rates `0.01` and `0.1`.

### Experiment Setup

* Input (`x`): `3`
* Target (`y`): `10`
* Initial weight (`w`): `2`
* Bias (`b`): `0`
* Initial prediction: `6`
* Initial squared error: `16`

### Training Results

With a learning rate of `0.01` over 100 iterations:

* Final weight: approximately `3.33333333`
* Final prediction: approximately `10`
* Final loss: approximately `9.27e-17`

With a learning rate of `0.1` over 100 iterations:

* Final weight: approximately `3.33333333`
* Final prediction: approximately `10`
* Final loss: approximately `6.64e-19`

### What I Learned

For the simple model:

`prediction = w * x + b`

The squared loss is:

`loss = (y - prediction) ** 2`

For this model, the gradient of the loss with respect to the weight is:

`dw = -2 * x * (y - prediction)`

The weight is updated using:

`w = w - learning_rate * dw`

Repeating this update reduced the loss and brought the prediction close to the target. The learning rate controls the size of each update; a larger learning rate is not automatically unstable and its effect depends on the model and data.

This experiment updated the weight while keeping the bias fixed at zero.

### What I Built

`week-01-python-git/day-06-gradient-descent/gradient_descent.py`

The script calculates a prediction and loss, updates the weight repeatedly, and prints the final weight, prediction, and loss.

### Time Spent

Update with actual time.

### Blockers

None reported.

**Status:** Complete.

## Day 7 — 30 October 2026

**Focus:** Gradient Descent with Both Weight and Bias

### Completed

* [x] Used the linear model `prediction = w * x + b`.
* [x] Calculated prediction error and squared loss.
* [x] Calculated the gradient with respect to weight (`dw`).
* [x] Calculated the gradient with respect to bias (`db`).
* [x] Updated both weight and bias during gradient descent.
* [x] Trained the model for 100 iterations.
* [x] Checked the final prediction and loss.

### Experiment Setup

* Input (`x`): `3`
* Target (`y`): `13`
* Initial weight (`w`): `2.0`
* Initial bias (`b`): `0.0`
* Learning rate: `0.01`
* Iterations: `100`

### Training Results

* Final weight: approximately `3.9199999992`
* Final bias: approximately `1.2399999997`
* Final prediction: approximately `12.9999999968`
* Final loss: approximately `9.97e-18`

### What I Learned

The model calculates a prediction using:

`prediction = w * x + b`

The squared loss is:

`loss = (y - prediction) ** 2`

The gradients used in this experiment are:

`dw = -2 * x * (y - prediction)`

`db = -2 * (y - prediction)`

Both parameters are updated using gradient descent:

`w = w - learning_rate * dw`

`b = b - learning_rate * db`

Updating the bias allows the model to adjust the prediction independently of the input's weighted contribution.

In this experiment, the model fitted the single training example closely. One example is not enough to establish whether the model generalizes to unseen data, and different weight/bias combinations can fit the same single example.

### What I Built

`week-01-python-git/day-07-training-bias/training_bias.py`

The script trains a simple linear model by updating both weight and bias over repeated iterations.

### Time Spent

Update with actual time.

### Blockers

None reported.

**Status:** Complete.

## Next Steps

* [ ] Train using multiple examples and examine how they affect loss.
* [ ] Explore optimization techniques for reducing loss.
* [ ] Progress toward implementing forward propagation and backpropagation.
* [ ] Continue toward understanding how neural networks learn automatically.

This log records completed work and the concepts learned during the 60-day AI journey.