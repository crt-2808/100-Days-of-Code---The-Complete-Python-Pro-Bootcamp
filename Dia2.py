"""
#Primer Ejercicio, conversion
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇
number1=int(two_digit_number[0])
number2=int(two_digit_number[1])

result=number1+number2
print(result)

#Tercer ejercico
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
age_numer=int(age)
years_left=90-age_numer
months_left=years_left*12
weeks_left=years_left*52
days_left=years_left*365
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

#Proyecto final
#Una calculadora que te pida el total a pagar de una cuenta, el porcentaje que se va a dejar de propina y
#Entre cuantas personas se va a dividir la cuenta
"""
print("Welcome to the tip calculator")
cuenta=input("What was the total bill? $")
cuenta_number=float(cuenta)
propina=input("What percentage tip would you like to give? 10, 12, or 15? ")
propina_number=float(propina)
personas_a_dividir=int(input("How many people to split the bill? "))

propina_number= 1+(propina_number/100)
cuenta_propina= (cuenta_number/personas_a_dividir) * propina_number
cuenta_dividida=round(cuenta_propina,2)
print(f"Each person should pay: ${cuenta_dividida}")