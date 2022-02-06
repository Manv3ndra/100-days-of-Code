import math
from tkinter import *

#Constants
BLUE = "#041562"
RED = "#da1212"
GREEN = "#3e8e7e"
YELLOW = "#f9e4d4"
BLACK = "#000000"
FONT_NAME = ("Courier", 35, "bold")
FONT_CHECK = ("Courier", 10, "bold")
FONT_BUTTON = ("Courier", 15, "bold")
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 20
reps = 0
timer = None

#Timer Reset
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")

#Timer Mechanism
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK * 60
    
    if reps % 2 != 0:
        countdown(work_sec)
        timer_label.config(text="Work", fg=RED)
    if reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Short Break", fg=GREEN)
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Long Break", fg=BLUE)

#Countdown Mechanism
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        for i in range(math.floor(reps/2)):
            marks += "✅"
        check_marks.config(text=marks)



#UI Setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=FONT_NAME, background=YELLOW, fg=BLACK)
timer_label.pack()

canvas = Canvas(width=364, height=378, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(182, 189, image=tomato_image)
timer_text = canvas.create_text(182, 220, text="00:00", fill="white", font=FONT_NAME)
canvas.pack()

start_button = Button(text="Start", highlightthickness=0, font=FONT_BUTTON, command=start_timer)
start_button.pack(side="left")

reset_button = Button(text="Reset", highlightthickness=0, font=FONT_BUTTON, command=reset)
reset_button.pack(side="right")

check_marks = Label(fg=BLACK, bg=YELLOW, font=FONT_CHECK, pady=15)
check_marks.pack()

window.mainloop()