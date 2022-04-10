print("Welome to my Computer quiz!")

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print('Okay! Let\'s playing')
score = 0

answer = input("what does cpu stand for? ")
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("what does gpu stand for? ")
if answer == "graphic processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("what does ram stand for? ")
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("what does psu stand for? ")
if answer == "power supply":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


print("you got a " + str(score) + " questions correct.")
