firstNumber = float(input("Input number: "));
operator = input("Input operator [*, /, +, -]: ")
secondNumber = float(input("Input another number: "));

if operator == "+":
        result = firstNumber + secondNumber
        print(f"{result}")
elif operator == "-":
        result = firstNumber - secondNumber
        print(f"{result}")
elif operator == "*":
        result == firstNumber * secondNumber
        print(f"{result}")
elif operator == "/":
        result == firstNumber / secondNumber
        print(f"{result}")
else:
        print("Imvalid operator. Try again.")