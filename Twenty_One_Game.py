#---------------------------
# 21 game for Game Center
#---------------------------

import tkinter as tk

class Twenty_One_Game():
    """Class used to store all code to run Twenty-One Game"""

    def __init__(self):
        """Method used to run setup() method for game automatically when new instance created"""
        self.setup()
    
    def setup(self):
        """Method used to create window for game and center window on screen"""
        self.count = 0
        self.numclicks = 0

        #Set up the main window
        self.gameWindow = tk.Tk()   #Initialize the window
        self.gameWindow.title("21 Game")   #Set title

        #Set window position and dimension
        window_width = 600
        window_height = 500
        screen_width = self.gameWindow.winfo_screenwidth()
        screen_height = self.gameWindow.winfo_screenheight()
        window_x = int((screen_width - window_width) / 2)
        window_y = int((screen_height - window_height) / 2)
        #Set the window to launch in the center of the screen
        self.gameWindow.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')

        self.play(window_height, window_width)

    def play(self, window_height, window_width):
        """Method used to load all text and buttons onto tkinter canvas, and play game
        :param window_height: int for height of tkinter window
        :param window_width: int for width of tkinter window"""
        #Make tkinter canvas
        canvas = tk.Canvas(self.gameWindow, bg = 'light blue', height = window_height, width = window_width)
        tallyPanel = canvas.create_rectangle(0, window_height * 2/3, window_width, window_height, fill = 'gray')

        #Make label with game title on canvas
        titleWidth = 20   #Width of window in terms of 8 is 85 (85 zeros wide)
        titleHeight = 2
        title = tk.Label(self.gameWindow, text = "21 Game", font = ("Calibri", 20), bg = "light blue", width = titleWidth, height = titleHeight)
        title.place(x = 155, y = 10)

        #Make label with game instructions
        inst_Width = 40
        inst_Height = 4
        instructions = tk.Label(self.gameWindow, text = "Take turns clicking buttons, \n don't be the player who hits 21!", font = ("Calibri", 12), bg = "light blue", width = inst_Width, height = inst_Height)
        instructions.place(x = 140, y = 60)

        #Make buttons for increasing count
        plusOne = tk.Button(self.gameWindow, text = "+1", width = 10, height = 2, font = ("Arial", 12), command = lambda : self.updateCountOne(self.count))
        plusTwo = tk.Button(self.gameWindow, text = "+2", width = 10, height = 2, font = ("Arial", 12), command = lambda : self.updateCountTwo(self.count))
        plusThree = tk.Button(self.gameWindow, text = "+3", width = 10, height = 2, font = ("Arial", 12), command = lambda : self.updateCountThree(self.count))

        #Place buttons on canvas
        plusOne.place(x = window_width/10, y = window_height*4/5)
        plusTwo.place(x = window_width*4/10, y = window_height*4/5)
        plusThree.place(x = window_width*7/10, y = window_height*4/5)

        self.display_count(self.count)
        canvas.pack()
        self.gameWindow.mainloop()

    def display_count(self, count):
        """Method used to display running count during game
        :param count: int for current tally in game"""
        text_label = tk.Label(self.gameWindow, text = "The current count is:", font = ("Arial", 12), bg = "light blue", width = 20, height = 2)
        text_label.place(x = 205, y = 150)
        count_label = tk.Label(self.gameWindow, text = count, font = ("Arial", 16), bg = "light blue", width = 15, height = 2)
        count_label.place(x = 205, y = 180)
        self.checkWin(self.count)

    def updateCountOne(self, count):
        """Method used to update the count of the game by 1 when button 1 is pressed"""
        self.count = count + 1
        self.numclicks += 1
        self.display_count(self.count)
    
    def updateCountTwo(self, count):
        """Method used to update the count of the game by 2 when button 2 is pressed"""
        self.count = count + 2
        self.numclicks += 1
        self.display_count(self.count)
    
    def updateCountThree(self, count):
        """Method used to update the count of the game by 3 when button 3 is pressed"""
        self.count = count + 3
        self.numclicks += 1
        self.display_count(self.count)
    
    def checkWin(self, count):
        """Method for continually checking if count has reached 21
        :param count: int for current tally in game, game over when hits 2"""
        if count >= 21:
            playerLose = "Player", self.numclicks % 2 + 1, "Lost!"
            showLose = tk.Label(self.gameWindow, text = playerLose, font = ("Arial", 16), bg = "red")
            showLose.place(x = 230, y = 250)
