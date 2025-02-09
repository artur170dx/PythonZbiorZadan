# Wyświetl w porządku malejącym liczby całkowite od 100 do 10 z wyłączeniem 10,
# pomijając podzielne przez 7.


def exclude(v) -> bool:
    return v == 10 or v % 7 == 0


result = []
for i in range(100, 10, -1):
    if exclude(i):
        continue
    result.append(str(i))

print(", ".join(result))
