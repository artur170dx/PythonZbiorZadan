# Pobierz z klawiatury trzy nieujemne liczby całkowite. Jeżeli któraś jest ujemna, po
# wtórz pobieranie. Następnie znajdź największą z nich [1]. Wyświetl sumę pozosta
# łych liczb tyle razy, ile wynosi wartość największej liczby [1].


def get_positive():
    v = int(input())
    if v > 0:
        return v
    return get_positive()


list = [get_positive(), get_positive(), get_positive()]

list.sort()

sum = list[0] + list[1]

for i in range(list[2]):
    print(sum)
