#-------------------------------------
# Full Game Center Application Code
#-------------------------------------

import tkinter as tk
from tkinter import *
from graphics import *
import random as r
import math as m

def main():
    """Method to run Game Center application, purpose is to keep source code hidden from user"""
    GameCenter()

main()

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
        game1Button.place(x = window_width*1/10, y = window_height*4/5)

        game2Button = tk.Button(mainWindow, text = "Matching", width = 10, height = 2, font = ("Arial", 13), command = lambda : Matching_Game())
        game2Button.place(x = window_width*4/10, y = window_height*4/5)

        game3Button = tk.Button(mainWindow, text = "Checkers", width = 10, height = 2, font = ("Arial", 13), command = lambda : Checkers())
        game3Button.place(x = window_width*7/10, y = window_height*4/5)
        
        canvas.pack()   #Load canvas into tkinter window
        mainWindow.mainloop()   #Keeps window open and running

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
        gameWindow = tk.Tk()   #Initialize the window
        gameWindow.title("21 Game")   #Set title

        #Set window position and dimension
        window_width = 600
        window_height = 500
        screen_width = gameWindow.winfo_screenwidth()
        screen_height = gameWindow.winfo_screenheight()
        window_x = int((screen_width - window_width) / 2)
        window_y = int((screen_height - window_height) / 2)
        #Set the window to launch in the center of the screen
        gameWindow.geometry(f'{window_width}x{window_height}+{window_x}+{window_y}')

        self.play(gameWindow, window_height, window_width)

    def play(self, gameWindow, window_height, window_width):
        """Method used to load all text and buttons onto tkinter canvas, and play game
        :param GameWindow: tkinter window of game, referenced when placing tkinter objects
        :param window_height: int for height of tkinter window
        :param window_width: int for width of tkinter window"""
        #Make tkinter canvas
        canvas = tk.Canvas(gameWindow, bg = 'light blue', height = window_height, width = window_width)
        tallyPanel = canvas.create_rectangle(0, window_height * 2/3, window_width, window_height, fill = 'gray')

        #Make label with game title on canvas
        titleWidth = 20   #Width of window in terms of 8 is 85 (85 zeros wide)
        titleHeight = 2
        title = tk.Label(gameWindow, text = "21 Game", font = ("Calibri", 20), bg = "light blue", width = titleWidth, height = titleHeight)
        title.place(x = 155, y = 10)

        #Make label with game instructions
        inst_Width = 40
        inst_Height = 4
        instructions = tk.Label(gameWindow, text = "Take turns clicking buttons, \n don't be the player who hits 21!", font = ("Calibri", 12), bg = "light blue", width = inst_Width, height = inst_Height)
        instructions.place(x = 140, y = 60)

        #Make buttons for increasing count
        plusOne = tk.Button(gameWindow, text = "+1", width = 10, height = 2, font = ("Arial", 12), command = lambda : self.updateCountOne(gameWindow, self.count))
        plusTwo = tk.Button(gameWindow, text = "+2", width = 10, height = 2, font = ("Arial", 12), command = lambda : self.updateCountTwo(gameWindow, self.count))
        plusThree = tk.Button(gameWindow, text = "+3", width = 10, height = 2, font = ("Arial", 12), command = lambda : self.updateCountThree(gameWindow, self.count))

        #Place buttons on canvas
        plusOne.place(x = window_width/10, y = window_height*4/5)
        plusTwo.place(x = window_width*4/10, y = window_height*4/5)
        plusThree.place(x = window_width*7/10, y = window_height*4/5)

        self.display_count(gameWindow, self.count)

        canvas.pack()
        gameWindow.mainloop()

    def display_count(self, gameWindow, count):
        """Method used to display running count during game
        :param gameWindow: tkinter window for game, referenced when placing tkinter objects
        :param count: int for current tally in game"""
        text_label = tk.Label(gameWindow, text = "The current count is:", font = ("Arial", 12), bg = "light blue", width = 20, height = 2)
        text_label.place(x = 205, y = 150)
        count_label = tk.Label(gameWindow, text = count, font = ("Arial", 16), bg = "light blue", width = 15, height = 2)
        count_label.place(x = 205, y = 180)
        self.checkWin(gameWindow, self.count)

    def updateCountOne(self, gameWindow, count):
        """Method used to update the count of the game by 1 when button 1 is pressed
        :param gameWindow: tkinter window for game, only used to pass to display_count() method"""
        self.count = count + 1
        self.numclicks += 1
        self.display_count(gameWindow, self.count)
    
    def updateCountTwo(self, gameWindow, count):
        """Method used to update the count of the game by 2 when button 2 is pressed
        :param gameWindow: tkinter window for game, only used to pass to display_count() method"""
        self.count = count + 2
        self.numclicks += 1
        self.display_count(gameWindow, self.count)
    
    def updateCountThree(self, gameWindow, count):
        """Method used to update the count of the game by 3 when button 3 is pressed
        :param gameWindow: tkinter window for game, only used to pass to display_count() method"""
        self.count = count + 3
        self.numclicks += 1
        self.display_count(gameWindow, self.count)
    
    def checkWin(self, gameWindow, count):
        """Method for continually checking if count has reached 21
        :param gameWindow: tkinter window for game, only used to place label on when player has lost the game
        :param count: int for current tally in game, game over when hits 2"""
        if count >= 21:
            playerLose = "Player", self.numclicks % 2 + 1, "Lost!"
            showLose = tk.Label(gameWindow, text = playerLose, font = ("Arial", 16), bg = "red")
            showLose.place(x = 230, y = 250)

class Matching_Game():
    """Class used to store all code to run matching game"""
    
    def __init__(self):
        """Method to play game automatically once game is started"""
        self.setup()
        self.gameOver = False
        self.playerTurn = 1
        mouseClick = 1

        while not self.gameOver:
            self.drawBoard()
            self.mousePoint = self.win.getMouse()   #Used for getting mouse coordinates

            if mouseClick == 1:   #If clicking first square of pair
                #Get row and col of first square
                fnum = self.board[self.getPosition()[0]][self.getPosition()[1]]
                frow = self.getPosition()[0]
                fcol = self.getPosition()[1]
                #Flip the square
                self.board[self.getPosition()[0]][self.getPosition()[1]] = -self.board[self.getPosition()[0]][self.getPosition()[1]]
                mouseClick += 1
            
            elif mouseClick == 2:   #If clicking second square of pair
                #Get row and col of second square
                snum = self.board[self.getPosition()[0]][self.getPosition()[1]]
                srow = self.getPosition()[0]
                scol = self.getPosition()[1]
                
                if frow == srow and fcol == scol:   #If same square do nothing
                    mouseClick = 2
                else:   #If not same square then flip second tile
                    self.board[self.getPosition()[0]][self.getPosition()[1]] = -self.board[self.getPosition()[0]][self.getPosition()[1]]
                    mouseClick += 1
            
            elif mouseClick == 3:   #If both squares of pair clicked have been flipped
                #If two squares are not equal value, flip them back over
                if fnum != snum:
                    self.board[frow][fcol] = -self.board[frow][fcol]
                    self.board[srow][scol] = -self.board[srow][scol]
                    mouseClick = 1
                #If two squares are equal value, keep them flipped and check if all squares are flipped
                else:
                    mouseClick = 1
                    self.checkWin()
    
    def setup(self):
        """Method to create window for game and generate randomly oragnized matrix for matching pairs"""
        self.numPairs = 8   #Define number of pairs in game
        numSquares = m.ceil(m.sqrt(self.numPairs*2))   #Find number of squares required for number of pairs
        windowSize = 600
        self.squareSize = windowSize//numSquares   #Define size for squares so that all squares will fit properly in window

        #Create list of correct number of pairs
        nums = []
        for i in range(self.numPairs):
            for j in range(2):
                nums.append(i + 1)
        
        #Randomize pair list so that game is not the same every time
        r.shuffle(nums)
        self.board = []
        
        #Create array based on number of squares contained in board, split list into separate rows
        for row in range(numSquares):
            self.board.append([])
            for col in range(numSquares):
                if len(nums) != 0:
                    self.board[row].append(nums.pop())
        
        #Display window
        self.win = GraphWin("Matching Game", windowSize, windowSize)
        self.win.setBackground("light blue")
    
    def drawBoard(self):
        """Method to draw game board with appropriate number of tiles, and fill in tiles with color"""
        #Draw squares on board, in form of equally sized squares
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != 0:
                    x = j * self.squareSize
                    y = i * self.squareSize
                    #x and y change so that squares are not all generated in the same spot
                    rect = Rectangle(Point(x, y), Point(x + self.squareSize, y + self.squareSize))
                    rect.setFill("light blue")
                    #Draw squares to board
                    rect.draw(self.win)
                    
                    #If spot on board is not empty space
                    if self.board[i][j] < 0:
                        num = -self.board[i][j]
                        text = Text(Point(x + self.squareSize/2, y + self.squareSize/2), str(num))
                        text.setTextColor("black")
                        text.setSize(30)
                        text.draw(self.win)
    
    def getPosition(self):
        """Method to get cursor position when mouse is clicked
        :return: tuple of cursor position, in terms of rows and cols of the game board"""
        row = int(self.mousePoint.getY() / self.squareSize)
        col = int(self.mousePoint.getX() / self.squareSize)
        return row, col
    
    def checkWin(self):
        """Method to check if game has been complete (all pairs have been correctly matched)"""
        counter = 0   #Number of pairs found
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] < 0:
                    counter += 1
        #If number of apirs found is equal to the number of pairs, then the game is voer
        if counter == self.numPairs * 2:
            self.gameOver = True

class Checkers():
    """Class used to store all code for running chess game"""
    
    def __init__(self):
        """Method to start game automatically once method is called"""
        #Run setup function for game, gameOver False until all player's pieces captured, playerTurn starts at 1, which is black player
        self.setup()
        gameOver = False
        self.playerTurn = 1
        mouseClick = 1
        self.drawBoard()

        #Keep running game as long as checkWin() does not set self.gameOver to True
        while gameOver == False:
            #Update board after each turn
            if mouseClick == 1:
                self.drawBoard()   #Draw current board
                self.clear(self.win)   #Then wipe previous board
            self.mousePoint = self.win.getMouse()
            self.anotherPiece = False   #Used if player wants to switch piece they've clicked to move
            
            #Makes sure that first spot clicked contains piece
            if mouseClick == 1:
                while not self.validPiece():
                    self.mousePoint = self.win.getMouse()
                mouseClick = 2

            #Makes sure second spot clicked is a valid move
            elif mouseClick == 2:
                run = True
                while not self.validMove():
                    self.mousePoint = self.win.getMouse()
                    run = False
                    mouseClick = 1
                    break

                #If move is valid, move piece, then change whose turn it is
                if not self.anotherPiece and run == True:
                    mouseClick = 1
                    self.movePiece()
                    #Only use for these methods is to change playerturn for checking valid pieces and moves
                    if self.playerTurn == 1:
                        self.playerTurn = 2
                    elif self.playerTurn == 2:
                        self.playerTurn = 1
            
            self.checkKing()   #Check for any normal pieces to make king pieces
            gameOver = self.checkWin()   #Check if game has been won
        
        #When game is over, display text indicating which player won the game
        if gameOver == True:
            if self.playerTurn == 1:
                winString = "Player 1 Won!"
            elif self.playerTurn == 2:
                winString = "Player 2 Won!"
            winText = Text(Point(400, 400), winString)
            winText.setSize(36)
            winText.setStyle("bold")
            winText.setTextColor("red")
            winText.draw(self.win)

    def setup(self):
        """Method used only for creating game window and initalizing values of each spot on board"""
        #Starting state of board, 0 => empty square, 1 => square with black piece, 2 => square with white piece
        self.board = [  [0, 2, 0, 2, 0, 2, 0, 2],
                        [2, 0, 2, 0, 2, 0, 2, 0],
                        [0, 2, 0, 2, 0, 2, 0, 2],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 0, 1, 0, 1, 0, 1, 0],
                        [0, 1, 0, 1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0]]
        
        #Set window to be slightly wider than tall, so can display information in side panel
        windowWidth = 1000
        windowHeight = 800
        self.squareSize = 100
        self.win = GraphWin("Checkers Game", windowWidth, windowHeight)
        self.win.setBackground("antique white")   #This will be the color of the side panel
    
    def getPosition(self):
        """Method used to get position of mouseclick and transform that into row and col values equal to index of board
        :return: tuple row, col, values of board index where clicked"""
        row = int(self.mousePoint.getY() // self.squareSize)
        col = int(self.mousePoint.getX() // self.squareSize)
        if col > 7:
            col = 7
        return row, col

    def drawBoard(self):
        """Method used to draw board and pieces. Draws tiles of board first, then draws pieces based on valud of piece"""
        #Double for loop to iterate through every square in board
        for i in range(8):
            for j in range(8):
                #Draw board first before pieces
                #Have to have nested if statements since row tiles are offset in color
                if i % 2 == 0:
                    if j % 2 == 0:
                        x = j * self.squareSize
                        y = i * self.squareSize
                        rect = Rectangle(Point(x, y), Point(x + self.squareSize, y + self.squareSize))
                        rect.setFill("burlywood2")
                        rect.draw(self.win)
                
                    elif j % 2 == 1:
                        x = j * self.squareSize
                        y = i * self.squareSize
                        rect = Rectangle(Point(x, y), Point(x + self.squareSize, y + self.squareSize))
                        rect.setFill("burlywood4")
                        rect.draw(self.win)
                
                elif i % 2 == 1:
                    if j % 2 == 0:
                        x = j * self.squareSize
                        y = i * self.squareSize
                        rect = Rectangle(Point(x, y), Point(x + self.squareSize, y + self.squareSize))
                        rect.setFill("burlywood4")
                        rect.draw(self.win)
                
                    elif j % 2 == 1:
                        x = j * self.squareSize
                        y = i * self.squareSize
                        rect = Rectangle(Point(x, y), Point(x + self.squareSize, y + self.squareSize))
                        rect.setFill("burlywood2")
                        rect.draw(self.win)

        #Second double for loop to iterate through every square in board
        for i in range(8):
            for j in range(8):
                #Draw pieces on top of board
                #If 1, draw black circle
                if self.board[i][j] == 1:
                    circ = Circle(Point(j * self.squareSize + self.squareSize/2, i * self.squareSize + self.squareSize/2), 45)
                    circ.setFill("black")
                    circ.draw(self.win)
                
                #If 2, draw white circle
                elif self.board[i][j] == 2:
                    circ = Circle(Point(j * self.squareSize + self.squareSize/2, i * self.squareSize + self.squareSize/2), 45)
                    circ.setFill("white")
                    circ.draw(self.win)
                
                #If 3, draw black circle with letter K in white
                elif self.board[i][j] == 3:
                    circ = Circle(Point(j * self.squareSize + self.squareSize/2, i * self.squareSize + self.squareSize/2), 45)
                    circ.setFill("black")
                    circ.draw(self.win)
                    king = Text(Point(j * self.squareSize + self.squareSize/2, i * self.squareSize + self.squareSize/2), 'K')
                    king.setSize(25)
                    king.setTextColor("white")
                    king.setStyle("bold")
                    king.draw(self.win)
                
                #If 4, draw white circle with letter K in black
                elif self.board[i][j] == 4:
                    circ = Circle(Point(j * self.squareSize + self.squareSize/2, i * self.squareSize + self.squareSize/2), 45)
                    circ.setFill("white")
                    circ.draw(self.win)
                    king = Text(Point(j * self.squareSize + self.squareSize/2, i * self.squareSize + self.squareSize/2), 'K')
                    king.setSize(25)
                    king.setTextColor("black")
                    king.setStyle("bold")
                    king.draw(self.win)
        
        instructions = Text(Point(900, 400), "Player 1 = Black\n Player 2 = White\n\nAlternate turns\nNo double jumps\nCapture all opponent pieces\nIf player cannot move,\nthey lose")
        instructions.draw(self.win)
    
    def validPiece(self):
        """Method to check if first spot selected on a turn contains a piece
        :return: True if contains piece, False if does not"""

        prow = self.getPosition()[0]
        pcol = self.getPosition()[1]
        
        #If player 1 and piece is black, return True
        if ((self.board[prow][pcol] == 1 or self.board[prow][pcol] == 3) and self.playerTurn == 1):
            self.prow = prow
            self.pcol = pcol
            return True
        
        #If player 2 and piece is white, return True
        elif ((self.board[prow][pcol] == 2 or self.board[prow][pcol] == 4) and self.playerTurn == 2):
            self.prow = prow
            self.pcol = pcol
            return True
        
        #else return False
        return False
    
    def validMove(self):
        """Method to check if second spot selected on a turn is a valid move
        :return: True is move is valid, False if move is invalid"""

        erow = self.getPosition()[0]
        ecol = self.getPosition()[1]
        
        #If the clicked space is empty
        if self.board[erow][ecol] == 0:
            
            #This if statement only runs for pieces that are value 1, therefore normal black pieces
            if self.board[self.prow][self.pcol] == 1:
                #If spot clicked is one diagonal up from current spot and empty, is valid move
                if ((erow + 1 == self.prow and ecol - 1 == self.pcol) or (erow + 1 == self.prow and ecol + 1 == self.pcol)):
                    self.erow = erow
                    self.ecol = ecol
                    return True
                
                #If spot clicked is two diagonal spots up and left from current spot, and diagonal between clicked spot and current spot contains white piece, jump and remove white piece
                elif ((self.board[erow + 1][ecol - 1] == 2 or self.board[erow + 1][ecol - 1] == 4) and (erow + 2 == self.prow and ecol - 2 == self.pcol)):
                    self.erow = erow
                    self.ecol = ecol
                    self.board[erow + 1][ecol - 1] = 0
                    return True
                
                #If spot clicked is two diagonal spots up and right from current spot, and diagonal between clicked spot and current spot contains white piece, jump and remove white piece
                elif ((self.board[erow + 1][ecol + 1] == 2 or self.board[erow + 1][ecol + 1] == 4) and (erow + 2 == self.prow and ecol + 2 == self.pcol)):
                    self.erow = erow
                    self.ecol = ecol
                    self.board[erow + 1][ecol + 1] = 0
                    return True
            
            #This if statement only runs for pieces that are value 2, therefore normal white pieces
            elif self.board[self.prow][self.pcol] == 2:
                #If spot clicked is one diagonal down from current spot and empty, is valid move
                if ((erow - 1 == self.prow and ecol - 1 == self.pcol) or (erow - 1 == self.prow and ecol + 1 == self.pcol)):
                    self.erow = erow
                    self.ecol = ecol
                    return True
                
                #If spot clicked is two diagonal spots down and left from current spot, and diagonal between clicked spot and current spot contains black piece, jump and remove black piece
                elif ((self.board[erow - 1][ecol - 1] == 1 or self.board[erow - 1][ecol - 1] == 3) and (erow - 2 == self.prow and ecol - 2 == self.pcol)):
                    self.erow = erow
                    self.ecol = ecol
                    self.board[erow - 1][ecol - 1] = 0
                    return True
                
                #If spot clicked is two diagonal spots down and right from current spot, and diagonal between clicked spot and current spot contains black piece, jump and remove black piece
                elif ((self.board[erow - 1][ecol + 1] == 1 or self.board[erow - 1][ecol + 1] == 3) and (erow - 2 == self.prow and ecol + 2 == self.pcol)):
                    self.erow = erow
                    self.ecol = ecol
                    self.board[erow - 1][ecol + 1] = 0
                    return True

            #This if statement only runs for pieces that are value 3, therefore black kings
            #Allows black kings to move in any 4 directions diagonally
            elif self.board[self.prow][self.pcol] == 3:
                #If spot clicked is one diagonal in any direction and empty, is valid move
                if ((erow - 1 == self.prow or erow + 1 == self.prow) and (ecol - 1 == self.pcol or ecol + 1 == self.pcol)):
                    self.erow = erow
                    self.ecol = ecol
                    return True
                
                if erow > 0:   #Make sure list indexes are not out of range
                    if ecol > 0:   #Make sure list indexes are not out of range
                        #If spot clicked is two diagonal spots up and left from current spot, and diagonal between clicked spot and current spot contains white piece, jump and remove white piece
                        if ((self.board[erow - 1][ecol - 1] == 2 or self.board[erow - 1][ecol - 1] == 4) and (erow - 2 == self.prow and ecol - 2 == self.pcol)):
                            self.erow = erow
                            self.ecol = ecol
                            self.board[erow - 1][ecol - 1] = 0
                            return True

                    if ecol < 8:   #Make sure list indexes are not out of range
                        #If spot clicked is two diagonal spots up and right from current spot, and diagonal between clicked spot and current spot contains white piece, jump and remove white piece
                        if ((self.board[erow - 1][ecol + 1] == 2 or self.board[erow - 1][ecol + 1] == 4) and (erow - 2 == self.prow and ecol + 2 == self.pcol)):
                            self.erow = erow
                            self.ecol = ecol
                            self.board[erow - 1][ecol + 1] = 0
                            return True

                if erow < 8:   #Make sure list indexes are not out of range
                    if ecol > 0:   #Make sure list indexes are not out of range
                        #If spot clicked is two diagonal spots down and left from current spot, and diagonal between clicked spot and current spot contains white piece, jump and remove white piece
                        if ((self.board[erow + 1][ecol - 1] == 2 or self.board[erow + 1][ecol - 1] == 4) and (erow + 2 == self.prow and ecol - 2 == self.pcol)):
                            self.erow = erow
                            self.ecol = ecol
                            self.board[erow + 1][ecol - 1] = 0
                            return True

                    if ecol < 8:   #Make sure list indexes are not out of range
                        #If spot clicked is two diagonal spots down and right from current spot, and diagonal between clicked spot and current spot contains white piece, jump and remove white piece
                        if ((self.board[erow + 1][ecol + 1] == 2 or self.board[erow + 1][ecol + 1] == 4) and (erow + 2 == self.prow and ecol + 2 == self.pcol)):
                            self.erow = erow
                            self.ecol = ecol
                            self.board[erow + 1][ecol + 1] = 0
                            return True
            
            #This if statement only runs for pieces that are value 4, therefore white kings
            elif self.board[self.prow][self.pcol] == 4:
                #If spot clicked is one diagonal in any direction and empty, is valid move
                if ((erow - 1 == self.prow or erow + 1 == self.prow) and (ecol - 1 == self.pcol or ecol + 1 == self.pcol)):
                    self.erow = erow
                    self.ecol = ecol
                    return True
                
                if erow > 0:   #Make sure list indexes are not out of range
                    if ecol > 0:   #Make sure list indexes are not out of range
                        #If spot clicked is two diagonal spots up and left from current spot, and diagonal between clicked spot and current spot contains black piece, jump and remove black piece
                        if ((self.board[erow - 1][ecol - 1] == 1 or self.board[erow - 1][ecol - 1] == 3) and (erow - 2 == self.prow and ecol - 2 == self.pcol)):
                            self.erow = erow
                            self.ecol = ecol
                            self.board[erow - 1][ecol - 1] = 0
                            return True

                    if ecol < 8:   #Make sure list indexes are not out of range
                        #If spot clicked is two diagonal spots up and right from current spot, and diagonal between clicked spot and current spot contains black piece, jump and remove black piece
                        if ((self.board[erow - 1][ecol + 1] == 1 or self.board[erow - 1][ecol + 1] == 3) and (erow - 2 == self.prow and ecol + 2 == self.pcol)):
                            self.erow = erow
                            self.ecol = ecol
                            self.board[erow - 1][ecol + 1] = 0
                            return True

                if erow < 8:   #Make sure list indexes are not out of range
                    if ecol > 0:   #Make sure list indexes are not out of range
                        #If spot clicked is two diagonal spots down and left from current spot, and diagonal between clicked spot and current spot contains white piece, jump and remove black piece
                        if ((self.board[erow + 1][ecol - 1] == 1 or self.board[erow + 1][ecol - 1] == 3) and (erow + 2 == self.prow and ecol - 2 == self.pcol)):
                            self.erow = erow
                            self.ecol = ecol
                            self.board[erow + 1][ecol - 1] = 0
                            return True

                    if ecol < 8:   #Make sure list indexes are not out of range
                        #If spot clicked is two diagonal spots down and right from current spot, and diagonal between clicked spot and current spot contains white piece, jump and remove black piece
                        if ((self.board[erow + 1][ecol + 1] == 1 or self.board[erow + 1][ecol + 1] == 3) and (erow + 2 == self.prow and ecol + 2 == self.pcol)):
                            self.erow = erow
                            self.ecol = ecol
                            self.board[erow + 1][ecol + 1] = 0
                            return True
            
            return False
        
        #If the clicked space is occupied
        elif self.board[erow][ecol] != 0:
            #If clicked spot contains piece of same color, then change piece being moved to new piece (i.e. player misclicks)
            if self.playerTurn == 1 and (self.board[erow][ecol] == 1 or self.board[erow][ecol] == 3):
                self.anotherPiece = True
                self.prow = erow
                self.pcol = ecol
                return True
            if self.playerTurn == 2 and (self.board[erow][ecol] == 2 or self.board[erow][ecol] == 4):
                self.anotherPiece = True
                self.prow = erow
                self.pcol = ecol
                return True
            #Otherwise return False
            return False
    
    def movePiece(self):
        """Method to change values of board array to reflect pieces being moved"""
        
        if self.playerTurn == 1:   #If black's turn
            if self.board[self.prow][self.pcol] == 1:   #If moving normal black piece
                self.board[self.prow][self.pcol] = 0   #Set original spot to be empty
                self.board[self.erow][self.ecol] = 1   #Set new spot to contain normal black piece
            
            elif self.board[self.prow][self.pcol] == 3:   #If moving black king piece
                self.board[self.prow][self.pcol] = 0   #Set original spot to be empty
                self.board[self.erow][self.ecol] = 3   #Set new spot to contain black king piece
        
        elif self.playerTurn == 2:   #If white's turn
            if self.board[self.prow][self.pcol] == 2:   #If moving normal white piece
                self.board[self.prow][self.pcol] = 0   #Set original spot to be empty
                self.board[self.erow][self.ecol] = 2   #Set new spot to contain normal white piece
            
            elif self.board[self.prow][self.pcol] == 4:   #If moving black king piece
                self.board[self.prow][self.pcol] = 0   #Set original spot to be empty
                self.board[self.erow][self.ecol] = 4   #Set new spot to contain white king piece
            
    def clear(self, win):
        """Method used to clear previous versions of the board, to prevent game window from slowing down"""

        halfindex = len(win.items) // 2   #Only want to erase objects from previous iteration of board, not current
        for item in win.items[:halfindex]:   #FIrst half of win.items is previous iteration, second half is current iteration
            item.undraw()
        win.update()

    def checkKing(self):
        """Method used to check if there are any new pieces in top or bottom row, and then convert them to king pieces"""
        for i in range(8):
            if self.board[0][i] == 1:
                self.board[0][i] = 3
            if self.board[7][i] == 2:
                self.board[7][i] = 4
    
    def checkWin(self):
        """Method used to check if either player has run out of pieces
        If either player has no pieces left, that means that the game is over"""

        p1count = 0
        p2count = 0

        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 1 or self.board[i][j] == 3:
                    p1count += 1

                if self.board[i][j] == 2 or self.board[i][j] == 4:
                    p2count += 1

        if p1count == 0 or p2count == 0:
            print("game over")
            return True
        
        return False