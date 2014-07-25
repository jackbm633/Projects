#Addition function
def add(x, y):
    z = x + y
    return z
    
def subtract(x, y):
    z = x - y
    return z
    
def multiply(x, y):
    z = x * y
    return z
    
def divide(x, y):
    z = x / y
    return z
    
def sqrt(x):
    z = x ** (0.5)
    return z
    
def percent(x):
    z = x / 100
    return z
    
def reciprocal(x):
    z = 1 / x
    return z
    
def twonuminput():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: ")) 
    return num1
    return num2 

operation = input("Enter an operation: ")

if operation.lower() == "add" or operation == "+":

    add(twonuminput()[0], twonuminput()[1])

