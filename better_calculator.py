num1 = float(input("please enter first interger: "))
operator = input("please enter the arithmetic operator: ")
num2 = float(input("please enter second integer: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("不支援的運算")
