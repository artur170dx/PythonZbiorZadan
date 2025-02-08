# Pobieraj znaki z klawiatury aż do wprowadzenia znaku x. Ile znaków pobrano?


char_counter = 0

while input() != "x":
    char_counter += 1

print(char_counter)
