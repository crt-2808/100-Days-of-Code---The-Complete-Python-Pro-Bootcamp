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
"""


score=0
print("Your score is "+ score)  #Te arroja un TypeError ya que no se puede concatenar string con int 
#(se tiene que hacer el cast a string de la variable score con un str(score))