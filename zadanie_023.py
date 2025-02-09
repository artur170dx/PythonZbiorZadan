# Pobieraj liczby z klawiatury i wkładaj je do listy pod warunkiem, że taka liczba
# jeszcze w liście nie istnieje. Jeżeli istnieje, zignoruj ją i pobieraj dalej. Zakończ po
# bieranie, gdy lista będzie zawierała dziesięć liczb [2].
# Zrób to samo zadanie z wykorzystaniem zbioru (set) [1].

entered_values = []

while len(entered_values) < 10:
    last_input = input()
    if last_input in entered_values:
        continue
    entered_values.append(last_input)

entered_values_set = set()

while len(entered_values_set) < 10:
    entered_values_set.add(input())
