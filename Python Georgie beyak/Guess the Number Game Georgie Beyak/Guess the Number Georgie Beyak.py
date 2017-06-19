import random
import sys 
guessestaken = 0
guess = 0
print('Hello!')

number = random.randint(1, 1000)
print('I am thinking of a number between 1 and 1000.')
my_input = input("A)Guess a number\nB)Quit\n")
if my_input.lower()== "a":
    while guessestaken < 300:
        print('Take a guess.') 
        guess = input()
        guess = int(guess)

        guessestaken = guessestaken + 1

        if guess < number:
            print('Your guess is too low.') 

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break
else: 
    my_input.lower()== "b"    
    sys.exit 
if guess == number:
    guessestaken = str(guessestaken)
    print('You guessed my number in ' + guessestaken + ' guesses!')

if guess != number and guess != 0:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)