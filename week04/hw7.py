#positional_only
def add(a, b , /):
    res = a + b
    return  a, b, res

a, b, result = add(4, 3)
print(f"{a} + {b} = {result}")


#keyword_only
def user(*, name, age):
    return name, age

name , age = user(name = "Fatemeh Sdat", age = 24)
print(f"{name} : {age}")


#calculator
def calculator(first_number, second_number, /, *, operator):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number / second_number
    
print(calculator(2 , 10, operator= "*" ))
    