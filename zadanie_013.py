# Wyświetl w porządku rosnącym liczby całkowite od 1 do 120, z pominięciem liczb
# podzielnych równocześnie przez 11 i 5. Wyświetl informacje, ile liczb się wyświe
# tliło, a ile zostało pominiętych.


def exclude(v):
    return v % 11 == 0 and v % 5 == 0


result = []
count_printed = 0
count_excluded = 0

for i in range(1, 121):
    if exclude(i):
        count_excluded += 1
        continue
    count_printed += 1
    result.append(str(i))

print(", ".join(result))
print(f"Printed: {count_printed}")
print(f"Excluded: {count_excluded}")
