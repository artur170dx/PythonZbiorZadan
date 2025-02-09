# Pobierz liczbę całkowitą z klawiatury i sprawdź, czy jest podzielna: przez 3 i przez 5;
# przez 3, ale nie przez 5; przez 5, ale nie przez 3; ani przez 3, ani przez 5. Właściwą
# odpowiedź wyświetl na ekranie.


def divisible_by(input, div):
    if input % div == 0:
        print(f"{input} is divisible by {div}")
    else:
        print(f"{input} is NOT divisible by {div}")


input = int(input("Provide integer: "))

divisible_by(input, 3)
divisible_by(input, 5)
