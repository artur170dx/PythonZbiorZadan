def divisible_by(input, div) :
    if input % div == 0 :
        print(f"{input} is divisible by {div}")
    else :
        print(f"{input} is NOT divisible by {div}")
        
input = int(input("Provide integer: "))

divisible_by(input, 3)
divisible_by(input, 5)