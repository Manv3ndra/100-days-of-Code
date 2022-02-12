from cgitb import text
from tkinter import *
import os
import requests

os.chdir("D:/My Stuff/100 Days of Code/Day 22")

def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text = quote)

window = Tk()
window.title("Kanye Says")
window.config(padx=50, pady=50)

canvas = Canvas(width=434, height=550)
text_box = PhotoImage(file="Kanye Quotes/text_box.png")
canvas.create_image(217,275,image=text_box)
quote_text = canvas.create_text(217, 225, text = "Kanye Quote goes here", width=370, font = ("Arial", 24,"bold"), fill="black")
canvas.grid(row=0,column=0)

kanye_img = PhotoImage(file="Kanye Quotes/kanye.png")
button = Button(image=kanye_img,highlightthickness=0, command=get_quote, borderwidth=0)
button.grid(row=1,column=0)

window.mainloop()