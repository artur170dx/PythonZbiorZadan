# Pobierz liczbę całkowitą z klawiatury i wykonaj na niej poniższe operacje: jeżeli
# liczba była ujemna, zmniejsz ją o 1; jeżeli liczba była dodatnia, zwiększ ją o 1; jeżeli
# była zerem, pozostaw bez zmian; Wyświetl liczbę po zmianach [1]. Następnie określ
# parzystość liczby po zmianach i wyświetl informację na ten temat za pomocą ade
# kwatnego komunikatu [1].


value = int(input())

change = 0

if value < 0:
    change = +-1
if value > 0:
    change = +1

result = value + change

print(result)

if result % 2 == 0:
    print("Even")
else:
    print("Odd")
