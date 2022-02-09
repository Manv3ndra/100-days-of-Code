import os
import json
from tkinter import *
import random
import pandas

os.chdir("D:/My Stuff/100 Days of Code/Day 20")

BACKGROUND_COLOR = "#29D7B0"

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("word_data/words_to_learn.csv")
except FileNotFoundError:
    og_data = pandas.read_csv("word_data/french_words.csv")
    to_learn = og_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(card_image, image = card_front)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_image, image = card_back)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("word_data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=745, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="card_images/card_front.png")
card_back = PhotoImage(file="card_images/card_back.png")
card_image = canvas.create_image(372,263,image=card_front)
card_title = canvas.create_text(372, 120, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(372, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2, pady=20)

cross = PhotoImage(file="card_images/wrong.png")
correct_button = Button(image=cross, height=100, width=100, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=next_card)
correct_button.grid(row=1, column=0)

check = PhotoImage(file="card_images/right.png")
correct_button = Button(image=check, height=100, width=100, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=is_known)
correct_button.grid(row=1, column=1)

next_card()

window.mainloop()