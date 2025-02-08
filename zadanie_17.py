# Odgadnij wzór ciągu na podstawie pierwszych dziesięciu elementów [1], a następnie
# wyświetl jego sto elementów [1]. Początek ciągu: 6, 2, 8, 3, 10 ,4, 12, 5, 14, 6, …

# diff -4, 6, -5, 7, -6, 8, -7, 9, -8


start_odd, start_even = 6, 2

odd, even = start_odd, start_even

result = []
for i in range(0, 100):
    if i % 2 == 0:
        result.append(odd)
        odd += 2
    else:
        result.append(even)
        even += 1


print(*result)
