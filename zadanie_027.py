# Utwórz trzy listy (list) z następującą zawartością (plik 27_listy.txt):
# v1=[1,3,5,7,9]
# v2=[1,4,7,11,15]
# v3=[1,2,3,4,5,6,7,8,9,20]
# Potraktuj je jak zbiory, w których każdy element może wystąpić tylko jeden raz.
# Przykładowo, po dodaniu do zbioru v1 liczby 5, zbiór nie uległby zmianie, gdyż 5
# już tam jest. Dla podanych list/zbiorów wyświetl:
# a) część wspólną zbiorów: v1 i v2 [2],
# b) różnicę zbioru v3 i sumy zbiorów v1+v2 := v3–(v1+v2) [3],
# c) sumę wszystkich zbiorów v1, v2 i v3 := v1+v2+v3 [2].
# Wykonaj to zadanie jeszcze raz z wykorzystaniem zbiorów (set) [1].
# Różnica zbioru A – B to takie elementy A, których nie ma w B. Suma zbiorów A + B
# to wszystkie elementy z A i B (bez powtórzeń). Część wspólna A i B to tylko takie
# elementy, którą są równocześnie w A i B.

v1 = [1, 3, 5, 7, 9]
v2 = [1, 4, 7, 11, 15]
v3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

v1_and_v2 = []
for v in v1:
    if v in v2:
        v1_and_v2.append(v)
print(f"v1 and v2: ", v1_and_v2)

v1_sum_v2 = v1.copy()
for v in v2:
    if v not in v1_sum_v2:
        v1_sum_v2.append(v)
v3_minus_v1_sum_v2 = []
for v in v3:
    if v not in v1_sum_v2:
        v3_minus_v1_sum_v2.append(v)
print(f"v3_minus_v1_and_v2: ", v3_minus_v1_sum_v2)

sum = v1_sum_v2.copy()
for v in v3:
    if v not in sum:
        sum.append(v)
print("sum: ", sum)

s1 = set(v1)
s2 = set(v2)
s3 = set(v3)

print(f"s1 and s2: ", s1 & s2)
print(f"v3_minus_v1_and_v2: ", s3 - (s1 | s2))
print("sum: ", s1 | s2 | s3)
