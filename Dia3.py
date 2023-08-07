"""
#Primer ejercicio
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number%2 !=0:
    print("This is an odd number.")
else:
    print("This is an even number.")
    
#Segundo Ejercicio
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI=weight/(height**2)
BMI=round(BMI)
if BMI<18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif (18.5<BMI<25):
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif (25<BMI<30):
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif(30<BMI<35):
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")


#Tercer Ejercicio
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
if (year %4 ==0):
    if (year%100==0):
        if(year%400==0):
            print("Leap year.")
        else:
            print("Not leap year.")

    else:
        print("Leap year.")
else:
    print("Not leap year.")

#Cuarto Ejercicio
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
bill=0

if(size=="S"):
    bill=15
elif(size=="M"):
    bill=20
else:
    bill=25

if(add_pepperoni=="Y"):
    if(size=="S"):
        bill+=2
    else:
        bill+=3

if(extra_cheese=="Y"):
    bill+=1

print(f"Your final bill is: ${bill}.")

#Quinto Ejercicio
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()

T_count=name1.count("t") + name2.count("t")
R_count=name1.count("r") + name2.count("r")
U_count=name1.count("u") + name2.count("u")
E_count=name1.count("e") + name2.count("e")

L_count=name1.count("l") + name2.count("l")
O_count=name1.count("o") + name2.count("o")
V_count=name1.count("v") + name2.count("v")

second_digit=str(T_count+R_count+U_count+E_count)
first_digit=str(L_count+O_count+V_count+E_count)

percentage=second_digit+first_digit


if (int(percentage)<10 or int(percentage)>90):
    print(f"Your score is {percentage}, you go together like coke and mentos.")
elif(40<int(percentage) and int(percentage)<50):
    print(f"Your score is {percentage}, you are alright together.")
else:
    print(f"Your score is {percentage}.")
"""
#Proyecto Final
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
print("You wake up on a deserted island, you have to choose between building a boat or swim to for resourses \n")
first_answer=input("Write your answer. Build or swim? ")
if (first_answer.lower()=="build"):
    second_answer=input("You arrived on an island where there is a small civilization that is still looking for the treasure. Do you join them or continue on your own? Type Join or Continue ")
    if(second_answer.lower()=="continue"):
        print("You found an old map that shows three areas of the island where the treasure might be")
        third_aswer=input(" What area do you choose? Forest, Beach or Waterfall? ")
        if(third_aswer.lower()=="forest"):
            print("You chose the most obvious option, the forest is full of poisonous animals that do not hesitate to attack you. You lost the game")
        elif(third_aswer.lower()=="beach"):
            print("You thought like a pirate and you decided to look for the treasure on a beach, the townspeople thought that you were damaging their property, you lost the game")
        else:
            print("The waterfall is the option that sounds more dangerous, but when you arrive you realize that behind it is a cave with treasure. You won the game")
    else:
        print("The townspeople found an old map showing the location of the treasure. You chose to stay and live without the treasure. You lost the game")
else:
    print("You couldn't swim against the current, which made you return to the island tired. You lost the game")