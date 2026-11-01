import numpy as np

# składanie przykładowych imion
imiona = ["Mateusz", "Paweł", "Dominik", "Karol", "Marcin", "Marzena", "Amelia", "Wiktoria"]
nazwiska = ["Paduch", "Piotrowski/a", "Wierzejewski/a", "Lis", "Ulatowski/a", "Słupkowski/a"]

k1 = []

for imie in imiona:
    for nazwisko in nazwiska:
        k1.append(f"{imie} {nazwisko}")

# parametry rozkładu
mean = 0.5 # średnia
var = 0.1 # wariancja

for ilosc in [12, 24, 48]:
    for seed in [1, 2, 3]:
        rng = np.random.default_rng(seed)

        statystyki = np.clip( # ograniczamy dane do przedziału
                np.round(rng.normal(mean, var, (ilosc, 7)), 5) # losujemy dane o rozkłądzie normalnym i zaokrąglamy wyniki  
                , 0  # minimum
                , 1) # maximum

        dane = np.hstack((np.array(k1)[:ilosc, None], statystyki))

        np.savetxt(f"{ilosc}_gracze_v{seed}.csv", dane, "%s", delimiter=", ")