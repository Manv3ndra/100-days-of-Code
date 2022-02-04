import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

#labels in the window
my_label = tkinter.Label(text="I am a label", font=("Arial", 20, "bold"))
my_label.pack()

#Buttons
def button_clicked():
    new_text = tkinter_input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

#Entry
tkinter_input = tkinter.Entry(width=10)
tkinter_input.pack(pady=10)

#Text
textbox_text = tkinter.Text(height=5, width=30)
textbox_text.focus()
textbox_text.insert(tkinter.END,"Example of text box in tkinter")
print(textbox_text.get("1.0", tkinter.END))
textbox_text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0, to=10, width=2, command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbox
def checkbox_used():
    print(checked_state.get())
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On", variable=checked_state, command=checkbox_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Mango", "Pear", "Grapes"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()