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
