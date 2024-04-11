from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}

try:
    df=pandas.read_csv("./Dia31/data/words_to_learn.csv")
except FileNotFoundError:
    original_df=pandas.read_csv("./Dia31/data/french_words.csv")
    language_dic=original_df.to_dict(orient="records")
else:
    language_dic=df.to_dict(orient="records")
    


def is_known():
    language_dic.remove(current_card)
    data=pandas.DataFrame(language_dic)
    data.to_csv("./Dia31/data/words_to_learn.csv", index=False)
    new_word()


def new_word():
    global current_card, filp_timer
    window.after_cancel(filp_timer)
    current_card=random.choice(language_dic)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_image_front)
    filp_timer=window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_image_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")



window=Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
filp_timer=window.after(3000, func=flip_card)


card_image_front=PhotoImage(file="./Dia31/images/card_front.png")
card_image_back=PhotoImage(file="./Dia31/images/card_back.png")
accept_image=PhotoImage(file="./Dia31/images/right.png")
cancel_image=PhotoImage(file="./Dia31/images/wrong.png")

canvas=Canvas(width=800, height=526)
card_background=canvas.create_image(400, 263, image=card_image_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_title=canvas.create_text(400,150, text="", font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263, text="    ", font=("Ariel",60, "bold"))

accept_button=Button(image=accept_image, command=is_known)
accept_button.grid(column=1, row=1)
accept_button.config(highlightthickness=0, bg=BACKGROUND_COLOR)

unknown_button=Button(image=cancel_image, command=new_word)
unknown_button.grid(column=0, row=1)
unknown_button.config(highlightthickness=0, bg=BACKGROUND_COLOR)

new_word()
window.mainloop()