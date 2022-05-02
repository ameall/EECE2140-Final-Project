#---------------------------------
# Checkers program for Game Hub
#---------------------------------

from graphics import *

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
