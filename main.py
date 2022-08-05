from tkinter import *
import math

# # COLOR CODES
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Time New Roman"
WORK_MIN = 25
BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
checkmark_list = ""
CHECKMARK = "✅"
timer = "None"


def start():
    global reps
    work_sec = WORK_MIN * 60
    work_break = BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label.config(text="Time to relax!", foreground=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        label.config(text="Time to take a quick break!", foreground=PINK)
        count_down(work_break)
    else:
        label.config(text="Time to work!", foreground=GREEN)
        count_down(work_sec)
    reps += 1


def reset():
    global reps
    global timer
    global checkmark_list
    window.after_cancel(timer)
    reps = 1
    checkmark.config(text="")
    label.config(text="Pomodoro Timer", foreground=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


def count_down(count):
    global reps
    global checkmark_list
    global CHECKMARK
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10 or count_min < 10:
        if count_sec < 10:
            count_sec = "0" + str(count_sec)
        if count_min < 10:
            count_min = "0" + str(count_min)
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 0:
            print("here")
            checkmark_list = CHECKMARK + checkmark_list
            checkmark.config(text=checkmark_list)
            print(checkmark_list)
        start()


# # UI SETUP
window = Tk()
window.config(padx=100, pady=50, background=YELLOW)
window.title("Pomodoro App v1.0")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Pomodoro Timer", font=(FONT_NAME, 20, "bold"), foreground=GREEN, background=YELLOW)
label.grid(column=1, row=0)

button1 = Button(text="Start", command=start, font=(FONT_NAME, 15, "bold"), background=GREEN)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", command=reset, font=(FONT_NAME, 15, "bold"), background=RED)
button2.grid(column=2, row=2)

checkmark = Label(text=checkmark_list, font=(FONT_NAME, 20, "bold"), background=YELLOW, foreground=GREEN)
checkmark.grid(row=3, column=1)
window.mainloop()
