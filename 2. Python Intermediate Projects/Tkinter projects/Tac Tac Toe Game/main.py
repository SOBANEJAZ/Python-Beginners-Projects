from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("TIC TAC TOE GAME")

# Define dark colors for the UI
bg_color = "#222222"  # Dark background color
fg_color = "#FFFFFF"  # White text color

root.configure(bg=bg_color)

frame1 = Frame(root, bg=bg_color)
frame1.pack()
titlelabel = Label(
    frame1,
    text="Tic Tac Toe Game",
    font=("Arial", 30),
    bg=bg_color,
    fg=fg_color
)
titlelabel.pack()


frame2 = Frame(root, bg=bg_color)
frame2.pack()

# Modify the button style for the dark theme
button_style = {"width": 4, "height": 2, "font": ("Arial", 30), "bg": bg_color, "fg": fg_color}

board = {1: " ", 2: " ", 3: " ", 
         4: " ", 5: " ", 6: " ", 
         7: " ", 8: " ", 9: " "}

turn = "o"

def checkforwin(player):
    if (board[1] == board[2] == board[3] == player) and (board[1] != " "):
        return True
    elif (board[4] == board[5] == board[6] == player) and (board[4] != " "):
        return True
    elif (board[7] == board[8] == board[9] == player) and (board[7] != " "):
        return True
    elif (board[1] == board[4] == board[7] == player) and (board[1] != " "):
        return True
    elif (board[2] == board[5] == board[8] == player) and (board[2] != " "):
        return True
    elif (board[3] == board[6] == board[9] == player) and (board[3] != " "):
        return True
    elif (board[1] == board[5] == board[9] == player) and (board[1] != " "):
        return True
    elif (board[3] == board[5] == board[7] == player) and (board[3] != " "):
        return True
    else:
        return False


def play(event):
    global turn
    button = event.widget
    button_text = str(button)
    clicked = button_text[-1]
    if clicked == "n":
        clicked = "1"
    else:
        clicked = int(clicked)

    if button["text"] == " ":
        if turn == "o":
            button["text"] = "O"
            board[clicked] = turn
            if checkforwin(turn):
                print(f"{turn} won the game")
                print("GAME OVER")
            turn = "x"
        else:
            button["text"] = "X"
            board[clicked] = turn
            if checkforwin(turn):
                print(f"{turn} won the game")
                print("GAME OVER")
            turn = "o"


button1 = Button(frame2, text=" ", **button_style)
button1.grid(row=1, column=1)
button1.bind("<Button-1>", play)

button2 = Button(frame2, text=" ", **button_style)
button2.grid(row=1, column=2)
button2.bind("<Button-1>", play)

button3 = Button(frame2, text=" ", **button_style)
button3.grid(row=1, column=3)
button3.bind("<Button-1>", play)


button4 = Button(frame2, text=" ", **button_style)
button4.grid(row=2, column=1)
button4.bind("<Button-1>", play)

button5 = Button(frame2, text=" ", **button_style)
button5.grid(row=2, column=2)
button5.bind("<Button-1>", play)

button6 = Button(frame2, text=" ", **button_style)
button6.grid(row=2, column=3)
button6.bind("<Button-1>", play)


button7 = Button(frame2, text=" ", **button_style)
button7.grid(row=3, column=1)
button7.bind("<Button-1>", play)

button8 = Button(frame2, text=" ", **button_style)
button8.grid(row=3, column=2)
button8.bind("<Button-1>", play)

button9 = Button(frame2, text=" ", **button_style)
button9.grid(row=3, column=3)
button9.bind("<Button-1>", play)


root.mainloop()
