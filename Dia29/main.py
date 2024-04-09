from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyclip
import json

FONT=("Arial", 11)
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
    new_data={
        website:{
            "email": user,
            "password": password,
            }
        }

    if len(website)<1 or len(password)<1:
        messagebox.showerror(
            message="The website or password can not be empty"
            ,title="Error"
        )
    else:
        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email:{user} \n Password:{password} \n Is it ok to save?")
        if is_ok:
            try:
                with open("./Dia29/data.json", mode="r") as file:
                    data=json.load(file)
            except FileNotFoundError:
                with open("./Dia29/data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("./Dia29/data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
    
def handleSearch():
    site=website_entry.get()
    try:
        with open("./Dia29/data.json", mode="r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File Error",message="No Data File Found.")
    else:
        if site in data:
            password=data[site]["password"]
            email=data[site]["email"]
            messagebox.showinfo(
                message=f"Email: {email} \n Password: {password}",
                title=f"{site.capitalize()} Founded"
                )
        else:
            messagebox.showinfo(title="Error", message=f"No details for {site} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200, height=200)
logo=PhotoImage(file="./Dia29/logo.png")
canvas.create_image(100,100, image=logo)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

user_label=Label(text="Email/Username:", font=FONT)
user_label.grid(column=0, row=2)

password_label=Label(text="Password", font=FONT)
password_label.grid(column=0, row=3)

website_entry=Entry(font=FONT, width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

user_entry=Entry(font=FONT, width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(END, "example@mail.com") #End es una constante que representa el ultimo caracter

password_entry=Entry(font=FONT, width=21)
password_entry.grid(column=1, row=3)

generate_button=Button(text="Generate Password", command=randomPass, width=13)
generate_button.grid(column=2, row=3)

save_button=Button(text="Add", font=FONT, width=36, command=save)
save_button.grid(column=1, row=4, columnspan=2)

search_button=Button(text="Search", command=handleSearch, width=13)
search_button.grid(column=2, row=1)

window.mainloop()