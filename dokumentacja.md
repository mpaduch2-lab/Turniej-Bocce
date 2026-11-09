# Turniej Bocce

**Zespół:** Z9 · grupa L2 · **Repozytorium:** "https://github.com/mpaduch2-lab/Turniej-Bocce"
Sztuczna inteligencja — laboratorium · Collegium Da Vinci · rok akad. 2026/2027

## 1. Problem *(rubryka A)*

> Co tu wpisać: kto ma problem, w jakiej sytuacji, co system dla niego robi. Co wchodzi do systemu, co z niego wychodzi. 3–6 zdań, rozwinięcie pkt 4 karty tematu.

## 2. Dlaczego SI i dlaczego ta technika *(B · 7 pkt)*

> Co tu wpisać: dlaczego zwykły algorytm nie wystarcza (nie umiemy zapisać reguły / przepis jest za drogi / reguł jest za dużo). Dlaczego wybraliście tę technikę z modułu, a nie inną — jedno zdanie o tym, co by się stało przy alternatywie.

## 3. Dane *(B · 8 pkt)*

Dane generowane są przy pomocy skrytpu generator.py. Generuje on po 3 niezależne zestawy danych (seed 1, 2, 3) w różnych wielkościach (12, 24, i 48 wierszy). Dane składają się z ośmiu kolumn - jednej teksotwej (przykładowe Imię i nazwisko) oraz 7 liczbowych (Celność, Panowanie nad stresem, Poziom koncentracji, Siła rzutu, Skuteczność rzutów, Dostosowywanie się do terenu, Umiejętność czytania gry) które są znormalizowane (z przedziału $[0, 1]$) i generowane na podstawie rozkładu normalnego $\mathcal{N}(0.5, 0.1)$.

## 4. Rozwiązanie *(A · 10 pkt, B · 5 pkt)*

### 1. Schemat działania systemu

System służy do automatycznego podziału graczy w Bocce na trzyosobowe drużyny w taki sposób, aby poziom umiejętności poszczególnych zespołów był jak najbardziej wyrównany. Do rozwiązania problemu wykorzystaliśmy algorytm genetyczny, który przeszukuje możliwe kombinacje podziału zawodników i wybiera te, które zapewniają najlepsze zbalansowanie drużyn.

Działanie systemu przebiega w następujących krokach:

1. **Wczytanie danych** – system odczytuje z pliku CSV listę zawodników oraz przypisane im statystyki.
2. **Inicjalizacja populacji** – generowana jest początkowa populacja składająca się z 40 losowych osobników. Każdy osobnik reprezentuje jeden możliwy podział zawodników na drużyny.
3. **Ocena przystosowania** – dla każdego osobnika obliczana jest wartość funkcji przystosowania (fitness), która określa, jak bardzo drużyny różnią się poziomem od ogólnej średniej wszystkich zawodników.
4. **Selekcja rodziców** – osobniki o najlepszych wartościach funkcji przystosowania są wybierane do dalszego rozmnażania.
5. **Krzyżowanie** – wybrani rodzice łączeni są za pomocą krzyżowania jednopunktowego. Następnie usuwane są ewentualne powtórzenia zawodników.
6. **Mutacja** – z prawdopodobieństwem 15% następuje zamiana miejscami dwóch losowo wybranych zawodników w chromosomie.
7. **Selekcja nowej populacji** – spośród dotychczasowych osobników oraz nowo utworzonych potomków wybierane są najlepsze rozwiązania, które tworzą kolejną populację.
8. **Powtarzanie procesu** – kroki od 3 do 7 wykonywane są przez 100 pokoleń.
9. **Zwrócenie wyniku** – system zwraca najlepszy znaleziony podział zawodników na drużyny oraz wartość jego funkcji przystosowania.

### 2. Opis algorytmu SI i podstawa matematyczna

W projekcie zastosowaliśmy algorytm genetyczny. Algorytm wykorzystuje mechanizmy selekcji naturalnej, krzyżowania oraz mutacji, aby stopniowo poprawiać jakość uzyskiwanych rozwiązań.

W naszym problemie pojedynczy osobnik reprezentuje jeden możliwy podział wszystkich zawodników na trzyosobowe drużyny. Chromosom ma postać permutacji numerów zawodników, np.:

`[3, 7, 1 | 5, 2, 8 | 4, 6, 9]`

Oznacza to, że:
- pierwsza drużyna składa się z graczy 3, 7 i 1,
- druga drużyna składa się z graczy 5, 2 i 8,
- trzecia drużyna składa się z graczy 4, 6 i 9.

Każdy zawodnik występuje dokładnie raz, dzięki czemu nie dochodzi do przypisania tej samej osoby do kilku drużyn.

#### Funkcja przystosowania (fitness)

Najważniejszym elementem algorytmu jest funkcja przystosowania, która ocenia jakość danego podziału. W projekcie wykorzystano sumę kwadratów różnic pomiędzy średnimi wartościami statystyk drużyn a średnimi wartościami tych statystyk dla wszystkich zawodników.

Funkcję można zapisać wzorem:

$$
F(X)=\sum_{j=1}^{S}\sum_{i=1}^{T}
w_j\left(\overline{x}_{ij}-\mu_j\right)^2
$$

Gdzie:
- $F(X)$ – wartość funkcji przystosowania dla danego podziału,
- $S$ – liczba analizowanych statystyk,
- $T$ – liczba utworzonych drużyn,
- $w_j$ – waga przypisana danej statystyce,
- **$\overline{x}_{ij}$ – średnia wartość statystyki $j$ w drużynie $i$**,
- $\mu_j$ – średnia wartość statystyki $j$ dla wszystkich zawodników.

W obecnej implementacji wszystkie wagi wynoszą 1, co oznacza, że każda statystyka ma jednakowe znaczenie.

Celem algorytmu jest minimalizacja wartości funkcji przystosowania F(X). Im mniejsza wartość funkcji, tym bardziej wyrównany jest poziom drużyn pod względem analizowanych statystyk. Wykorzystanie kwadratu różnicy powoduje, że większe odchylenia są silniej karane niż mniejsze.

#### Operatory genetyczne

W algorytmie zastosowano trzy podstawowe mechanizmy:

- **Selekcja:** wybierane są osobniki o najniższej wartości funkcji przystosowania. Dzięki temu większe szanse na przekazanie swoich cech mają lepsze rozwiązania.
- **Krzyżowanie jednopunktowe:** chromosomy dwóch rodziców są przecinane w losowym miejscu, a ich fragmenty łączone w celu utworzenia potomków. Ponieważ chromosom reprezentuje permutację, po krzyżowaniu wykonywana jest naprawa powtórzeń, aby każdy zawodnik występował tylko raz.
- **Mutacja typu Swap:** z określonym prawdopodobieństwem zamieniane są miejscami dwa losowo wybrane elementy chromosomu. Pozwala to uzyskiwać nowe kombinacje drużyn i ogranicza ryzyko przedwczesnego zatrzymania algorytmu na lokalnym rozwiązaniu.

### 3. Kluczowe parametry algorytmu

W projekcie zastosowano następujące parametry:

| Parametr | Wartość | Znaczenie |
|---|---:|---|
| Rozmiar populacji | 40 | Liczba osobników w jednym pokoleniu |
| Liczba pokoleń | 100 | Liczba iteracji algorytmu |
| Prawdopodobieństwo mutacji | 0,15 (15%) | Szansa wykonania mutacji chromosomu |
| Liczba zawodników | 12, 24, 48 | Testowane rozmiary zbioru zawodników |
| Liczba zawodników w drużynie | 3 | Każda drużyna składa się z trzech osób |
| Wagi statystyk | Wszystkie równe 1 | Każda statystyka ma jednakowy wpływ na ocenę |
| Liczba powtórzeń testu | 30 | Liczba uruchomień dla każdej wersji danych |

Dodatkowo eksperymenty przeprowadzane są na trzech wersjach plików danych (`v1`, `v2`, `v3`). Dla każdej konfiguracji liczby zawodników i wersji danych algorytm uruchamiany jest trzydzieści razy. Następnie obliczana jest średnia wartość funkcji przystosowania uzyskanych wyników, co pozwala ocenić skuteczność algorytmu i wpływ losowości na otrzymywane rozwiązania.

## 5. Ewaluacja *(B · 8 pkt)*

**Metryka:** Funkcja zrównoważenia drużyn oparta na średnim błędzie kwadratowym (MSE), mierząca odchylenie średnich statystyk poszczególnych drużyn od średniej wszystkich graczy w turnieju.

**Punkt odniesienia:** Metoda bazowa polegająca na 1000 losowych prób podziału zawodników na 3-osobowe drużyny.

#### Tabela z wynikami eksperymentu (Średnia wartość MSE):

| Przypadek / Zbiór | Punkt odniesienia (Losowy) | Biblioteka PyGAD | Nasz Algorytm Genetyczny |
| :--- | :--- | :--- | :--- |
| **12 graczy** | 0.06611 | 0.01410 | 0.01188 |
| **24 graczy** | 0.15129 | 0.05062 | 0.01149 |
| **48 graczy** | 0.33194 | 0.16160 | 0.01065 |

*Uwaga: Wartości w tabeli stanowią uśredniony błąd MSE wyznaczony z 3 niezależnych zestawów danych (v1, v2, v3).*

#### Wykresy porównawcze:

![Porównanie wyników 12 graczy](wykres_porownanie_12_graczy.png)
![Porównanie wyników 24 graczy](wykres_porownanie_24_graczy.png)
![Porównanie wyników 48 graczy](wykres_porownanie_48_graczy.png)

#### Wnioski z przeprowadzonej analizy:
1. **Wyraźna przewaga optymalizacji:** Zastosowanie algorytmu genetycznego z biblioteki PyGAD pozwoliło na wielokrotne obniżenie błędu zrównoważenia drużyn (MSE) w porównaniu do losowego podziału zawodników we wszystkich przetestowanych wariantach.
2. **Skalowalność rozwiązania:** Dla standardowego turnieju (n = 48 graczy) przestrzeń możliwych podziałów jest astronomicznie duża. Metoda losowa uzyskuje bardzo wysoki błąd (MSE ≈ 0.33), podczas gdy PyGAD redukuje go ponad dwukrotnie (MSE ≈ 0.16), co dowodzi praktycznej skuteczności algorytmu genetycznego w rozwiązywaniu tego problemu.

## 6. Wymagania niefunkcjonalne *(A · 5 pkt)*

> Co tu wpisać: ile trwa działanie (na czym mierzone), co się dzieje przy złych lub brakujących danych, czy wyniki są powtarzalne (ziarno losowości).

## 7. Ograniczenia *(E · 4 pkt)*

> Co tu wpisać: kiedy system się myli albo nie zadziała — najlepiej na konkretnym przykładzie. Co zrobilibyście dalej, mając więcej czasu. Czy zastosowana technologia jest dziś nadal stosowana, czy zastąpiły ją nowsze.

## 8. Zastosowania w praktyce *(E · 4 pkt)*

> Co tu wpisać: gdzie podobne rozwiązania są używane w branży (firma, produkt, dziedzina). Jeśli rozmawialiście z praktykiem — co powiedział i co zmieniliście.

## 9. Zespół *(D · 8 pkt)*

> Co tu wpisać: kto za co odpowiadał. Jeśli role się zmieniały — napiszcie kiedy i dlaczego. Wkład powinien zgadzać się z historią repozytorium.

| Osoba | Za co odpowiadała |
|---|---|
| … | … |

## 10. Uruchomienie *(C · 4 pkt)*
```
git clone https://github.com/mpaduch2-lab/Turniej-Bocce
cd Turniej-Bocce
pip install -r requirements.txt
python implementation_genetic_algorithm.py
```

## 11. Narzędzia AI

> Co tu wpisać: czy korzystaliście z narzędzi AI (np. ChatGPT, Claude, Copilot) i do czego — kod, tekst, debugowanie. Jeśli nie — napiszcie „nie korzystaliśmy”. Pamiętajcie: każdą linię kodu musicie umieć wyjaśnić na obronie.
