import random
"""
#Importas un nuevo modulo al programa
import mi_modulo
#El valor pi esta almacenado en el archivo mi_modulo, por lo que puedo nombrar otra variable llamada pi y que tenga un valor diferente al del modulo
pi=3.14
print(mi_modulo.pi)
print(pi)

#Ejercicio1: Simula el lanzamiento de una moneda
coin=random.randint(0,1)
if coin==1:
    print("Heads")
else:
    print("Tails")
    
    
Ejercicio2: toma un elemento random de una lista y decide quien va a pagar
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
personToPay=names[random.randint(0, (len(names)-1))]
print(f"{personToPay} is going to buy the meal today!")

Ejercicio3: pone una X en el lugar en el que se le indica
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
row_position=int(position[1])
column_postition=int(position[0])
Treasure='X'
map[row_position-1][column_postition-1]=Treasure
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
"""
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
elements=[rock, paper, scissors]
user_election=int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if(user_election>2):
    print("You choose an invalid number, you loose")
else:
    print(elements[user_election])
    print("Computer chose:")
    computer_election=random.randint(0, 2)
    print(elements[computer_election])
    if(user_election==computer_election):
            print("It is a tie")
    elif((computer_election+1==user_election)or(computer_election==2 and user_election==0)):
            print("You Win")
    else:
            print("You loose")