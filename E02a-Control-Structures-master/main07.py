#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
color = color.lower().strip()
if (color == 'red'):
    print('Correct!')
elif (color == 'pink'):
    print('Close!')
else:
    print('Sorry, try again.')

##BEFORE: The program changes the answer before the if/else method instead of during, making the code a little
##          bit easier to follow. Additionally, there's elif, which gives the program an alternative answer
##          to look at and determine how it will respond to the user. Typically I just use if's, no matter
##          how many, and then end with an else. 

##AFTER: Correct