# Karta zgłoszenia tematu projektu

**Wersja karty:** 22.10.2026 · *zmiana względem poprzedniej wersji: pkt 5 uzupełniony o pytanie „dlaczego nie zwykły algorytm”*

**Grupa:** L2 · **Zespół:** Z9 · **Data:** 22.10.2026
Sztuczna inteligencja — laboratorium · Collegium Da Vinci · rok akad. 2026/2027
Pierwsza wersja: mailem do **22.10, 16:45**. Poprawki: mailem do **29.10, 16:45**. Temat maila: `SI L2 · Z9 · karta`.

## 1. Skład zespołu

> Rola jest wstępna — można ją zmienić w trakcie projektu bez uzgadniania.

| Imię i nazwisko | Nr albumu | Rola (wstępna) |
| Antonina Bentyn | 29211 | Duchnik & Ben |
| Mateusz Paduch | 31162 | Duchnik & Ben |

## 2. Roboczy tytuł (PL)

Dobieranie do składu drużyny w grę Bocce.

## 3. Tytuł (EN)

Selecting team members for a game of Bocce.

## 4. Problem — co system ma robić i dla kogo (3–5 zdań)

Dobiera skład drużyn po trzech zawodników/zawodniczek. Dba o to, aby drużyny były zrównoważone (patrząc na statystyki). System będzie przeznaczony dla organizatorów/organizatorek turniejów.

## 5. Dlaczego SI i dlaczego ta technologia

**a) Dlaczego zwykły algorytm nie wystarczy.** Zaznaczcie jeden powód:

- [ ] nie umiemy zapisać reguły krok po kroku
- [x] przepis istnieje, ale jest obliczeniowo za drogi
- [ ] reguł jest za dużo i zmieniają się w czasie

Uzasadnienie (2–3 zdania):

Zwykły algorytm nie pasuje do problemu gdyż ma on zbyt wiele parametrów i możliwości. Algorytm zwykły zająłby zbyt dużo czasu dla dużej licby uczesników.    

**b) Technologia SI:**

- [ ] sieć neuronowa
- [ ] system ekspertowy / wnioskowanie regułowe
- [x] algorytm genetyczny
- [ ] klasyczne uczenie maszynowe

Dlaczego ta technologia pasuje do tego problemu (2–3 zdania):

Ta technologia ta technologia bardzo szybka przeszukuje duże przestrzenie rozwiązań oraz znajduje optymalne lub bliskie optymalnemu rozwiązanie problemu. W przeciwieństwie do pełnego przeszukania wszystkich stanów, nie musi sprawdzać ich wszystkich po kolei, lecz z każdą ewolucją zachowują siętylko te cechy które polepszają rozwiązanie.

> Pkt 5 to pierwsza wersja sekcji 2 dokumentacji projektu („Dlaczego SI i dlaczego ta technika”). To, co tu napiszecie, rozwiniecie później w dokumentacji.

## 6. Dane

- Źródło: Spis osób uczestniczących w turneju Bocce
- Rozmiar / format: CSV o kolumnach (Imię i nazwisko, Celność, Panowanie nad stresem, Poziom koncentracji, Siła rzutu, Skuteczność rzutów, Dostosowywanie się do terenu, Umiejętność czytania gry)
- Czy dane są już dostępne? nie — plan pozyskania: Wygenerujemy losowe dane

## 7. Stos technologiczny

Python

## 8. Kryterium sukcesu

- Metryka i próg: Funkcja zrównoważenia drużyn. Zestaw najmniej różniących się drużyn. Jak najmniejsza różnica statystyk między drużynami.
- Punkt odniesienia (prosta metoda, z którą porównacie wynik): Różnica statystyk między najlepszą a najgorszą drużyną jest nie większa niż 10%.

## 9. Zakres minimalny (co powstanie na pewno)

System, który z listy uczestników i opisu ich umiejętności będzie układał zrównoważone drużyny do turnieju Bocce.

## 10. Zakres opcjonalny (co dorobimy, jeśli starczy czasu)

Działająca tabela wyników uzupełniana w trakcie rozgrywek pokazująca ostateczny wynik.

## 11. Repozytorium

https://github.com/mpaduch2-lab/Turniej-Bocce

## 12. Główne ryzyko i plan awaryjny

Ryzyko, że drużyny wyjdą niewystarczająco zbalansowane lub pula zawodników będzie nie zbalansowana przez co nie będzie możliwe utworzenie mało zróżnicowanych drużyn. Planem awaryjnym jest akceptacja wyniku, jeżeli nie istnieje lepszy lub w przypadku niewystarczającej dokładności możemy dodać więcej statystyk / zmienić metrykę / zmienić paarametry algorytmu genetycznego.

---

*Decyzja prowadzącego:* [ ] zatwierdzony  [ ] do poprawy · *Uwagi:*

---
<small>Bartosz Lewandowski · bartosz.lewandowski@cdv.pl · Sztuczna inteligencja — laboratorium, grupa L2 (I.SI.519) · Collegium Da Vinci · rok akad. 2026/2027</small>
