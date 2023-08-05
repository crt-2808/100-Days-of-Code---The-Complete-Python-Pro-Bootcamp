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

"""
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