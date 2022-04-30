#---------------------------------
# Checkers program for Game Hub
#---------------------------------

"""
How to make this game:
    Make a 2D Array of objects, with values being 0, 1, or 2
    Make red canvas, then use for loop to create black squares over top of red canvas to represent the board
    Let 0 = empty square, 1 = square with white piece, 2 = square with black piece
        For spots in array marked with 1 or 2, display corresponding circle on square
    Have user click square with checkers piece first
        Make sure to check if there is actual checkers piece in clicked square
    Then have user click square where they want to move to and check if move is a valid move (diagonal by one square)
        If there is piece in square, then auto-move the piece to the spot on the diagonal after the piece
            Do we want to allow doulbe jumping?
    Keep counter of number of pieces controlled by each player (starting is 12)
        If counter reaches, the game is over and one player has won
    
In terms of graphics:
    Divide canvas into 8x8 grid and fill every other grid spot black to get checkerboard pattern
    Then display all the circles for the game pieces for both user (pieces should be on black tiles)
        Black player goes first

How to make this game:
    Make multiple classes, board, piece, and main
    Initialize board class and draw 8x8 grid of squares using graphics.py
    Set all squares to 0, then 
"""

from graphics import *

class Checkers():
    
    def __init__(self):
        """Method to start game automatically once method is called"""
        self.setup()
        self.gameOver = False
        self.playerTurn = 1

        while not self.gameOver:
            self.drawBoard()
            #self.mousePoint = self.win.getMouse()
        
    def setup(self):
        self.board = [  [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0]]
        windowWidth = 900
        windowHeight = 800
        self.squareSize = 100
        self.win = GraphWin("Checkers Game", windowWidth, windowHeight)
        self.win.setBackground("antique white")
    
    def drawBoard(self):
        for i in range(8):
            for j in range(8):
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
    
    def makePieces():
        pass

class Board():
    pass

class Piece():
    pass

newgame = Checkers()

# class Board():
#     def __init__(self):
#         self.setup()
#         self.drawBoard()
    
#     def setup(self):
#         self.board = []
#         for i in range(8):
#             boardRow = []
#             for j in range(8):
#                 boardRow.append(0)
#             self.board.append(boardRow)
#         for i in range(3):
#             for j in range(3):
#                 if i % 2 == 0:
#                     self.board[i][j*2] = 1
#                     self.board[7 - i][j * 2 + 1]
#                 if i % 2 == 1:
#                     self.board[i][j*2 + 1] = 1
#         windowSize = 600
#         self.win = GraphWin("Checkers", windowSize, windowSize)
#         self.win.setBackground('white')

#     def drawBoard():
#         for i in range(8):
#             for j in range(8):
#                 self.