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

turn = "o"


def play(event):
    global turn
    Button = event.widget
    if turn == "o":
        Button["text"] = "O"
        turn = "x"
    else:
        Button["text"] = "X"
        turn = "o"


button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button1.grid(row=1, column=1)
button1.bind("<Button-1>", play)

button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button1.grid(row=1, column=2)
button1.bind("<Button-1>", play)

button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button1.grid(row=1, column=3)
button1.bind("<Button-1>", play)


button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button1.grid(row=2, column=1)
button1.bind("<Button-1>", play)

button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button1.grid(row=2, column=2)
button1.bind("<Button-1>", play)

button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button1.grid(row=2, column=3)
button1.bind("<Button-1>", play)


button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button1.grid(row=3, column=1)
button1.bind("<Button-1>", play)

button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button1.grid(row=3, column=2)
button1.bind("<Button-1>", play)

button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30))
button1.grid(row=3, column=3)
button1.bind("<Button-1>", play)


root.mainloop()
