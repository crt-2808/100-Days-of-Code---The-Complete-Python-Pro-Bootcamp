"""
#Ejercicio 1: Calculador de pintura
import math
#Write your code below this line 👇
def paint_calc(height, width, cover):
    num_cans=math.ceil((height*width)/cover)
    print(f"You'll need {num_cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#Ejercicio 2: Revisar si es un numero primo
#Write your code below this line 👇
def prime_checker(number):
    is_Prime=True
    for i in range (2, number):
        if number%i==0:
            is_Prime=False
    if is_Prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
"""
import art


def caesar(text, shift_to_move, cipher_direction):
    message=""
    if(direction=="encode"):
        for char in text:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=position+shift_to_move
                new_letter=alphabet[new_position]
            #encrypted_message+=alphabet[(alphabet.index(text[i])+shift_to_move)]
                message+=new_letter
            else:
                message+=char
    elif(direction=="decode"):
        for char in text:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=position-shift_to_move
                new_letter=alphabet[new_position]
                message+=new_letter
            else:
                message+=char
            
    print(f"The {cipher_direction} text is {message}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
execute=True
enable=True
while execute:
    while enable==True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if(direction=="encode" or direction=="decode"):
            enable=False
    text_input = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift>26:
        shift%=26
    caesar(text=text_input, shift_to_move=shift, cipher_direction=direction)
    answer=input("Would you like to encode/decode again? Type yes or no: ").lower()
    if(answer=="no"):
        execute=False
    else:
        enable=True
    