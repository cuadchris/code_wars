'''
https://www.codewars.com/kata/5672a98bdbdd995fad00000f

DESCRIPTION:

Rock Paper Scissors

Let's play! You have to return which player won! In case of a draw return Draw!.

(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
'''

def rps(p1, p2):
    
    match(p1, p2):
        case ('rock', 'scissors') | ('scissors', 'paper') | ('paper', 'rock'):
            return 'Player 1 won!'
        case ('rock', 'rock') | ('scissors', 'scissors') | ('paper', 'paper'):
            return 'Draw!'
    
    return 'Player 2 won!'