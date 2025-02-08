# Pobierz pięć liczb z klawiatury. Jeżeli tworzą ciąg rosnący (zgodnie z kolejnością
# pobierania), poinformuj o tym.


def is_sorted(values: list):
    values_copy = values.copy()
    values_copy.sort()
    return values == values_copy


input_values = []

for _ in range(5):
    input_values.append(int(input()))

if is_sorted(input_values):
    print("The provided list is sorted in asending order")
