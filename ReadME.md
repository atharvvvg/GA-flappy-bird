# Flappy Bird AI using Genetic Algorithm

![Flappy Bird AI Demo](media/flappy_genalg.mp4)

An artificial intelligence implementation that learns to play Flappy Bird using neuroevolution and genetic algorithms. The AI agents improve through generations by evolving their neural network brains.

## Features

- Neural network decision system for bird control
- Genetic algorithm for population evolution
- Species formation and speciation mechanism
- Fitness-based natural selection
- Weight mutation and crossover operations
- Visualized game mechanics with Pygame
- Real-time generational statistics

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/flappy-bird-ai.git
   cd flappy-bird-ai
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the game:
   ```bash
   python main.py
   ```

## Usage

- The game starts automatically with the first generation of birds.
- Watch as AI agents learn to navigate through pipes.
- Each generation improves based on previous performance.
- The score represents how many pipes the current generation has passed.
- Different colors represent different species.

## Theory & Implementation

### Genetic Algorithm Flow

1. **Population Initialization**: Random neural networks for the initial generation.
2. **Fitness Evaluation**: Lifespan-based fitness calculation.
3. **Selection**:
   - Species formation based on neural network similarity.
   - Fitness-proportionate selection.
4. **Crossover**: Breeding between successful individuals.
5. **Mutation**:
   - Weight perturbation (Gaussian noise).
   - Occasional random weight replacement.
6. **Speciation**:
   - Dynamic species threshold (δ = 1.2).
   - Staleness counter for species improvement.

### Neural Network Architecture

- **Inputs (3 nodes)**:
  - Vertical distance to the top pipe.
  - Horizontal distance to the next pipe.
  - Vertical distance to the bottom pipe.
- **Hidden Layers**: Single hidden layer (evolvable).
- **Output (1 node)**: Flap decision (Sigmoid activation > 0.73).

### Mathematical Concepts

#### Activation Function:

```python
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))
```

#### Fitness Calculation:

```python
fitness = lifespan
```

#### Species Similarity:

```python
similarity = sum(abs(w1_i - w2_i) for w1_i, w2_i in zip(weights1, weights2))
```

#### Mutation:

- **80% chance for weight perturbation:**

```python
new_weight = weight + random.gauss(0, 0.1)
```

- **10% chance for random weight replacement:**

```python
new_weight = random.uniform(-1, 1)
```

---
