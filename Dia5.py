"""
#Ejercicio1: Recibe un arrego de longitud n y regresa el promedio de esos numeros
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
heights_sum=0
for i in range (len(student_heights)):
    heights_sum=heights_sum+student_heights[i]
height_prom=heights_sum/len(student_heights)
height_prom=round(height_prom)
print(height_prom)

#Ejercicio2: Recibe un arreglo de longitud n y regresa el elemento más alto
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
max_score=0
for score in range(0,len(student_scores)):
    if student_scores[score]>max_score:
        max_score=student_scores[score]

print(f"The highest score in the class is: {max_score}")

#Ejercicio3: Suma de numeros pares
#Write your code below this row 👇
even_sum=0
for i in range(0,102,2):
    even_sum=even_sum+i
print(even_sum)

#Ejercicio4: Fizz Buzz ENTREVISTA
#Write your code below this row 👇
for i in range(1,101):
  if(i%3==0 and i%5==0):
    print("FizzBuzz")
  elif(i%3==0):
    print("Fizz")
  elif(i%5==0):
    print("Buzz")
  else:
    print(f"{i}")

"""
#Generador de contraseñas
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for char in range(1, nr_letters+1):
  password+=random.choice(letters)
  
for char in range(1, nr_symbols+1):
  password+=random.choice(symbols)
  
for char in range(1, nr_numbers+1):
  password+=random.choice(numbers)


print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_hard=[]
for char in range(1, nr_letters+1):
  password_hard.append(random.choice(letters))
  
for char in range(1, nr_symbols+1):
  password_hard.append(random.choice(symbols))
  
for char in range(1, nr_numbers+1):
  password_hard.append(random.choice(numbers))

random.shuffle(password_hard)

password_hard_final=''
for i in password_hard:
  password_hard_final+=i
  
print(password_hard_final)

