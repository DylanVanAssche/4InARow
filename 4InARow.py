# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 13:47:07 2016
@author: Dylan Van Assche
@title: Simple 4 in a row game
"""

import sys

class Error(Exception):
    pass

class EndGame(Exception):
    pass

class Token():
    
    def __init__(self, player, positionX):
        self.player = player
        self.positionX = positionX
        self.positionY = 0

class Board():
    
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self.board = [[0 for i in range(self._columns)] for j in range(self._rows)]
    
    def insert(self, token):
        for i in range(self._rows-1, -1, -1):
            if self.board[i][token.positionX] == 0:
                self.board[i][token.positionX] = token.player
                break
            elif(i == 0):
                raise Error("Target full, choose another column!")
    
    def printBoard(self):
        print "-" * (self._columns * 4 + 1)
        for i in range(self._rows):
            boardString = "| "
            for j in range(self._columns):
                if self.board[i][j] != 0:
                    if j < self._columns-1:
                        boardString += str(self.board[i][j]) + " | "
                    else:
                        boardString += str(self.board[i][j])
                else:
                        boardString += "  | "
            print boardString
            print "-" * (self._columns * 4 + 1)
    
    def searchHorizontal(self):
        
        for i in range(self._rows):
            self._searchString = ""
            for j in range(self._columns):
                if self.board[i][j] != 0:
                    self._searchString += self.board[i][j]
                else:
                    self._searchString += " "
                    
            self.findWinner()
                
    def searchVertical(self):
        
        for j in range(self._columns):
            self._searchString = ""
            for i in range(self._rows):
                if self.board[i][j] != 0:
                    self._searchString += self.board[i][j]
                else:
                    self._searchString += " "
            
            self.findWinner()
                
    def searchDiagonal1(self):
        
        for k in range(self._columns-1, -1, -1):
            for i in range(self._rows):
                self._searchString = ""
                for j in range(self._columns):
                    try:
                        if self.board[i+j][k+j] != 0:
                            self._searchString += self.board[i+j][k+j]
                        else:
                            self._searchString += " "
                    except:
                        break
                        
                self.findWinner()
                
    def searchDiagonal2(self):
        
        for k in range(self._columns-1, -1, -1):
            for i in range(self._rows):
                self._searchString = ""
                for j in range(self._columns):
                    try:
                        if self.board[i+j][self._columns-1-j-k] != 0:
                            self._searchString += self.board[i+j][self._columns-1-j-k]
                        else:
                            self._searchString += " "
                    except:
                        break
                    
                self.findWinner()       

                    
    def findWinner(self):
        if self._searchString.find("YYYY") >= 0:
            self.printBoard() 
            raise EndGame("[INFO] Player YELLOW wins!")
        
        elif self._searchString.find("RRRR") >= 0:
            self.printBoard() 
            raise EndGame("[INFO] Player RED wins!")
            
            
    
def main():
    print "[INFO] Simple 4 in a row game by Dylan Van Assche"
    player = "R"
    while(True):
        
        try:
            board_input = raw_input("[QUESTION] Give the size of the board as ROWS,COLUMNS: ")
            rows, columns = board_input.split(',')
            rows = int(rows)
            columns = int(columns)
            game = Board(rows, columns)
            break
            
        except ValueError:
            print "[ERROR] Input is not an integer or not given as ROWS,COLUMNS!"
    
    while(True):
        
        try:
            positionX = raw_input("[QUESTION] Column to insert new token: ")
            positionX = int(positionX)                
            token = Token(player, positionX)
            
            try:
                game.insert(token)
                if player == "R":
                    player = "Y"
                else:
                    player = "R"
            except Error as e:
                print e
            try:
                game.searchHorizontal()
                game.searchVertical()
                game.searchDiagonal1()
                game.searchDiagonal2()
                game.printBoard()
            except EndGame as end:
                print end
                sys.exit(1)

            if player == "Y":
                print "[INFO] Next player: YELLOW"
            else:
                print "[INFO] Next player: RED"
                
        except ValueError:
            print "[ERROR] Input is not an integer!"
        
        except KeyboardInterrupt:
            print "Exiting game..."
            sys.exit(1)

main()
