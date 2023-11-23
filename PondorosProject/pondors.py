from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECONDS = 60
reps = 0
timer_intial = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_func():
    global reps
    window.after_cancel(timer_intial)
    #timer_text = 00
    canvas.itemconfig(timer_set, text="00:00")
    #timer_label = Timer.
    title_label.config(text="Timer")
    #Reset_checkmarks.
    reps = 0
    check_mark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_func():
    global reps
    reps+= 1

    work_sec = WORK_MIN * SECONDS
    show_break_sec = SHORT_BREAK_MIN * SECONDS
    long_break_sec = LONG_BREAK_MIN * SECONDS

    if reps == 8:
        title_label.config(text="Break", fg=RED)
        window_timer_counter(long_break_sec)
    elif reps % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        window_timer_counter(work_sec)
    else :
        title_label.config(text="Break", fg=PINK)
        window_timer_counter(show_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def window_timer_counter(count):
    # VISUAL COUNT TO 10:10
    mintues = math.floor(count / SECONDS)
    seconds = count % SECONDS
    if seconds < 10 :
        #Dynamic Typing.
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_set, text=f"{mintues}:{seconds}")
    if count > 0 :
        global timer_intial
        timer_intial = window.after(1000, window_timer_counter, count - 1)
    else:
        start_func()
        if reps%2 == 1:
            txt = "✔" * (reps/2)
            check_mark_label.config(text=txt)
            print(txt)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#TITLE_LABEL
title_label = Label(text="Timer", fg = GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(row=0,column=1)

#CHECKMARK.
check_mark_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_mark_label.grid(row=3,column=1)


#CANVAS + TEXT + IMAGE.
img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=img)
timer_set = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)


#BUTTONS.
start_button = Button(text="start",command=start_func ,highlightthickness=0, bd=2, width=6, relief="ridge")
start_button.grid(row=2,column=0)

reset_button = Button(text="reset",command=reset_func, highlightthickness=0, bd=2, width=6, relief="ridge")
reset_button.grid(row=2,column=2)


window.mainloop()

