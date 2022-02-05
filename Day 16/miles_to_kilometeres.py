from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text = "%.2f" %km)

window = Tk()
window.title("Miles to Km")
window.config(padx=20, pady=20)

#Miles Input
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#Miles Label
miles_label = Label(text="Miles", font=("Arial", 20))
miles_label.grid(column=2, row=0)

#Is Equal To Label
isequalto_label = Label(text="is equal to", font=("Arial", 20))
isequalto_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0", font=("Arial", 20))
kilometer_result_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()