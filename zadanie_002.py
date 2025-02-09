# Pobraną z klawiatury liczbę całkowitą zweryfikuj pod kątem parzystości. Wyświetl
# adekwatny komunikat, gdy jest lub nie jest parzysta.

input = int(input())

if input % 2 == 0:
    print("even")
else:
    print("odd")
