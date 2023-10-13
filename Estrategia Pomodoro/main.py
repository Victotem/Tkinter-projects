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
reps = 0
timer= None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    
    window.after_cancel(timer)
    global reps 
    reps = 0
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    tick.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    if reps % 2 ==1:
        count_down(WORK_MIN * 60)
        title.config(text="Work", fg=GREEN)
    elif reps % 2 == 0 and reps != 8:
        count_down(SHORT_BREAK_MIN * 60)
        title.config(text="Short break", fg=RED)
    elif reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        title.config(text="Long break", fg=PINK)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count /60)
    count_sec = count % 60
    if count_sec <10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    elif count == 0:
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        tick.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



title = Label(text="Timer", font=(FONT_NAME,28,"bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_png=PhotoImage(file="tomato.png")
canvas.create_image(100, 112,image=tomato_png)
canvas.grid(column=1, row=2)
timer_text = canvas.create_text(100,130, text="00:00",fill="white", font=(FONT_NAME, 35, "bold"))

button1=Button(text="Start",highlightthickness=0, command= start_timer)
button1.grid(column=0, row=3)

button2=Button(text="Reset", highlightthickness=0, command=reset_timer)
button2.grid(column=2, row=3)

tick = Label(text="", font=(FONT_NAME,12,"bold"), fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=4)


window.mainloop()