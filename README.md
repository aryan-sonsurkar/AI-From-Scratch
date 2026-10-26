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

### Next Steps

* Experiment with how inputs, weights, and bias affect neuron outputs.
* Explore activation functions and their role in neural networks.
* Understand how neural networks learn by adjusting their parameters.
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
    └── day-03-first-neuron/
        └── neuron_from_scratch.py
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
