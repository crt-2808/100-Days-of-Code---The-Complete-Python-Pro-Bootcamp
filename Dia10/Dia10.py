from art import logo
print(logo)

def add(num1, num2):
    return num1+num2

def substract(num1,num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2


operation={
    "+": add,
    "-": substract,
    "*": mult,
    "/": div
}

num1=int(input("What's the first number?: "))
for symbol in operation:
    print(symbol)
function=input("What operation do you want to do? Please type one of the symbols above: ")
num2=int(input("What's the second number?: "))

calculation_function=operation[function]
result=calculation_function(num1, num2)

print(f"{num1} {calculation_function} {num2} = {result}")

for symbols in operation:
    print(symbol)
function=input("What operation do you want to do? Please type one of the symbols above: ")
num3=int(input("What's the next number?: "))

calculation_function=operation[function]
result_2=calculation_function(result, num3)
print(f"{result} {calculation_function} {num3} = {result_2}")
