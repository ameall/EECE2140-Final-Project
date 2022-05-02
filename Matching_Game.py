#---------------------------------
# Matching game for Game Center
#---------------------------------

import math as m
import random as r
from graphics import *

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
        
        if self.gameOver == True:
            winText = Text(Point(300, 300), "You've found all of\nthe matches!")
            winText.setSize(36)
            winText.setStyle("bold")
            winText.setTextColor("red")
            winText.draw(self.win)
    
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
