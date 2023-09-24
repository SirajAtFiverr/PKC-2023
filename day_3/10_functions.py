
# Functions
# Functions is a block of code which only runs when it is called.

def print_info():
    print("Hello World!")
    print("Welcome to Python Programming")

print_info() # calling the function

def calculator(num1, num2):
    print("Sum:", num1 + num2)
    print("Difference:", num1 - num2)
    print("Product:", num1 * num2)
    print("Quotient:", num1 / num2)

calculator(23, 73) # calling the function

def square(num):
    return num * num

print(square(5)) # calling the function