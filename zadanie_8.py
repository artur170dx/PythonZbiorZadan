# Pobierz z klawiatury dwie liczby (float) i znak działania (jeden z tych: *, +, –, /).
# W zależności od znaku wykonaj na pobranych dwóch liczbach odpowiednie
# i możliwe działania i poinformuj o wyniku [1]. Zwróć uwagę na dzielenie przez 0!
# Przykładowo, dla pobranej liczby 3 i 9,5 oraz znaku + zwróć sumę 3 + 9,5 równą 12,5.
# Sprawdź też operację przy zamianie liczb miejscami [1]. Jeżeli wynik różni się od
# wcześniejszego, wyświetl oba wyniki. Jeżeli jest taki sam, wyświetl go tylko jeden
# raz. Na przykład dla liczb 5 i 2 oraz znaku / (dzielenie) trzeba wyświetlić 5/2 i 2/5,
# ponieważ dają różny wynik.


a = float(input("a: "))
b = float(input("b: "))
operator = input("Arithmetic sign: ")


def calculate(a, b, operator):
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "/":
            if b == 0:
                print("Division by zero")
                exit()
            return a / b
        case "*":
            return a * b


result_1 = calculate(a, b, operator)
result_2 = calculate(b, a, operator)

print(f"a{operator}b={result_1}")
if result_1 != result_2:
    print(f"b{operator}a={result_2}")
