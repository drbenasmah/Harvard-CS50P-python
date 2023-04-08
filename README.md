ALX SE Python Sprint 2 Augmentation with CS50P
This is a repository for the Python Sprint Augmentation with CS50P, part of the ALX Africa Software Engineering program. The purpose of this repository is to provide students with additional resources and exercises to supplement their learning in the Python sprint.

Completed Topics
Conditionals: Explanation of how to use conditional statements in programming.
Incomplete Topics
Functions, Variables
Loops, Exceptions
Libraries, Unit Tests
File I/O, Regular Expressions
Object-Oriented Programming
Et Cetera
Functions
Functions are reusable blocks of code that perform a specific task. They can take input (arguments) and return output. Functions help modularize and organize code, making it easier to read and maintain. Here are some examples of functions:

python
Copy code
def greet(name):
return f"Hello, {name}!"

def add(a, b):
return a + b
In the above example, greet is a function that takes a string argument name and returns a greeting message. add is a function that takes two numeric arguments and returns their sum.

Variables
Variables are used to store values in a program. In Python, variables do not need to be declared before they are used. They are assigned a value using the assignment operator =. Here are some examples of variables:

python
Copy code
x = 5
y = "Hello, world!"
z = True
In the above example, x is an integer variable, y is a string variable, and z is a boolean variable.

Conditionals
Conditionals are used to execute different code blocks based on a specified condition. In Python, conditionals are created using if, elif, and else statements. Here is an example of a conditional:

python
Copy code
x = 5

if x > 10:
print("x is greater than 10")
elif x > 5:
print("x is greater than 5 but less than or equal to 10")
else:
print("x is less than or equal to 5")
In the above example, the conditional checks if x is greater than 10, greater than 5 but less than or equal to 10, or less than or equal to 5, and prints a message accordingly.

Loops
Loops are used to repeat code blocks a specified number of times or until a condition is met. In Python, there are two types of loops: for loops and while loops. Here is an example of a for loop:

python
Copy code
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
print(fruit)
In the above example, the for loop iterates over the fruits list and prints each fruit.

Exceptions
Exceptions are used to handle errors and unexpected situations in a program. In Python, exceptions are raised using the raise statement and handled using try and except statements. Here is an example of an exception:

python
Copy code
try:
x = 5 / 0
except ZeroDivisionError:
print("Cannot divide by zero")
In the above example, the try block attempts to divide 5 by 0, which raises a ZeroDivisionError. The except block catches the exception and prints a message.

Libraries
Libraries are pre-written modules of code that can be imported and used in a program. Python has a large number of libraries for various purposes. Here is an example of importing a library:

python
Copy code
import random

print(random.randint(
