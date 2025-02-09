# Utwórz listę i wstaw do niej dziesięć dowolnych liczb całkowitych. Utwórz drugą
# listę, która na początku zawiera liczby parzyste z pierwszej listy, a potem pozo
# stałe. Wyświetl obie listy w oddzielnych wierszach.

random_10 = [1, 5, 24, 7, 3, 8, 13, 4, 9, 33]
second = [v for v in random_10 if v % 2 == 0] 
second += [v for v in random_10 if v not in second]

print(second)