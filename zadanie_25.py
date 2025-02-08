# Pobieraj w pętli liczby całkowite z klawiatury, wkładaj je do listy V. Szczegółowe
# postępowanie we wnętrzu pętli to następujące kroki:
# 1. Pobierz liczbę i wprowadź ją na koniec listy.
# 2. Pobierz liczbę i wprowadź ją na koniec listy (tak, takie samo polecenie
# w ramach kroku pętli) [1].
# 3. Jeżeli iloczyn dwóch ostatnich liczb z listy nie przekracza 1000, wprowadź
# również ten iloczyn do listy V i wróć do punktu 1., a jeżeli ten iloczyn przekro
# czył wartość 1000, zakończ pętlę [1].
# Pokaż listę po wyjściu z pętli.

V = []

while True:
    V.append(int(input()))
    V.append(int(input()))
    p = V[-1] * V[-2]
    if p < 1000:
        V.append(p)
    else:
        break

print(V)
