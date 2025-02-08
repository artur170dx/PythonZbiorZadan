# Masz takie wyrażenie: (((a1+a2)*a3)-a4)/a5 (elementy od a1 do a5 są typu zmien
# noprzecinkowego: float). Pobierz z klawiatury każdą ze zmiennych a1 do a5, oblicz
# wartość wyrażenia i wyświetl wynik. Zwróć uwagę na wartość zmiennej a5. W przy
# padku, gdy jej wartość będzie równa 0, nie wykonuj działania, tylko poinformuj o tym.


print("Calculate (((a1+a2)*a3)-a4)/a5")

a = []
for a_i in range(1, 6):
    a.append(float(input(f"Provide value for a{a_i}: ")))

if a[4] == 0:
    print("a5 is equal 0. Can't calculate")
    exit()

result = ((a[0] + a[1]) * a[2] - a[3]) / a[4]
print(f"(((a1+a2)*a3)-a4)/a5 = {result}")
