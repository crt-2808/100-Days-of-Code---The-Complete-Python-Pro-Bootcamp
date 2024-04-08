from tkinter import *

#Creacion de la pantalla
window=Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)
#Cuando creas componentes, primero los defines y despues usas pack para mostrarlos
#Label
my_label=Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Formas de cambiar el texto
#my_label["text"]="New Text"
#my_label.config(text="New Text")

def button_clicked():
    inputtext=input_text.get()
    my_label.config(text=inputtext)
    print("I got clicked")

my_button=Button(text="Click me", command=button_clicked)
my_button.grid(column=1, row=1)

new_button=Button(text="New")
new_button.grid(column=3, row=0)

input_text=Entry(width=10)
print(input_text.get())
input_text.grid(column=4, row=3)


window.mainloop()