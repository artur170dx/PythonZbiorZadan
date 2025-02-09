# Odgadnij wzór ciągu na podstawie pierwszych dziesięciu elementów [1], a następ
# nie wyświetl jego sto elementów [2]. Początek ciągu: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, …

result = []
i = 1
while len(result) <= 100:
    for j in range(0, i):
        result.append(str(i))
    i += 1

print(f"Number of elements: {len(result)}")
print(", ".join(result))



# sposób 3 
start = 1 
n = [] 
while len(n) < 100: 
    if (n.count(start) < start): 
        n.append(start) 
    else: 
        start += 1 
print(*n) 