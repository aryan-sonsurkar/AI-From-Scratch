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

| Phase      | Focus                                                          |
| ---------- | -------------------------------------------------------------- |
| Week 1     | Python refresh, Git, development setup, and NumPy fundamentals |
| Week 2     | Numerical computing and mathematics for machine learning       |
| Week 3     | Machine learning fundamentals with scikit-learn                |
| Week 4     | Neural networks and gradients from scratch                     |
| Week 5     | PyTorch fundamentals                                           |
| Week 6     | Tokenization and language models                               |
| Week 7     | Attention and transformer architecture                         |
| Week 8     | Building a tiny GPT-style model                                |
| Final days | Testing, documentation, and publishing                         |

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

### Day 4 — Experimenting with Neuron Parameters

* [x] Experiment with different input weights.
* [x] Observe how positive and negative weights affect the weighted sum.
* [x] Investigate how changing the bias shifts the weighted sum.
* [x] Test ReLU with negative, zero, and positive values.
* [x] Implement a reusable neuron function that returns both the weighted sum and final output.
* [x] Run experiments using biases of `0`, `4`, `8`, `9`, and `10`.
* [x] Verify the experimental results.

**Key learning:** A neuron's output depends on its inputs, weights, bias, and activation function. Increasing the bias can shift a negative weighted sum into positive territory.

The neuron does not learn automatically yet. Its weights and bias are manually selected.

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

**Key learning:** A loss function measures the difference between predictions and actual values. MSE averages squared errors, giving larger errors a greater influence on the result.

For the experiment:

* Actual prices: `[30, 30, 30]`
* Predicted prices: `[25, 29, 40]`
* Squared errors: `[25, 1, 100]`
* Mean Squared Error: `(25 + 1 + 100) / 3 = 42.0`

A lower MSE indicates smaller average squared prediction errors when models are evaluated on the same dataset.

Calculating loss alone does not train a model. The next step is to explore how model parameters can be adjusted to reduce loss.

## Next Steps

* Explore how changing model parameters affects prediction errors.
* Understand how a model can adjust its weights and bias to reduce loss.
* Introduce optimization and gradient descent through numerical experiments.
* Build toward implementing forward propagation and backpropagation.

Progress is documented as concepts are practised and experiments are completed.

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
    └── day-05-loss-functions/
        └── loss_function.py
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
