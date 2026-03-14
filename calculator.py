a =int(input("Enter a number: "))
b =int(input("Enter b number: "))
print("Choose operation")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")
sum = input("Enter operator: ")
if sum == "+":
    print("Result:", a + b)

elif sum == "-":
    print("Result:", a - b)

elif sum == "*":
    print("Result:", a * b)

elif sum == "/":
     print("Result:", a / b)
else:
    print("Invalid operator")