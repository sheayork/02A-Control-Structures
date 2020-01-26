#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

def choose_color(last_color):
    colors = ['red','orange','yellow','green','blue','violet','purple']
    c = random.choice(colors)
    while c == last_color:
        c = random.choice(colors)
    return c




print('Greetings!')
play_again = ''
best_count = sys.maxsize            # the biggest number
last_color = ''

while (play_again != 'n' and play_again != 'no'):
    count = 0
    color = ''
    match_color = choose_color(last_color)
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()
        count += 1
        if (color == match_color):
            print('Correct!')
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    
    print('\nYou guessed it in {} tries!'.format(count))

    if (count < best_count):
        print('This was your best guess so far!')
        best_count = count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()

print('Thanks for playing!')