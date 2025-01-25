def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return a / b
    return a/b    
a=10
b=15
print(f"sum = {add(a,b)}")    
print(f"Difference = {subtract(a,b)}")
print(f"Product = {multiply(a,b)}")
print(f'Division = {divide(a,b)}')