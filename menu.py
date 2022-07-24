import os
from tkinter import *
from turtle import bgcolor, color, window_width

def MiniMaxPressed():
    os.system('\"D:\\1. Files\\S6\\Mini Project\\minimax\\index.html"')

def TrainAIPressed():
    os.system('start cmd.exe')
    os.chdir('D:')
    os.chdir('D:\\1. Files\\S6\\Mini Project\\trainable')
    os.system('start cmd.exe /c \"npm start\"')

if __name__ == "__main__":
    ui = Tk()
    ui.title("Tic-Tac-Toe using AI")
    ui.config(bg = "white") 

    title1 = Label(ui, text = "Tic-Tac-Toe using AI", font = ("Constantia", 72), padx = 100, pady = 50, bg = "white")
    title2 = Label(ui, text = "S6 CSE Gamma Mini Project", font = ("Constantia", 24), bg = "white")
    title3 = Label(ui, text = "Karthik Variath\nShiyas Ahamed\nTushar Renji\nYadul Manoj", font = ("Constantia", 16), bg = "white", pady = 50)
    title1.grid(columnspan = 2)
    title2.grid(columnspan = 2)
    title3.grid(columnspan = 2)

    MinimaxButton = Button(ui, text = "MiniMax", width = 50, padx = 10, pady = 15, font = ("Constantia", 12, "bold"), bg = "red", fg = "white", activeforeground = "black", command = MiniMaxPressed)
    TrainAIButton = Button(ui, text = "Trainable AI", width = 50, padx = 10, pady = 15,font = ("Constantia", 12, "bold"), bg = "red", fg = "white", activeforeground = "black", command = TrainAIPressed)
    MinimaxButton.grid(row = 3, column = 0)
    TrainAIButton.grid(row = 3, column = 1)

    l = Label(ui, text = "", pady = 15)
    l.grid(columnspan = 2)
    
    ui.mainloop()