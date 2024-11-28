'''
https://www.codewars.com/kata/564e1d90c41a8423230000bc

DESCRIPTION:

Knight vs King
If you are not familiar with chess game you can learn more Here .

Here is the chess board (rows, denoted by numbers, are called ranks, columns, denoted by a
letter, are called files):

You put a Knight and a King in the board.

Complete the method that tell us which one can capture the other one.

You are provided with two object array; each contains an integer (the rank, first item) and a
string/char (the file, second item) to show the position of the pieces in the chess board.

Return:

"Knight" if the knight is putting the king in check,
"King" if the king is attacking the knight
"None" if none of the above occur
Example:

knight = [7, "B"], king = [6, "C"]  ---> "King"
'''

def knight_vs_king(knight_position, king_position):
    # Three possible outputs are "Knight", "King", and "None"

    file = {

        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8
    }

    knight_moves = [[-1, 2], [-1, -2], [-2, 1],
                    [-2, -1], [1, 2], [1, -2], [2, 1], [2, -1]]

    king_moves = [[1, 0], [1, 1], [1, -1], [0, 1],
                  [0, -1], [-1, 1], [-1, -1], [-1, 0]]

    current_position = [knight_position[0] - king_position[0],
                        file[knight_position[1]] - file[king_position[1]]]

    if current_position in knight_moves:
        return "Knight"
    elif current_position in king_moves:
        return "King"
    else:
        return "None"

# Looking back, this is overkill. I thought it was so clever at the time.
