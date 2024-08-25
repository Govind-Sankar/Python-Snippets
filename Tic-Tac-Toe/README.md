# Python Tic-Tac-Toe Game
This is a simple command-line implementation of the classic Tic-Tac-Toe game in Python. The game is played on a 3x3 grid, where two players take turns to place their marks (X or O) on the board. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

## How to Play
1. Run the program.
2. The board will be displayed with numbered positions from 1 to 9.
3. Players will be prompted to enter the position (1-9) where they want to place their mark.
4. The program will check if the position is already taken. If it is, the game will end.
5. The board will be updated and displayed after each turn.
6. The game will check for a winner after each move. If there is a winner, the game will announce the winner and end.
7. If all positions are filled and there is no winner, the game will end in a tie.

## Requirements
Python 3.x

## How to Run
1. Ensure you have Python installed on your system.
2. Save the code in a file named tic_tac_toe.py.
3. Run the script using the command:
```bash
python tic_tac_toe.py
```

## Notes
- The game will terminate if an invalid input is given or if a position is already taken.
- The board uses a 1-based index, so positions are numbered from 1 to 9.

## License
This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
