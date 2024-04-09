from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyclip

FONT=("Arial", 11)
RUTA="C:/Users/ramos/OneDrive/Documentos/Udemy/100-Days-of-Code---The-Complete-Python-Pro-Bootcamp/Dia29/data.txt"
LOGO="C:/Users/ramos/OneDrive/Documentos/Udemy/100-Days-of-Code---The-Complete-Python-Pro-Bootcamp/Dia29/logo.png"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def randomPass():
    password_entry.delete(0, END)
    letter_pass=[ choice(letters) for _ in range(randint(8,10))]
    symbols_pass=[ choice(symbols) for _ in range(randint(2,4))]
    number_pass=[ choice(numbers) for _ in range(randint(2,4))]
    password_list=letter_pass+symbols_pass+number_pass
    shuffle(password_list)
    password="".join(password_list)
    pyclip.copy(password)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    user=user_entry.get()
    password=password_entry.get()

    if len(website)<1 or len(password)<1:
        messagebox.showerror(
            message="The website or password can not be empty"
            ,title="Error"
        )
    else:
        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email:{user} \n Password:{password} \n Is it ok to save?")
        if is_ok:
            with open(RUTA, mode="a") as file:
                file.write(f"{website} | {user} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200, height=200)
logo=PhotoImage(file=LOGO)
canvas.create_image(100,100, image=logo)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

user_label=Label(text="Email/Username:", font=FONT)
user_label.grid(column=0, row=2)

password_label=Label(text="Password", font=FONT)
password_label.grid(column=0, row=3)

website_entry=Entry(font=FONT, width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_entry=Entry(font=FONT, width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(END, "example@mail.com") #End es una constante que representa el ultimo caracter

password_entry=Entry(font=FONT, width=21)
password_entry.grid(column=1, row=3)

generate_button=Button(text="Generate Password", command=randomPass)
generate_button.grid(column=2, row=3)

save_button=Button(text="Add", font=FONT, width=36, command=save)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()