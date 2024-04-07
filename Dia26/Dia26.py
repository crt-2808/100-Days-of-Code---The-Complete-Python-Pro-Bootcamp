'''
#new_list=[new_item for itemn in list if condition]

#List Comprenhension
numbers=[1,2,3,4,5]
new_numbers=[ number +1 for number in numbers]
print(new_numbers)

#Trabajar en un string
name="Cristian"
letter_list=[letter for letter in name]
print(letter_list)

#Range como lista
range_list=[num *2 for num in range(1,5)]
print(range_list)

#Condicionales
names=["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names=[name.upper() for name in names if len(name)<5]
print(short_names)

#Ejercico 1: Crea una nueva lista donde los elementos sean los numeros de la lista numbers al cuadrado
numbers=[1,2,3,4,5,6]
squared_numbers=[(num*num) for num in numbers]
print(squared_numbers)

#Ejercicio 2: Recorre una lista de string con numeros y regresa los pares
list_of_strings=input().split(",")
result=[int(number) for number in list_of_strings if int(number)%2 == 0]

print(result)
'''
with open("./Dia26/text1.txt") as list1:
    file1=list1.readlines()

with open("./Dia26/text2.txt") as list2:
    file2=list2.readlines()

result=[int(num) for num in file1 if num in file2]
print(result)