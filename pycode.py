import sys

def add(a, b):
    return a + b

def sub(a, b):
    try:
        c = a / b
        return c
    except:
        print("Division by zero not possible")
        sys.exit()
def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print(add(10,12))
print(sub(10,12))
print(mul(10,12))
print(div(10,0))
