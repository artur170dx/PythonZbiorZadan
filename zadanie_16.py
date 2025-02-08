# Odgadnij wzór ciągu na podstawie pierwszych sześciu elementów [1], a następnie
# wyświetl jego sto elementów. Początek ciągu: 100, 99, 97, 94, 90, 85, … Ile wynosi
# ostatni (setny) element ciągu? [2]

step = 1
start = 100

result = [start]

for i in range(0, 99):
    result.append(result[i] - step)
    step += 1


print(*result)
print(f"Last value: {result[-1]}")
