import random

number_digit = 3
max_guess = 10

def main():
    print(f'''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a {number_digit}-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.''')

    while True:
        secretnumber = getsecretnumber()
        print('I have thought up a number.')
        print(f'You have {max_guess} guesses to get it.')
        
        numguesses = 1
        while numguesses <= max_guess:
            guess = ''
            while len(guess) != number_digit or not guess.isdecimal():
                print(f'Guess # {numguesses}')
                guess = input('> ')

            clue = getclues(guess, secretnumber)
            print(clue)
            numguesses += 1

        if guess == secretnumber:
            break
        if numguesses >  max_guess:
            print('You are out of guesses')
            print(f'the secret number was {secretnumber}')

        print('Do you want to play again')
        if not input('> ').lower().startswith('y'):
            break

def getsecretnumber():
    number = list('0123456789')
    random.shuffle(number)
    secretnumber = ''

    for i in range(number_digit):
        secretnumber = secretnumber + str(number[i])
    return secretnumber

def getclues(guess, secretnumber):
    if guess == secretnumber:
        return 'you Got it'
    clue = []

    for i in range(len(guess)):
        if guess[i] == secretnumber[i]:
            clue.append('fermi')
        elif guess[i] in secretnumber:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagel'
    else:
        clue.sort()
        return ' '.join(clue)

    



if __name__ == '__main__':
    main()
