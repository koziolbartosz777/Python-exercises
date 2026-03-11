num1 = float(input("Enter first number: "))
while True:
    operator = input("Enter operator: ")
    if operator not in "+-*/":
        continue
    break

num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1*num2
elif operator == "/":
    result = num1/num2
else:
    print("Invalid operator. Try again")

print(result)