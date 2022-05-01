#---------------------------------
# Checkers program for Game Hub
#---------------------------------

from graphics import *
import time

#In terms of redrawing board overtop for each move, would be easier to redraw single square where piece was
#This would stop ripple updating of board and pieces

class Checkers():
    
    def __init__(self):
        """Method to start game automatically once method is called"""
        #Run setup function for game, gameOver False until all player's pieces captured, playerTurn starts at 1, which is black player
        self.setup()
        self.gameOver = False
        self.playerTurn = 1
        mouseClick = 1

        while not self.gameOver:
            self.drawBoard()
            self.mousePoint = self.win.getMouse()
            
            if mouseClick == 1:
                while not self.validPiece():
                    self.mousePoint = self.win.getMouse()
                    #Set variables equal to prow and pcol so that can use them to pass into validMove() to check if move is valid
            
            elif mouseClick == 2:
                while not self.validMove(self.prow, self.pcol):
                    self.mousePoint = self.win.getMouse()
            
            if self.playerTurn == 1:
                pass

            elif self.playerTurn == 2:
                pass

    def setup(self):
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
        windowWidth = 900
        windowHeight = 800
        self.squareSize = 100
        self.win = GraphWin("Checkers Game", windowWidth, windowHeight)
        self.win.setBackground("antique white")   #This will be the color of the side panel
    
    def drawBoard(self):
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
                if self.board[j][i] == 1:
                    circ = Circle(Point(i * self.squareSize + self.squareSize/2, j * self.squareSize + self.squareSize/2), 45)
                    circ.setFill("black")
                    circ.draw(self.win)
                
                #If 2, draw white circle
                elif self.board[j][i] == 2:
                    circ = Circle(Point(i * self.squareSize + self.squareSize/2, j * self.squareSize + self.squareSize/2), 45)
                    circ.setFill("white")
                    circ.draw(self.win)
                
                #If 3, draw black king
                elif self.board[j][i] == 3:
                    circ = Circle(Point(i * self.squareSize + self.squareSize/2, j * self.squareSize + self.squareSize/2), 45)
                    circ.setFill("black")
                    circ.draw(self.win)
                
                #If 4, draw white king
                elif self.board[j][i] == 4:
                    circ = Circle(Point(i * self.squareSize + self.squareSize/2, j * self.squareSize + self.squareSize/2), 45)
                    circ.setFill("white")
                    circ.draw(self.win)
    
    def getPosition(self):
        row = int(self.mousePoint.getX() / self.squareSize)
        col = int(self.mousePoint.getY() / self.squareSize)
        return row, col
    
    def validPiece(self):
        print("Checking valid")
        prow = self.getPosition()[0]
        pcol = self.getPosition()[1]
        if ((self.board[prow][pcol] == 1 or self.board[prow][pcol] == 3) and self.playerTurn == 1):
            self.prow = prow
            self.pcol = pcol
            return True
        elif ((self.board[prow][pcol] == 2 or self.board[prow][pcol] == 4) and self.playerTurn == 2):
            self.prow = prow
            self.pcol = pcol
            return True
        return False
    
    def validMove(self, pieceRow, pieceCol):
        prow = self.getPosition()[0]
        pcol = self.getPosition()[1]
        if self.board[prow][pcol] == 0:
            pass

newgame = Checkers()
