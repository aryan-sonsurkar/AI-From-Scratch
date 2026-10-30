# AI From Scratch

**Learning AI by building it, not just using it.**

This repository documents my 60-day journey into Artificial Intelligence and Machine Learning, starting with numerical computing and progressing toward building a tiny GPT-style language model.

My goal is to understand how AI works under the hood by implementing concepts, running experiments, and documenting what I learn.

## Goals

* Strengthen Python and numerical computing fundamentals.
* Learn NumPy and the mathematics behind machine learning.
* Implement basic machine learning algorithms.
* Understand neural networks, forward propagation, and backpropagation.
* Learn PyTorch fundamentals.
* Explore tokenization, attention, and transformer architecture.
* Build a small GPT-style language model for educational purposes.
* Share my progress and code through open source.

## Roadmap

| Phase      | Focus                                                                                       |
| ---------- | ------------------------------------------------------------------------------------------- |
| Week 1     | Python refresh, Git, development setup, NumPy, neurons, loss, and introductory optimization |
| Week 2     | Numerical computing and mathematics for machine learning                                    |
| Week 3     | Machine learning fundamentals with scikit-learn                                             |
| Week 4     | Neural networks and gradients from scratch                                                  |
| Week 5     | PyTorch fundamentals                                                                        |
| Week 6     | Tokenization and language models                                                            |
| Week 7     | Attention and transformer architecture                                                      |
| Week 8     | Building a tiny GPT-style model                                                             |
| Final days | Testing, documentation, and publishing                                                      |

This is a learning roadmap, so the schedule may change as I work through the concepts.

## Tech Stack

* Python 3.11
* NumPy
* Git and GitHub
* scikit-learn
* PyTorch

Additional libraries will be introduced as needed.

## Progress

### Day 1 — Environment Setup and NumPy Basics

* [x] Verify Python, Git, and pip.
* [x] Create a Python virtual environment.
* [x] Install NumPy.
* [x] Create the project repository and push the initial work to GitHub.
* [x] Practice array creation, indexing, and shape.
* [x] Explore element-wise addition, multiplication, and exponentiation.
* [x] Create the first NumPy experiment.

### Day 2 — NumPy Dimensions, Reshaping, and Matrix Operations

* [x] Explore 1D, 2D, and 3D arrays.
* [x] Understand `ndim` and `shape`.
* [x] Practise accessing elements using row and column indexing.
* [x] Reshape arrays using `reshape()`.
* [x] Compare element-wise addition and multiplication.
* [x] Understand the difference between element-wise multiplication (`*`) and matrix multiplication (`@`).
* [x] Calculate weighted sums using NumPy.
* [x] Practise the relationship between array operations and neural network calculations.

### Day 3 — Building an Artificial Neuron from Scratch

* [x] Understand inputs, weights, and weighted sums.
* [x] Introduce bias into the neuron's calculation.
* [x] Learn the ReLU activation function.
* [x] Implement a reusable neuron function using Python and NumPy.
* [x] Test the neuron with positive and negative weighted sums.
* [x] Understand how ReLU transforms negative results into zero.

**Key learning:** A neuron combines inputs and weights, adds a bias, and applies an activation function. This first implementation performs a forward calculation; its parameters are manually selected.

### Day 4 — Experimenting with Neuron Parameters

* [x] Experiment with different input weights.
* [x] Observe how positive and negative weights affect the weighted sum.
* [x] Investigate how changing the bias shifts the weighted sum.
* [x] Test ReLU with negative, zero, and positive values.
* [x] Implement a reusable neuron function that returns both the weighted sum and final output.
* [x] Run experiments using biases of `0`, `4`, `8`, `9`, and `10`.
* [x] Verify the experimental results.

**Key learning:** A neuron's output depends on its inputs, weights, bias, and activation function. The neuron does not learn automatically yet; its weights and bias are manually selected.

### Day 5 — Loss Functions and Mean Squared Error

* [x] Understand prediction errors using predicted and actual values.
* [x] Calculate squared error.
* [x] Understand why squaring removes the sign of an error.
* [x] Learn Mean Squared Error (MSE).
* [x] Calculate MSE manually for multiple predictions.
* [x] Compare prediction errors using MSE.
* [x] Implement a reusable `squared_error()` function.
* [x] Implement a reusable `mean_squared_error()` function.
* [x] Test the loss functions using sample house-price predictions.

**Experiment**

* Actual values: `[30, 30, 30]`
* Predicted values: `[25, 29, 40]`
* Squared errors: `[25, 1, 100]`
* MSE: `(25 + 1 + 100) / 3 = 42.0`

**Key learning:** A loss function measures the difference between predictions and actual values. MSE averages squared errors, giving larger errors a greater influence on the result. Calculating loss alone does not train a model; parameters must be adjusted to reduce it.

### Day 6 — Gradient Descent: Training a Simple Model

* [x] Review predictions and squared error.
* [x] Experiment with how changing a weight affects prediction and loss.
* [x] Compare weights to see which produces lower loss.
* [x] Learn how the gradient indicates how loss changes as a parameter changes.
* [x] Use a learning rate to control the size of weight updates.
* [x] Implement a gradient-based weight update in Python.
* [x] Repeat weight updates over 100 iterations.
* [x] Compare learning rates `0.01` and `0.1`.

**Experiment setup**

* Input: `x = 3`
* Target: `y = 10`
* Initial weight: `w = 2`
* Bias: `b = 0`
* Initial prediction: `6`
* Initial squared loss: `16`

**Results after 100 iterations**

| Learning rate | Final weight (approx.) | Final prediction (approx.) | Final loss (approx.) |
| ------------- | ---------------------: | -------------------------: | -------------------: |
| `0.01`        |           `3.33333333` |                       `10` |           `9.27e-17` |
| `0.1`         |           `3.33333333` |                       `10` |           `6.64e-19` |

**Key learning:** For `prediction = w * x + b`, squared loss is `(y - prediction) ** 2`. The weight gradient is `-2 * x * (y - prediction)`, and the update rule is `w = w - learning_rate * dw`.

Repeating the update reduced the loss and brought the prediction close to the target. A larger learning rate is not automatically unstable; its effect depends on the model and data. In this experiment, the weight was updated while the bias remained fixed at zero.

### Day 7 — Gradient Descent with Both Weight and Bias

* [x] Use the linear model `prediction = w * x + b`.
* [x] Calculate prediction error and squared loss.
* [x] Calculate the gradient with respect to weight (`dw`).
* [x] Calculate the gradient with respect to bias (`db`).
* [x] Update both weight and bias during gradient descent.
* [x] Train the model for 100 iterations.
* [x] Check the final prediction and loss.

**Experiment setup**

* Input: `x = 3`
* Target: `y = 13`
* Initial weight: `w = 2.0`
* Initial bias: `b = 0.0`
* Learning rate: `0.01`
* Iterations: `100`

**Results after 100 iterations**

| Parameter    |    Final result |
| ------------ | --------------: |
| Weight (`w`) |  `3.9199999992` |
| Bias (`b`)   |  `1.2399999997` |
| Prediction   | `12.9999999968` |
| Loss         |      `9.97e-18` |

**Key learning:** The gradients are `dw = -2 * x * (y - prediction)` and `db = -2 * (y - prediction)`. The parameters are updated with `w = w - learning_rate * dw` and `b = b - learning_rate * db`.

Updating the bias lets the model adjust the prediction independently of the input's weighted contribution. In this experiment, the model fitted one training example closely. One example is not enough to establish generalization, and multiple weight/bias combinations can fit the same single example.

## Next Steps

* [ ] Train using multiple examples and examine how they affect loss.
* [ ] Explore optimization techniques for reducing loss.
* [ ] Build toward implementing forward propagation and backpropagation.
* [ ] Progress toward understanding how neural networks learn automatically.

## Repository Structure

```text
AI-From-Scratch/
├── README.md
├── progress.md
├── requirements.txt
├── .gitignore
└── week-01-python-git/
    ├── day-01-setup/
    │   └── numpy_first_steps.py
    ├── day-02-numpy/
    │   └── numpy_dimensions.py
    ├── day-03-first-neuron/
    │   └── neuron_from_scratch.py
    ├── day-04-neuron-experiments/
    │   └── neuron_experiments.py
    ├── day-05-loss-functions/
    │   └── loss_function.py
    ├── day-06-gradient-descent/
    │   └── gradient_descent.py
    └── day-07-training-bias/
        └── training_bias.py
```

The structure will evolve as new topics, experiments, and projects are added.

## Learning Philosophy

1. Understand the concept before relying on a library.
2. Write code and experiment with it.
3. Learn from errors instead of blindly copying fixes.
4. Document progress honestly.
5. Build small projects that demonstrate what I understand.

## Important Note

This repository is an educational project. Implementations are intended to develop my understanding of AI and Machine Learning, not to compete with production-scale models.

## Follow the Journey

This repository is my public learning log. The objective is to build a strong foundation in AI, contribute to open source, and gradually work toward developing AI systems of my own.