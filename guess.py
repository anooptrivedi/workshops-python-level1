import random

secret = random.randint(1,100) #shh! secret, we need to find this
guess = 0 #starting guess
attempts = 0 #no of attempts we guesses in..

while secret != guess:

    guess = int(input('Guess a Number between 1 and 100: '))
    attempts +=1

    if(secret == guess):
        print('Good Job! You found the secret sauce')
    elif(secret > guess):
        print('Too low, Try Again!')
    else:
        print('Too high, Try Again!')

print('You found the secret', secret, 'in', attempts, 'attempts')
