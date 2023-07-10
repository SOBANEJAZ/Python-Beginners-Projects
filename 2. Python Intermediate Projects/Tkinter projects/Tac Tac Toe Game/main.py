from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("TIC TAC TOE GAME")

frame1 = Frame(root)
frame1.pack()
titlelabel = Label(
    frame1,
    text="Tic Tac Toe Game",
    font=("Arial", 30),
)
titlelabel.pack()


frame2 = Frame(root)
frame2.pack()

board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

turn = "o"

def checkforwin(player):
    if board[1] == board[2] == board[3] == player:
        return True
    elif board[4] == board[5] == board[6] == player:
        return True
    elif board[7] == board[8] == board[9] == player:
        return True
    elif board[1] == board[4] == board[7] == player:
        return True
    elif board[2] == board[5] == board[8] == player:
        return True
    elif board[3] == board[6] == board[9] == player:
        return True
    elif board[1] == board[5] == board[9] == player:
        return True
    elif board[3] == board[5] == board[7] == player:
        return True
    else:
        return False


def play(event):
    global turn
    Button = event.widget
    buttontext = str(Button)
    clicked = buttontext[-1]
    if clicked == "n" :
        clicked = "1"
    else:
        clicked = int(clicked)

    if Button["text"] == " ":
        if turn == "o":
            Button["text"] = "O"
            board[clicked] = turn
            if checkforwin(turn) == True:
                print(f"{turn} won the game")
                print("GAMEOVER")
            turn = "x"
        else:
            Button["text"] = "X"
            board[clicked] = turn
            if checkforwin(turn) == True:
                print(f"{turn} won the game")
                print("GAMEOVER")
            turn = "o"
    



button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button1.grid(row=1, column=1)
button1.bind("<Button-1>", play)

button2 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button2.grid(row=1, column=2)
button2.bind("<Button-1>", play)

button3 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button3.grid(row=1, column=3)
button3.bind("<Button-1>", play)


button4 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button4.grid(row=2, column=1)
button4.bind("<Button-1>", play)

button5 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button5.grid(row=2, column=2)
button5.bind("<Button-1>", play)

button6 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button6.grid(row=2, column=3)
button6.bind("<Button-1>", play)


button7 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button7.grid(row=3, column=1)
button7.bind("<Button-1>", play)

button8 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button8.grid(row=3, column=2)
button8.bind("<Button-1>", play)
button9 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button9.grid(row=3, column=3)
button9.bind("<Button-1>", play)


root.mainloop()
