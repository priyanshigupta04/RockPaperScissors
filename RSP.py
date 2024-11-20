from tkinter import *
import random

win = 0
lose = 0

def rps(win, lose, user):
    computer = random.randrange(1, 4)
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    result = ""
    if user == computer:
        result = f"It's a draw.\nYou both chose {choices[user]}."
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        result = f"You chose {choices[user]}, I chose {choices[computer]}.\nYou win!"
        wins.set(wins.get() + 1)
    else:
        result = f"You chose {choices[user]}, I chose {choices[computer]}.\nYou lose!"
        loses.set(loses.get() + 1)
    var.set(result)

#The main window
top = Tk()
top.title("Rock Paper Scissors Game")
top.geometry("400x300")
top.configure(bg="#f7f7f7")

# Title Label
title = Label(top, text="Rock Paper Scissors", font=("Arial", 16, "bold"), bg="#f7f7f7", fg="#333")
title.pack(pady=10)

# Score Frame
score_frame = Frame(top, bg="#f7f7f7")
score_frame.pack(pady=10)
Label(score_frame, text="Wins:", font=("Arial", 12), bg="#f7f7f7").grid(row=0, column=0, padx=10)
wins = IntVar(value=win)
Label(score_frame, textvariable=wins, font=("Arial", 12), bg="#f7f7f7").grid(row=0, column=1, padx=10)
Label(score_frame, text="Losses:", font=("Arial", 12), bg="#f7f7f7").grid(row=0, column=2, padx=10)
loses = IntVar(value=lose)
Label(score_frame, textvariable=loses, font=("Arial", 12), bg="#f7f7f7").grid(row=0, column=3, padx=10)

# Buttons Frame
button_frame = Frame(top, bg="#f7f7f7")
button_frame.pack(pady=10)
Button(button_frame, text="Rock", font=("Arial", 12), command=lambda: rps(win, lose, 1), bg="#ffcccc", fg="#333").grid(row=0, column=0, padx=10, pady=5)
Button(button_frame, text="Paper", font=("Arial", 12), command=lambda: rps(win, lose, 2), bg="#ccffcc", fg="#333").grid(row=0, column=1, padx=10, pady=5)
Button(button_frame, text="Scissors", font=("Arial", 12), command=lambda: rps(win, lose, 3), bg="#ccccff", fg="#333").grid(row=0, column=2, padx=10, pady=5)

# Feedback Label
feedback_frame = Frame(top, bg="#f7f7f7")
feedback_frame.pack(pady=20)
var = StringVar(value="Make your move!")
Label(feedback_frame, textvariable=var, font=("Arial", 12), bg="#f7f7f7", wraplength=300, justify="center").pack()

# Exit Button
Button(top, text="Exit Game", font=("Arial", 12), command=top.quit, bg="#f08080", fg="#fff").pack(pady=10)

top.mainloop()
