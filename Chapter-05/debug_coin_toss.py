import random

guess = ''
guess_options = ['heads', 'tails']
while guess not in guess_options:
    print('Guess the coin toss! Enter heads or tails;')
    guess = input('> ')

toss_num = random.randint(0, 1)
toss = guess_options[toss_num]  # 0 is tails, 1 is heads.
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input('> ')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
