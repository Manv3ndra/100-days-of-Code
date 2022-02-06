from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

BLACK = "#000000"
WHITE = "#FFFFFF"
FONT = ("Courier", 15, "bold")
# Password Generator
def generate_password():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

# Save Password
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if (len(website)==0 or len(email)==0 or len(password)==0):
        messagebox.showwarning(title="Error", message="Please do not leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?")

        if is_ok:
            with open("data.txt", mode = "a") as f:
                f.write(f"\n{website} | {email} | {password}")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# UI Setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=300, height=300, bg=WHITE, highlightthickness=0)
lock_image = PhotoImage(file="lock.png")
canvas.create_image(150, 150, image=lock_image)
canvas.grid(column=1, row=0)
#Labels
website_label = Label(text="Website:", fg=BLACK, background=WHITE)
website_label.grid(column=0,row=1)

username_label = Label(text="Email/Username:", fg=BLACK, background=WHITE)
username_label.grid(column=0,row=2)

password_label = Label(text="Password:", fg=BLACK, background=WHITE)
password_label.grid(column=0,row=3)
#Entries
website_entry = Entry(width=45)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=45)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(END,"manvendra@email.com")

password_entry = Entry(width=27)
password_entry.grid(column=1,row=3)
#Buttons
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2,row=3)

add_button = Button(text="Add",width=39,command=save_password)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()