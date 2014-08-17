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
    return (num1, num2)

operation = input("Enter an operation: ")

if operation.lower() == "add" or operation == "+":
    i = twonuminput()
    
    result = add(i[0], i[1])
    print(result)

elif operation.lower() == "subtract" or operation == "-":
	i = twonuminput()
	
	result = subtract(i[0], i[1])
	print(result)

elif operation.lower() == "multiply" or operation == "*":
	i = twonuminput()
	
	result = multiply(i[0], i[1])
	print(result)

elif operation.lower() == "divide" or operation == "/":
	i = twonuminput()
	
	result = divide(i[0], i[1])
	print(result)

elif operation.lower() == "percent":
	i = float(input("Enter a number: ", "%"))
	
	result = percent(i)
	print(result)
	
elif operation.lower() == "reciprocal":
	i = float(input("Enter a number: "))
	
	result = reciprocal(i)
	print(result)
	
elif operation.lower() == "sqrt" or operation.lower() == "squareroot" or operation.lower() == "square root":
	i = float(input("Enter a number: "))
	
	result = sqrt(i)
	print(result)
