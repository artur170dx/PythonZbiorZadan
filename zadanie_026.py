# Utwórz listę zawierającą następujące cyfry (można skopiować z pliku 26_lista.txt):
#  v=[1,2,4,3,6,8,7,7,8,3,4,5,6,7,1,3,9,1,0,4,2,3,6,9]
# Znajdź w liście i wyświetl wszystkie podciągi trójelementowe (trzy kolejne cyfry
# listy), które tworzą ciągi niemalejące [2]. Znajdź przynajmniej jeden najdłuższy
# podciąg niemalejący [4]. Policz liczbę wystąpień każdej liczby w liście [1].

# def find_3(v: list[int], start_pos):
#     for el in v:

v = [1, 2, 4, 3, 6, 8, 7, 7, 8, 3, 4, 5, 6, 7, 1, 3, 9, 1, 0, 4, 2, 3, 6, 9]

for i in range(2, len(v)):
    if v[i - 2] < v[i - 1] < v[i]:
        print(f"Sequence of 3: {v[i-2:i+1]}")

longest_seq_start = 0
longest_seq_end = 0

for i in range(1, len(v)):
    for j in range(i, len(v)):
        if v[j - 1] <= v[j]:
            if (longest_seq_end - longest_seq_start) <= (j - i):
                longest_seq_start = i - 1
                longest_seq_end = j
        else:
            break

print(f"Longest seq: {v[longest_seq_start:longest_seq_end + 1]}")


counter_dict = {}
for d in v:
    if d in counter_dict:
        counter_dict[d] += 1
    else:
        counter_dict[d] = 1

print(f"Counter of digits: {counter_dict}")
