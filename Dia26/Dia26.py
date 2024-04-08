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

with open("./Dia26/text1.txt") as list1:
    file1=list1.readlines()

with open("./Dia26/text2.txt") as list2:
    file2=list2.readlines()

result=[int(num) for num in file1 if num in file2]
print(result)

#Diccionarios
import random
names=["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score={name:random.randint(0,100) for name in names}
print(students_score)
passed_students={name:score for (name,score) in students_score.items() if score>=60}
print(passed_students)

#Ejercicio1: Recibe una oracion, y regresa un diccionario con las palabras de la oracion y su longitud
sentence=input()
sentence_word=sentence.split()
sentence_length={word:len(word) for (word) in sentence_word }
print(sentence_length)

#Ejercicio2: Recibe un diccionario y regresa un diccionario con las temperaturas en °F
weather_c=eval(input()) #eval regresa en formato correcto el diccionario
weather_f={day:((temp*(9/5))+32) for (day, temp) in weather_c.items()}
print(weather_f)

import pandas
student_dict={
    "student":["Angela","Cris","Ale"],
    "score":[5,6,7]
}
student_dataframe=pandas.DataFrame(student_dict)

for (index, row) in student_dataframe.iterrows():
    if row.student=="Angela":
        print(row.score)
'''
import pandas
df=pandas.read_csv("./Dia26/nato_phonetic_alphabet.csv")

phonetic_dict= {row.letter:row.code for (index, row) in df.iterrows()}
word=input("Type the word you want: ").upper()
output_list=[phonetic_dict[letter] for letter in word]

print(output_list)