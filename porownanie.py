import numpy as np
import matplotlib.pyplot as plt
import pygad
import glob
import os

# 1. Funkcja obliczająca błąd MSE
def oblicz_mse(permutacja, statystyki):
    n = len(permutacja)
    liczba_druzyn = n // 3
    zreorganizowani = statystyki[permutacja]
    druzyny = zreorganizowani.reshape(liczba_druzyn, 3, 7)
    
    srednia_druzyn = np.mean(druzyny, axis=1)
    mu_j = np.mean(statystyki, axis=0)
    
    mse = np.sum((srednia_druzyn - mu_j) ** 2)
    return mse

# 2. Metoda losowa (1000 prób)
def losowy_podzial(statystyki, ilosc_prob=1000):
    n = len(statystyki)
    wyniki = []
    for _ in range(ilosc_prob):
        perm = np.random.permutation(n)
        wyniki.append(oblicz_mse(perm, statystyki))
    return np.mean(wyniki)

# 3. Metoda PyGAD (szybsza wersja)
def uruchom_pygad(statystyki):
    n = len(statystyki)
    
    def fitness_func(ga_instance, solution, solution_idx):
        score = oblicz_mse(solution.astype(int), statystyki)
        return 1.0 / (1.0 + score)

    ga_instance = pygad.GA(
        num_generations=50,
        num_parents_mating=8,
        fitness_func=fitness_func,
        sol_per_pop=30,
        num_genes=n,
        gene_type=int,
        gene_space=list(range(n)),
        allow_duplicate_genes=False,
        suppress_warnings=True
    )
    
    ga_instance.run()
    solution, solution_fitness, _ = ga_instance.best_solution()
    najlepsze_mse = (1.0 / solution_fitness) - 1.0
    return najlepsze_mse

if __name__ == "__main__":
    sciezka_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    
    szukane_pliki = []
    for n_graczy in [12, 24, 48]:
        for v in [1, 2, 3]:
            wzorzec = os.path.join(sciezka_downloads, "**", f"{n_graczy}_gracze_v{v}.csv")
            dopasowania = glob.glob(wzorzec, recursive=True)
            if dopasowania:
                szukane_pliki.append(dopasowania[0])

    print(f"Znaleziono {len(szukane_pliki)} unikalnych plików projektu!")
    
    wyniki_grupa = {}
    
    for plik in szukane_pliki:
        nazwa_pliku = os.path.basename(plik)
        print(f"\n---> Liczę dla: {nazwa_pliku} <---")
        
        try:
            statystyki = np.loadtxt(plik, delimiter=",", usecols=range(1, 8), dtype=float)
        except Exception as e:
            print(f"Błąd odczytu {nazwa_pliku}: {e}")
            continue
            
        n = len(statystyki)
        
        mse_losowe = losowy_podzial(statystyki, 1000)
        wyniki_pygad = [uruchom_pygad(statystyki) for _ in range(15)]
        mse_pygad = np.mean(wyniki_pygad)
        
        if n not in wyniki_grupa:
            wyniki_grupa[n] = {"los": [], "pygad": []}
            
        wyniki_grupa[n]["los"].append(mse_losowe)
        wyniki_grupa[n]["pygad"].append(mse_pygad)
        
        print(f"   Wynik -> Losowy: {mse_losowe:.5f} | PyGAD: {mse_pygad:.5f}")

    print("\n" + "="*60)
    print("OSTATECZNA TABELA ŚREDNICH WYNIKÓW MSE (DO DOKUMENTACJI):")
    print("="*60)
    print(f"{'Liczba graczy':<15} | {'Punkt odniesienia (Losowy)':<25} | {'Biblioteka PyGAD':<20}")
    print("-" * 60)
    
    for n in sorted(wyniki_grupa.keys()):
        srednia_los = np.mean(wyniki_grupa[n]["los"])
        srednia_pygad = np.mean(wyniki_grupa[n]["pygad"])
        print(f"{n:<15} | {srednia_los:<25.5f} | {srednia_pygad:<20.5f}")
        
        plt.figure(figsize=(6, 4))
        plt.bar(['Losowy', 'PyGAD'], [srednia_los, srednia_pygad], color=['#e74c3c', '#2ecc71'])
        plt.ylabel('Średni błąd MSE (im mniej, tym lepiej)')
        plt.title(f'Porównanie wyników dla n={n} graczy')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        sciezka_wykresu = os.path.join(sciezka_downloads, f'wykres_porownanie_{n}_graczy.png')
        plt.savefig(sciezka_wykresu)
        plt.close()

    print("\nGotowe! Zapisano wykresy w Pobranych.")
