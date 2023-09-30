"""
programming_dictionary={
    "Bug":"Error que evita que el programa funcione correctamente",
    "Loop": "Secuencia que se ejecuta cada cierto numero"
}
programming_dictionary2={
    "Bug":"Error que evita que el programa funcione correctamente",
    "Loop": "Secuencia que se ejecuta cada cierto numero"
}
# Llamada a la llave Bug
print(programming_dictionary["Bug"])
#Añadir un nuevo elemento
programming_dictionary["Funcion"]="Fraccion de codigo que se puede reutilizar"
print(programming_dictionary)
#Limpiar un diccionario
programming_dictionary2={}
#Acceder a los elementos e imprimir sus llaves
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])   
"""
from art import logo
import os

def clear():
    os.system('clear')

def find_highest_bidder(bidding_record):
    highest_bid=0
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
bids={}
biding_finish= False
print(logo)
while not biding_finish:
    name=input("What is yout name?: ")
    price=int(input("What is your bid?: $"))
    bids[name]=price
    should_continue=input("Are there any other bidders? Types yes or no: ").lower()
    if should_continue=="no":
        biding_finish=True
        find_highest_bidder(bids)
    elif should_continue=="yes":
        print("-------------------------------------")




