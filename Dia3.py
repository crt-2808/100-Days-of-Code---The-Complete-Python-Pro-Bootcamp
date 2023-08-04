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
