# Odgadnij wzór ciągu na podstawie pierwszych ośmiu elementów [1], a następnie
# wyświetl jego sto elementów [1]. Początek ciągu: 3, 1, 2, 1, 3, 1, 2, 1, …

const = [3, 1, 2, 1]

result = []
for i in range(0, 100):
    result.append(str(const[i % 4]))

print(", ".join(result))