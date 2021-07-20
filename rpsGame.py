
# Online Python - IDE, Editor, Compiler, Interpreter

import sys
import random
win = int(0)
loss = int(0)
Tie = int(0)

while True:
    print('ROCK, PAPER, SCISSORS')
    while True:
        print(str(win) + ' Wins', str(loss) + ' Losses', str(Tie) + ' Ties')
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s, or q.')
        
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
        
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')
        
        
    if playerMove == computerMove:
        print('It is a tie!')
        Tie = Tie + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        win = win + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        win = win + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        win = win + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        loss = loss + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        loss = loss + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        loss = loss + 1
    
