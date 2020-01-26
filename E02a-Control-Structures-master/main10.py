#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') #Greets the user
colors = ['red','orange','yellow','green','blue','violet','purple'] #List of colors program needs
play_again = '' #just blank space
best_count = sys.maxsize            # the biggest number #The highscore

while (play_again != 'n' and play_again != 'no'): #While the user says not to end the game at play_again
    match_color = random.choice(colors) #Chooses a random color from the list 
    count = 0 #Keeps track of how many guesses were made
    color = '' 
    while (color != match_color): #while the color isn't the answer to match_color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line #The question
        color = color.lower().strip() #Changes answer to lowercase and eliminates any spaces after set of characters
        count += 1 #Adds a number to count each time the asnwer is wrong
        if (color == match_color): #If it matches, it says correct and asks user if they want to play again
            print('Correct!')
        else: #Says they're wrong, says how many times they guessed so far, then asks the question again
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    
    print('\nYou guessed it in {} tries!'.format(count)) #When correct, the program says how many times it took for them to guess this round

    if (count < best_count): #If this count is less than the previous high score, the program tells them
        print('This was your best guess so far!')
        best_count = count

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() #asks the user if they want to play again

print('Thanks for playing!') #If they say no to play_again, the program thanks them and ends

##BEFORE: There's now a list of colors, and the programmer uses a random import function so the program
##          picks a color at random - one the programmer may not even know. Otherwise, it keeps asking the user
##          what color it is, it tells them how many guesses they made so far if they get it wrong, then
##          when they get it right it says they're right, asks if they want to play again, then either restarts by
##          itself or ends. It also keeps track of their highscore. 

##AFTER: Correct. In order to make this better, though, I would have probably printed out a list before
##          the input section so the user knows how many colors the program is thinking and choosing from.
##          Otherwise, if the user forgot about violet, they could be here forever. 