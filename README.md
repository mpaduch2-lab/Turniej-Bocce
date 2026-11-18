# Selecting team members for a game of Bocce.

**Team:** Z9 · Artificial Intelligence lab, Collegium Da Vinci, 2026/2027 · group L2

## What it does

This system automatically forms balanced tree-player teams based on individual statistics. It's designed for tournament organizers. It ensures fair play and maximizes spectator excitement by minimizing skill differeneces what is hard to achieve manually.

## AI technique

We used genetic algorithm because it quickly finds balanced team combinations out of countles possibilities which brute force algorithm would struggle with. Each candidate solution represents a unique order of players grouped into three-man teams. It minimizes the statistical differences between teams.

## Results

**Metric:** A team-balancing function based on Mean Squared Error (MSE), measuring the deviation of individual team average statistics from the overall tournament player average.

**Baseline:** A baseline method consisting of 1,000 random attempts to divide players into 3-player teams.

#### Experiment Results Table (Average MSE Value):

| Case / Dataset | Baseline (Random) | PyGAD Library | Our Genetic Algorithm |
| :--- | :--- | :--- | :--- |
| **12 players** | 0.06611 | 0.01410 | 0.01475 |
| **24 players** | 0.15129 | 0.05062 | 0.04134 |
| **48 players** | 0.33194 | 0.16160 | 0.10497 |

*Note: The values in the table represent the average MSE calculated from 3 independent datasets (v1, v2, v3).*

Based on the experiment results, our genetic algorithm outperforms other algorithms across 24 and 48 dataset sizes.


## How to run

```
git clone https://github.com/mpaduch2-lab/Turniej-Bocce
cd Turniej-Bocce
pip install -r requirements.txt
python implementation_genetic_algorithm.py
```
Requirements:
- python 3.8 (or newer)
- libraries from requirements.txt

Data Files: 
- CSV files containing player statistics (e.g., 12_gracze_v1.csv, 24_gracze_v1.csv, 48_gracze_v1.csv) must be located in the working directory.

## Team

- Mateusz Paduch: Data generation, Algorithm implementation, Documentation

- Antonina Bentyn: Experiments with different implementations, Results, Documentation

## Documentation

Full documentation in Polish: `dokumentacja.md`.
