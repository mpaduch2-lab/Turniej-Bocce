# Karta zgłoszenia tematu projektu

**Wersja karty:** 22.10.2026 · *zmiana względem poprzedniej wersji: pkt 5 uzupełniony o pytanie „dlaczego nie zwykły algorytm”*

**Grupa:** L2 · **Zespół:** Z9 · **Data:** 22.10.2026
Sztuczna inteligencja — laboratorium · Collegium Da Vinci · rok akad. 2026/2027
Pierwsza wersja: mailem do **22.10, 16:45**. Poprawki: mailem do **29.10, 16:45**. Temat maila: `SI L2 · Z9 · karta`.

## 1. Skład zespołu

> Rola jest wstępna — można ją zmienić w trakcie projektu bez uzgadniania.

| Imię i nazwisko | Nr albumu | Rola (wstępna) |
| --- | --- | --- |
| Antonina Bentyn | 29211 | Porównanie, Wyniki, Dokumentacja |
| Mateusz Paduch | 31162 | Generowanie danych, Algorytm, Dokumentacja |

## 2. Roboczy tytuł (PL)

Dobieranie do składu drużyny w grę Bocce.

## 3. Tytuł (EN)

Selecting team members for a game of Bocce.

## 4. Problem — co system ma robić i dla kogo (3–5 zdań)

Dobiera skład drużyn po trzech zawodników/zawodniczek. Dba o to, aby drużyny były zrównoważone (patrząc na statystyki). System będzie przeznaczony dla organizatorów/organizatorek turniejów. Dla zachowania największego napięcia wśród oglądających oraz zapewnienie poczucia sprawiedliwości i równego traktowania wszystkich, drużyny biorące udział w turnieju nie powinny znacząco odbiegać od siebie poziomem umiejętności, co jest trudne do zrobienia.

## 5. Dlaczego SI i dlaczego ta technologia

**a) Dlaczego zwykły algorytm nie wystarczy.** Zaznaczcie jeden powód:

- [ ] nie umiemy zapisać reguły krok po kroku
- [x] przepis istnieje, ale jest obliczeniowo za drogi
- [ ] reguł jest za dużo i zmieniają się w czasie

Uzasadnienie (2–3 zdania):

Zwykły algorytm nie pasuje do problemu gdyż ma on zbyt wiele parametrów i możliwości. Algorytm zwykły zająłby zbyt dużo czasu dla dużej liczby uczesników. Ilość kombinacji do sprawdzenia dla n zawodników (podzielonych na drużyny trzyosobowe) wyraża się wzorem:

$$
T(n) = \frac{n!} {(3!)^{\frac{n} {3}}(\frac{n}{3})!}
$$

n musi być liczbą podzielną przez 3. $n!$ oznacza liczbę możliwych ustawień wszystkich osób. $(3!)^{\frac{n} {3}}$ oznacza brak zależności kolejności w każdej z $\frac n 3$ drużyn. $(\frac{n}{3})!$ oznacza brak znaczenia kolejności drużyn.

| $n$ podzielne przez $3$ | $T(n)$ |
| --- | --- |
| $12$ | $15400$  |
| $24$ | $\approx 1.18 \times10^{18}$  |
| $48$ - standardowa ilość osób w turnieju | $\approx 1.23 \times10^{38}$  |

Sprawdzając 1 miliard podziałów na sekundę sprawdzenie wszystkich podziałów dla 48 osób zajęłoby $3.9 \times 10^{21}$ lat, czyli więcej niż wiek Wszechświata.

**b) Technologia SI:**

- [ ] sieć neuronowa
- [ ] system ekspertowy / wnioskowanie regułowe
- [x] algorytm genetyczny
- [ ] klasyczne uczenie maszynowe

Dlaczego ta technologia pasuje do tego problemu (2–3 zdania):

Ta technologia ta technologia bardzo szybka przeszukuje duże przestrzenie rozwiązań oraz znajduje optymalne lub bliskie optymalnemu rozwiązanie problemu. Osobnikiem w tym przypadku będzie ciąg liczb od 1 do 48 z którego każde kolejne 3 osoby trafiają odpowiednio do drużyn od 1 do 16. Funkcja przystosowania będzie przypisywać wartość $\infin$ tym ciągom, które będą posiadały powtórki, a dla pozostałych będzie obliczał:

$$
\sum_{j=1}^7 w_j(\frac 1 3(S[x_{3i-2}, j] + S[x_{3i-1}, j] + S[x_{3i}, j]) - \mu_j)^2
$$
> Pkt 5 to pierwsza wersja sekcji 2 dokumentacji projektu („Dlaczego SI i dlaczego ta technika”). To, co tu napiszecie, rozwiniecie później w dokumentacji.

## 6. Dane

- Źródło: Spis osób uczestniczących w turneju Bocce
- Rozmiar / format: CSV o kolumnach (Imię i nazwisko, Celność, Panowanie nad stresem, Poziom koncentracji, Siła rzutu, Skuteczność rzutów, Dostosowywanie się do terenu, Umiejętność czytania gry) i $48$ wierszach. Wszystkie wartości numeryczne będą z przedziału $[0,1]$
- Czy dane są już dostępne? nie — plan pozyskania: Wygenerujemy losowe dane rozkładem normalnym ograniczonym do przedziału $[0,1]$ ze średnią w $0.5$ oraz wariancji $0,0289$ - $\mathcal{N}(0.5, 0,0289)$

## 7. Stos technologiczny

- Python
- Numpy - obliczenia na macierzach, wczytywanie danych z pliku
- Matplotlib.pyplot - wykresy
- PyGAD - porównanie wyniku

## 8. Kryterium sukcesu

- Metryka i próg: Funkcja zrównoważenia drużyn. Zestaw najmniej różniących się drużyn. Jak najmniejsza różnica statystyk między drużynami.

  - $x$ - wektor przemieszania
  - $i$ - indeks drużyny
  - $j$ - indeks statystyki
  - $\mu_j$ - średnia wartość j-tej statystyki
  - $w$ - wektor wpływu poszczególnych statystyk na balans drużyny
  - $S$ - macierz statystyk
$$
MSE(x) = \sum_{i=1}^{\frac {n} {3}} \sum_{j=1}^7 w_j(\frac 1 3(S[x_{3i-2}, j] + S[x_{3i-1}, j] + S[x_{3i}, j]) - \mu_j)^2
$$


- Punkt odniesienia (prosta metoda, z którą porównacie wynik): 
Losowym podział zawodników na 16 drużyn po 3 osoby.
Powinien on dawać różne wyniki, ale średnio może być mniej wyrównany niż podział zoptymalizowany.
Jeśli wynik będzie podobny, może to oznaczać, że algorytm genetyczny nie poprawia istotnie jakości podziału albo, że trzeba przyjąć inną metrykę.
Algorytmy porównamy w takich konfiguracjach:

| $n$ podzielne przez $3$ | Ilość losowych podziałów | Ilość uruchomień AG | Ilość zestawów zawodników |
| --- | --- | --- | --- |
| $12$ | 1000 | 30 | 3 |
| $24$ | 1000 | 30 | 3 |
| $48$ - standardowa ilość osób w turnieju | 1000 | 30 | 3 |

## 9. Zakres minimalny (co powstanie na pewno)

- Generator danych — program w Pythonie generujący zestawy zawodników wraz z siedmioma statystykami z przedziału ([0,1]) i zapisujący je do plików CSV. Przygotujemy zestawy dla 12, 24 i 48 zawodników oraz po trzy niezależne zestawy danych dla każdej liczebności.
- Wczytywanie i walidacja danych — moduł odczytujący pliki CSV i sprawdzający poprawność danych, liczbę zawodników oraz zakres wartości statystyk.
- Funkcja oceny podziału — implementacja funkcji MSE mierzącej zrównoważenie drużyn na podstawie siedmiu statystyk.
- Losowy podział zawodników — implementacja metody bazowej tworzącej drużyny po trzy osoby oraz obliczającej wynik MSE.
- Algorytm genetyczny — implementacja algorytmu w bibliotece PyGAD, który wyszukuje podział zawodników na zrównoważone drużyny. Rozwiązania będą kodowane jako permutacje indeksów zawodników, dzięki czemu każdy zawodnik wystąpi dokładnie raz.
- Eksperyment porównawczy — wykonanie 1000 losowych podziałów i 30 uruchomień algorytmu genetycznego dla każdego zestawu danych.
- Analiza wyników — zapis wyników eksperymentów do plików oraz porównanie średnich wartości MSE obu metod. Przygotujemy wykresy pokazujące uzyskane wyniki dla różnych liczebności grup.
- Dokumentacja i instrukcja uruchomienia — opis sposobu przygotowania danych, działania funkcji celu, konfiguracji algorytmu genetycznego oraz przeprowadzonych eksperymentów. Dokumentacja będzie zawierać wymagane sekcje w języku angielskim.

## 10. Zakres opcjonalny (co dorobimy, jeśli starczy czasu)

W ramach rozszerzenia algorytm będzie uwzględniał role zawodników w grze Bocce: pointeur (zawodnik precyzyjnie umieszczający kule), milieu (zawodnik pełniący rolę wszechstronną) oraz tireur (zawodnik specjalizujący się w wybijaniu kul przeciwnika).

Rozszerzenie obejmie przypisanie zawodnikom dodatkowych ocen określających ich predyspozycje do poszczególnych ról oraz modyfikację funkcji celu tak, aby uwzględniała zarówno zrównoważenie drużyn pod względem umiejętności, jak i odpowiednie uzupełnianie się zawodników.

## 11. Repozytorium

https://github.com/mpaduch2-lab/Turniej-Bocce

## 12. Główne ryzyko i plan awaryjny

- Algorytm genetyczny nie uzyska wystarczająco zrównoważonych drużyn.

  - Plan awaryjny: przeanalizujemy wpływ parametrów algorytmu, takich jak liczebność populacji, prawdopodobieństwo mutacji, sposób selekcji oraz liczba pokoleń. W razie potrzeby zmodyfikujemy operator krzyżowania lub mutacji, zachowując poprawność reprezentacji rozwiązań.

- Losowy podział okaże się prawie tak dobry jak algorytm genetyczny.

  - Plan awaryjny: uczciwie przedstawimy uzyskane wyniki, porównując średnie MSE, oraz najlepsze wyniki obu metod. Sprawdzimy również, czy zmiana parametrów algorytmu lub uwzględnienie ról zawodników pozwoli poprawić rezultat. Jeżeli różnica pozostanie niewielka, opiszemy to jako wniosek z eksperymentu, a nie jako sukces optymalizacyjny.

- Wygenerowane dane nie pozwolą uzyskać bardzo wyrównanych drużyn.

  - Plan awaryjny: sprawdzimy rozkłady statystyk oraz różnice między zawodnikami. Jeżeli ograniczenia wynikają z dużego zróżnicowania puli, przedstawimy najlepszy znaleziony podział i wyjaśnimy, dlaczego dalsze wyrównanie może być trudne.

- Algorytm genetyczny nie znajdzie najlepszego możliwego rozwiązania.

  - Plan awaryjny: nie będziemy twierdzić, że znaleźliśmy optimum globalne, jeśli nie potwierdzimy tego. Dla małych zestawów zawodników będzie możliwe porównanie pełnego przeszukania z rozwiązaniem uzyskanym przez algorytm genetyczny. Dla większych zestawów ocenimy jakość rozwiązania na podstawie wyników metody losowej, wielu uruchomień algorytmu i stabilności rezultatów.

---

*Decyzja prowadzącego:* [ ] zatwierdzony  [ ] do poprawy · *Uwagi:*

---
<small>Bartosz Lewandowski · bartosz.lewandowski@cdv.pl · Sztuczna inteligencja — laboratorium, grupa L2 (I.SI.519) · Collegium Da Vinci · rok akad. 2026/2027</small>
