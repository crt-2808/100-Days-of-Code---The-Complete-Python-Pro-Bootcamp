#with open("C:/Users/ramos/OneDrive/Documentos/Udemy/100-Days-of-Code---The-Complete-Python-Pro-Bootcamp/Dia25/weather_data.csv") as weather:
#    data=weather.readlines()

#import csv
#
#with open("C:/Users/ramos/OneDrive/Documentos/Udemy/100-Days-of-Code---The-Complete-Python-Pro-Bootcamp/Dia25/weather_data.csv") as data_file:
#    data=csv.reader(data_file)
#    temperature=[]
#    for row in data:
#        if row[1] != "temp":
#            temperature.append(int(row[1]))
#    print(temperature)

import pandas
#RUTA="C:/Users/ramos/OneDrive/Documentos/Udemy/100-Days-of-Code---The-Complete-Python-Pro-Bootcamp/Dia25/weather_data.csv"
#data=pandas.read_csv(RUTA)
#data_dict=data.to_dict()
#
#
#temp_list=data["temp"].to_list()
#
##print(data["temp"].max())
#
##Data en columnas
##print(data.temp)
##print(data["temp"])
#
##Data de una fila
##print(data[data.temp == data.temp.max()])
#monday=data[data.day=="Monday"]
#print(monday.temp)
#
#monday_fahrenheit=(monday.temp[0]*(9/5))+32
#print(monday_fahrenheit)



#data_dict={
#    "students":["Amy", "James", "Angela"],
#    "scores":[76,65,65]
#}

#data=pandas.DataFrame(data_dict)
#data.to_csv("./Dia25/new_data.csv")


data=pandas.read_csv("./Dia25/dataframe.csv")
counts=data["Primary Fur Color"].value_counts()
print(counts)
csv_file=pandas.DataFrame(counts)
csv_file.to_csv("./Dia25/info.csv")