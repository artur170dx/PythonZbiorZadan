# Pobieraj w pętli jeden znak. Ignoruj znaki niebędące znakami cyfr (0 – 9). Przerwij 
# pętlę, gdy zbierzesz pięć znaków będących cyframi, np. '1', '4', '3', '5', '0'. Utwórz 
# zmienną całkowitą, która będzie liczbą utworzoną z tych cyfr. Dla podanego przy
# kładu byłaby to liczba całkowita: 14 350. Utwórz również liczbę w odwrotnej ko
# lejności cyfr. W obu przypadkach, gdy liczba zaczyna się od cyfr 0, należy je zigno
# rować. Na przykład 05341 to 5341. Wyświetl sumę obu powstałych liczb.

def stop(input: list[int]) -> bool: 
    return len(input) >= 5
    
input_list = []
valid_input = "0123456789"

while not stop(input_list):
    value = input("Provide value: ")
    if value in valid_input:
        input_list += value
    else:
        print("Value ignored")

integer = int("".join(input_list))
reverse_integer = int("".join(reversed(input_list)))

print(integer)
print(reverse_integer)

print(f"Sum: {integer + reverse_integer}")