from tkinter import *

FONT=("Arial", 24, "bold")

window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=50, pady=33)

label1=Label(text="is equal to", font=FONT)
label1.grid(column=1, row=2)

input_entry=Entry(font=FONT, width=7)
input_entry.grid(column=2, row=1)

label2=Label(text="0", font=FONT)
label2.grid(column=2, row=2)

def change_to_KM():
    double_input=float(input_entry.get())
    result=double_input*1.609
    label2.config(text=result)

button=Button(text="Calculate", command=change_to_KM)
button.grid(column=2, row=3)

label3=Label(text="Km", font=FONT)
label3.grid(column=3, row=2)

label4=Label(text="Miles", font=FONT)
label4.grid(column=3, row=1)


window.mainloop()