# Pobieraj z klawiatury znaki (bez polskich ogonków i bez dużych liter) i wprowadzaj
# je do listy według zasady: samogłoski zawsze na początku listy, pozostałe znaki na
# końcu listy. Jeżeli pojawi się znak * lub #, nie wstawiaj ich, tylko usuń z listy pierwszy
# znak (dla *) lub ostatni (dla #), o ile jest co usuwać. Zakończ pętlę pobierania i wsta
# wiania, gdy wprowadzony będzie znak ! (wykrzyknik).

VOWELS = ["a", "e", "i", "o", "y"]
result = []

input_char = input()
while input_char != "!":
    if input_char in VOWELS:
        result.insert(0, input_char)
    elif input_char == "*":
        result.pop(0)
    elif input_char == "#":
        result.pop()
    elif input_char == "!":
        break
    else:
        result.append(input_char)

    print(result)

    input_char = input()
