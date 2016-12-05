# 4InARow
4 in a row game written in Python with classes

## How to use
* Run the py file (Python 2.7 and 3.5 is supported).
* Choose how big your board need to be, a normal 4 in a row game uses a 6x7  board.
* Type the integer number of the column you want to place your token (0 - ...).
* The game will end when a winner is found or when you press CTRL + C.
* A new game can be started by running the py file again.

## How does this work?
### Game
* Creates a token connected with the right player.
* Token is inserted into the board.
* Searching for a winning combination each time a token has been inserted. 

### Searching for a winner algorithm
* Creates a string of each row, column or diagonals.
* Checks for the winning combinations: RRRR or YYYY.
* Ends the game if a winning combination has been detected.

### UI
* Prints every move the new board in the Python console by converting the board matrix into a string.
* Board is constructed by using '-' and '|' characters.
