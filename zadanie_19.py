# Wyświetl wszystkie liczby podzielne przez 6 ze zbioru od 0 do 1000 włącznie [1].
# Ile ich było? Ile wśród tych liczb było takich, które zawierają cyfrę 7? Wyświetl od
# dzielnie również te liczby i ich ilość [2].

div_by_6 = []
contains_7 = []

for i in range(0, 1001):
    if i % 6 == 0:
        div_by_6.append(i)
        if "7" in str(i):
            contains_7.append(i)

print("Div by 6:\n", *div_by_6)
print(f"Quantity of div by 6:\n {len(div_by_6)}")

print("Contains 7:\n", *contains_7)
print(f"Quantity of contains 7:\n {len(contains_7)}")
