import random
import numpy as np

data = np.genfromtxt("12_gracze_v1.csv", delimiter=",", dtype=np.str_)

PLAYER_NAMES = data[:, 0].copy()
STATISTICS = data[:, 1:].astype(np.float64).copy()

NUM_PLAYERS = len(PLAYER_NAMES)
TEAM_AMOUNT = NUM_PLAYERS // 3
STATISTICS_AMOUNT = STATISTICS.shape[1]

WEIGHTS = np.ones(STATISTICS_AMOUNT)

POPULATION_SIZE = 40
GENERATIONS = 100
MUTATION_RATE = 0.15

def calculate_fitness(chromosome):
    """
    Chromosom to ciąg liczb w którym co trzy osoby zaczyna się kolejna drużyna. </br>
    | 1 2 3| 4 5 6| 7 8 9| ... </br>
    |team 1|team 2|team 3| ... </br>
    Fitness: Oceniamy zbalansowanie drużyn. Im mniejsza różnica punktowa, tym wyższy fitness.
    """
    if len(set(chromosome)) != NUM_PLAYERS:
        return float("inf")  # Silna kara za zaistnienie powtórek w drużynach.

    fitness = 0
    for j in range(STATISTICS_AMOUNT):
        mu = np.mean(STATISTICS[:, j])
        w = WEIGHTS[j]

        for i in range(TEAM_AMOUNT):
            p1, p2, p3 = chromosome[3*i:3*i+3]
            avg = (STATISTICS[p1-1, j] + STATISTICS[p2-1, j] + STATISTICS[p3-1, j]) / 3

            fitness += w * (avg - mu)**2

    return fitness


def create_individual():
    """Tworzy osobnik z ciągiem liczb od 1 do NUM_PLAYERS."""
    chromosome = list(range(1, NUM_PLAYERS+1))
    random.shuffle(chromosome)
    return chromosome


def crossover(parent1, parent2):
    """
    Krzyżowanie jednopunktowe z naprawą powtórek.
    p1: 1234 5678
    p2: 4567 8910
           ) (
    c1: 1234 8910
    c2: 4567 5678
    """
    point = random.randint(1, NUM_PLAYERS - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    # Znajdowanie powtórek
    count = np.bincount(child1, minlength=NUM_PLAYERS)
    # Pominięcie zera
    missing = np.nonzero(count < 1)[1:] 
    
    # Naprawa osobników, gdyby wystąpiła powtórka
    for value in missing:
        count = np.bincount(child1, minlength=NUM_PLAYERS)
        duplicates = np.nonzero(count > 1)
        child1[duplicates[0]] = value

    
    count = np.bincount(child2, minlength=NUM_PLAYERS)
    # Pominięcie zera
    missing = np.nonzero(count < 1)[1:] 
    
    # Naprawa osobników, gdyby wystąpiła powtórka
    for value in missing:
        count = np.bincount(child2, minlength=NUM_PLAYERS)
        duplicates = np.nonzero(count > 1)
        child2[duplicates[0]] = value

    return child1, child2


def mutate(chromosome):
    """Mutacja typu Swap: zamienia miejscami dwóch graczy."""
    if random.random() < MUTATION_RATE:
        idx_a, idx_b = np.random.choice(list(range(NUM_PLAYERS)), size=2, replace=False)
        chromosome[idx_a], chromosome[idx_b] = chromosome[idx_b], chromosome[idx_a]
    return chromosome


def run_genetic_algorithm(path: str):
    # 1. Konfiguracja problemu i parametrów GA
    data = np.genfromtxt(path, delimiter=",", dtype=np.str_)

    PLAYER_NAMES = data[:, 0].copy()
    STATISTICS = data[:, 1:].astype(np.float64).copy()

    NUM_PLAYERS = len(PLAYER_NAMES)
    TEAM_AMOUNT = NUM_PLAYERS // 3
    STATISTICS_AMOUNT = STATISTICS.shape[1]

    # Inicjalizacja populacji
    population = [create_individual() for _ in range(POPULATION_SIZE)]

    best_solution = None
    best_fitness = float("inf")

    for generation in range(GENERATIONS):
        # Tworzenie nowej populacji
        new_population = population.copy()
        new_population.sort(key=lambda x: calculate_fitness(x))

        for i in range(0, POPULATION_SIZE, 2):
            p1 = new_population[i]
            p2 = new_population[i+1]
            child1, child2 = crossover(p1, p2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.append(child1)
            new_population.append(child2)

        # Selekcja elitarna
        new_population.sort(key=lambda x: calculate_fitness(x))
        population = new_population[:POPULATION_SIZE]

        # Śledzenie najlepszego wyniku
        min_fit = calculate_fitness(population[0])
        if min_fit < best_fitness:
            best_fitness = min_fit
            best_solution = population[0]

    return best_solution, best_fitness


# 2. Uruchomienie i prezentacja wyników
if __name__ == "__main__":
    for players in [12, 24, 48]:
        fitnesses = []
        for version in [1, 2, 3]:
            for iteration in range(30):
                best_chrom, fitness = run_genetic_algorithm(f"{players}_gracze_v{version}.csv")
                # print("=== Wynik Optymalizacji Turnieju Bocce ===")
                # for team in range(TEAM_AMOUNT):
                #     print(50*"=-")
                #     print(f"Drużyna {team + 1}:")
                #     p1, p2, p3 = best_chrom[3*team], best_chrom[3*team + 1], best_chrom[3*team + 2]
                #     print(f" - {PLAYER_NAMES[p1 - 1]} -> {STATISTICS[p1 - 1]}")
                #     print(f" - {PLAYER_NAMES[p2 - 1]} -> {STATISTICS[p2 - 1]}")
                #     print(f" - {PLAYER_NAMES[p3 - 1]} -> {STATISTICS[p3 - 1]}")
                #     print(f"Average team statistics: {np.mean(STATISTICS[[p1 - 1, p2 - 1, p3 - 1]], axis=0)}")
    
                
                # print(f"Najlepszy osobnik: {best_chrom}")
                # print(f"O wartości przystosowania: {fitness}")
                fitnesses.append(fitness)
        print(f"Players {players} average fitness: {np.mean(fitnesses)}")