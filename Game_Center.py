#---------------------------------------
# EECE2140 Final Project: Game Cneter
#---------------------------------------

import tkinter as tk
from Twenty_One_Game import Twenty_One_Game
from tkinter import *
from Matching_Game import Matching_Game

class GameCenter:
    """GameCenter class, used for storing all necessary code to run the main window of program"""

    def __init__(self):
        """Method used to run setup() method for game automatically when new instance of class is created"""
        self.setup()

    def setup(self):
        """Method to create main game window and buttons for launching other games"""
        #Set up the main window
        mainWindow = tk.Tk()   #Initialize the window
        mainWindow.title("Game Hub")   #Set title

        #Set window position and dimension
        window_width = 600
        window_height = 500
        screen_width = mainWindow.winfo_screenwidth()
        screen_height = mainWindow.winfo_screenheight()
        window_x = int((screen_width - window_width) / 2)
        window_y = int((screen_height - window_height) / 2)
        #Set window to launch in center of the screen
        mainWindow.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')

        #Create tkinter canvas and make panel on the canvas where buttons will go
        canvas = tk.Canvas(mainWindow, bg = 'green', height = window_height, width = window_width)
        buttonPanel = canvas.create_rectangle(0, window_height*2/3, window_width, window_height, fill = 'light blue')

        #Make label with game title on canvas
        titleWidth = 25
        titleHeight = 3
        title = tk.Label(mainWindow, text = "Welcome to the Game Center!", font = ("Helvetica", 24, "bold"), width = titleWidth, height = titleHeight, bg = "green", fg = "orange")
        title.place(x = (window_width-titleWidth*7)/6, y = (window_height/3-titleHeight*7)/2)
        
        #Make buttons to go on canvas
        #virtualPixel = tk.PhotoImage(width = 1, height = 1)   #do this if want to define buttons in terms of pixels
        game1Button = tk.Button(mainWindow, text = "21", width = 10, height = 2, font = ("Arial", 13), command = lambda : Twenty_One_Game())   #width and height units are equal to width and height of character 0, respectively
        game1Button.place(x = window_width*2/10, y = window_height*4/5)

        game2Button = tk.Button(mainWindow, text = "Matching", width = 10, height = 2, font = ("Arial", 13), command = lambda : Matching_Game())
        game2Button.place(x = window_width*6/10, y = window_height*4/5)

        # game3Button = tk.Button(mainWindow, text = "Game 3", width = 10, height = 2, font = ("Arial", 13))
        # game3Button.place(x = window_width*7/10, y = window_height*4/5)
        
        canvas.pack()   #Load canvas into tkinter window
        mainWindow.mainloop()   #Keeps window open and running
