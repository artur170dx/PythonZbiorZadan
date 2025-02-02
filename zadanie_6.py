evens = 0
odds = 0

for x in range(5) :
    if int(input()) % 2 == 0 :
        evens += 1
    else :
        odds += 1

print(f"{evens} evens")
print(f"{odds} odds")