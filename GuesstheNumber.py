import random, sys

def guess(x):
    random_number = random.randint(1 , x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a Number between 1 and {x}: '))
        if guess < random_number:
            print('Too low')
        elif guess > random_number:
            print('Too high')

    print('you have guess the number')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low!= high:
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (c)??').lower()
        if feedback == 'h':
            high = guess -1
        if feedback == 'l':
            low = guess + 1

    print('computer have guess the number')
        
            
computer_guess(10)  
