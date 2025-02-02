def get_positive():
    v = int(input())
    if v>0:
        return v
    return get_positive()

list = [get_positive(), get_positive(), get_positive()]

list.sort()

sum = list[0] + list[1]

for i in range(list[2]):
    print(sum)