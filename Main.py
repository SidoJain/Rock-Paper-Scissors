import tkinter as tk
from random import randint
from tkinter import PhotoImage

window = tk.Tk()
window.title("Rock Paper Scissors")
window.config(background="black")
window.resizable(False, False)

blank_image1 = PhotoImage(file="Blank.png")
rock_image1 = PhotoImage(file="Rock.png")
paper_image1 = PhotoImage(file="Paper.png")
scissors_image1 = PhotoImage(file="Scissors.png")

blank_image2 = blank_image1.subsample(2, 2)
rock_image2 = rock_image1.subsample(2, 2)
paper_image2 = paper_image1.subsample(2, 2)
scissors_image2 = scissors_image1.subsample(2, 2)

label_player = tk.Label(window, image=blank_image2)
label_computer = tk.Label(window, image=blank_image2)
label_player.grid(row=2, column=1)
label_computer.grid(row=2, column=3)

player_score = tk.Label(window, font=("arial", 20, "bold"), text=0,
                        bg="black", fg="green")
draw_score = tk.Label(window, font=("arial", 20, "bold"), text=0,
                        bg="black", fg="green")
computer_score = tk.Label(window, font=("arial", 20, "bold"), text=0,
                        bg="black", fg="green")
player_score.grid(row=3, column=1)
draw_score.grid(row=3, column=2)
computer_score.grid(row=3, column=3)

player = tk.Label(window, font=("arial", 20, "bold"), text="Player",
                bg="black", fg="orange").grid(row=1, column=1)
computer = tk.Label(window, font=("arial", 20, "bold"), text="Computer",
                bg="black", fg="orange").grid(row=1, column=3)

message = tk.Label(window, font=("arial", 20, "bold"), bg="black", fg="white", text="")
message.grid(row=2, column=2)

def Msg_Updation(text):
    message['text'] = text

def Draw_Update():
    score = int(draw_score['text'])
    score += 1
    draw_score['text'] = str(score)

def Computer_Update():
    score = int(computer_score['text'])
    score += 1
    computer_score['text'] = str(score)

def Player_Update():
    score = int(player_score['text'])
    score += 1
    player_score['text'] = str(score)

def Winner_Check(p, c):
    if p == c:
        Msg_Updation("It's a Draw!")
        Draw_Update()
    elif p == (c + 1) % 3:
        Msg_Updation("Player Wins!")
        Player_Update()
    else:
        Msg_Updation("Computer Wins!")
        Computer_Update()

def Move_Update(player_move):
    computer_move = randint(0, 2)
    if computer_move == 0:
        label_computer['image'] = rock_image2
    elif computer_move == 1:
        label_computer['image'] = paper_image2
    elif computer_move == 2:
        label_computer['image'] = scissors_image2

    if player_move == 0:
        label_player['image'] = rock_image2
    elif player_move == 1:
        label_player['image'] = paper_image2
    elif player_move == 2:
        label_player['image'] = scissors_image2

    Winner_Check(player_move, computer_move)

rock_button = tk.Button(window, width=240, height=240, image=rock_image1,
                        font=("arial", 20, "bold"), bg="black", fg="red",
                        command= lambda: Move_Update(0)).grid(row=4, column=1)
paper_button = tk.Button(window, width=240, height=240, image=paper_image1,
                        font=("arial", 20, "bold"), bg="black", fg="red",
                        command= lambda: Move_Update(1)).grid(row=4, column=2)
scissors_button = tk.Button(window, width=240, height=240, image=scissors_image1,
                        font=("arial", 20, "bold"), bg="black", fg="red",
                        command= lambda: Move_Update(2)).grid(row=4, column=3)

window.mainloop()