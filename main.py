from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 0.125
LONG_BREAK_MIN = 0.25
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)

    # reset timer text
    canvas.itemconfig(text_timer, text=f"00:00")
    reps = 0

    # reset label to timer
    timer_text.config(text="timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)

    # reset the tick symbols
    tick_symbol.config(text="", bg=YELLOW, font=(FONT_NAME, 20, "bold"))


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    # converting minutes into seconds
    work_countsec = int(WORK_MIN * 60)
    short_countsec = int(SHORT_BREAK_MIN * 60)
    long_countsec = int(LONG_BREAK_MIN * 60)

    # setting text to work
    if reps % 2 != 0:
        timer_text.config(text="WORK", fg=RED, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
        countdown(work_countsec)

    # setting text to long break and resetting check symbol
    elif reps == 8:
        reps = 0
        timer_text.config(text="LONG BREAK", fg=PINK, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
        tick_symbol.config(text="", bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        countdown(long_countsec)

    # setting text to short break
    else:
        timer_text.config(text="SHORT BREAK", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
        countdown(short_countsec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    # getting minutes and seconds values
    count_min = f"0{math.floor(count / 60)}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # displaying timer text
    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    # setting up the check symbol
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(reps / 2)):
            mark += "✔"
        tick_symbol.config(text=mark, bg=YELLOW, font=(FONT_NAME, 20, "bold"))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

# text,image,background,etc
canvas = Canvas(width=205, height=234, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(103, 113, image=img)
text_timer = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# timer text
timer_text = Label(text="timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer_text.grid(row=0, column=1)

# start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

# reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

# check symbol
tick_symbol = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
tick_symbol.grid(row=3, column=1)

window.mainloop()
