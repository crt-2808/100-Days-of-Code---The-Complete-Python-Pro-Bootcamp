from art import logo
def add(num1, num2):
    return num1+num2

def substract(num1,num2):
    return num1-num2

def mult(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2


operations={
    "+": add,
    "-": substract,
    "*": mult,
    "/": div
}
def calculator():
    print(logo)
    num1=float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    shoud_continue=True    
    while shoud_continue:
        function=input("What operation do you want to do?: ")
        num2=float(input("What's the next number?: "))

        calculation_function=operations[function]
        answer=calculation_function(num1, num2)
        print(f"{num1} {function} {num2} = {answer}")
        user_decision=input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation. If you want to exit, type 'exit' to end the program: ").lower()
        if user_decision =="y":
            num1=answer
        elif user_decision=="n":
            shoud_continue=False
            calculator()
        else:
            shoud_continue=False
            
calculator()