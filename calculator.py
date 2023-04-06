# Define a function for addition
def add(x, y):
   return x + y

# Define a function for subtraction
def subtract(x, y):
   return x - y

# Define a function for multiplication
def multiply(x, y):
   return x * y

# Define a function for division
def divide(x, y):
   return x / y

# Take user input for two numbers and the operation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

# Call the appropriate function based on the operation entered
if op == '+':
   print(num1, "+", num2, "=", add(num1, num2))

elif op == '-':
   print(num1, "-", num2, "=", subtract(num1, num2))

elif op == '*':
   print(num1, "*", num2, "=", multiply(num1, num2))

elif op == '/':
   if num2 == 0:
      print("Error: division by zero")
   else:
      print(num1, "/", num2, "=", divide(num1, num2))

else:
   print("Invalid operation")