# Wyświetl w porządku rosnącym liczby całkowite od –25 do 25 z pominięciem 0.

for i in range(-25, 26):
    if i == 0:
        continue
    print(i)
