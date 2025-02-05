a = float(input("a: "))
b = float(input("b: "))
operator = input("Arithmetic sign: ")

def calculate(a, b, operator):
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "/":
            if b == 0:
                print("Division by zero")
                exit()
            return a / b
        case "*":
            return a * b

result_1 = calculate(a, b, operator)
result_2 = calculate(b, a, operator)

print(f"a{operator}b={result_1}")
if result_1 != result_2:
    print(f"b{operator}a={result_2}")
