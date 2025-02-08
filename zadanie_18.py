# Pobieraj liczbę z klawiatury i wyświetlaj jej dwukrotność. Operację powtarzaj, do
# póki nie zostanie wpisana wartość pomiędzy 1 a 10 włącznie [1]. Oblicz sumę wy
# świetlonych elementów z pominięciem tej liczby, która kończy pętlę. Wyświetl tę
# sumę [1].

sum = float(0)

entered_value = float(input())
while entered_value not in range(1, 10):
    mul = entered_value * 2
    sum = sum + mul
    print(f"Doubled: {mul}")
    entered_value = float(input())


print(f"Sum: {sum}")
