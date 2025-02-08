# Pobieraj liczby z klawiatury i wkładaj je do listy [1]. Pobieranie ma się zakończyć,
# gdy zostanie wprowadzona dwa razy z rzędu taka sama liczba [1].

values = []

value = input()
values.append(value)
value = input()
while True:
    if values[-1] == value:
        break
    values.append(value)
    value = input()
