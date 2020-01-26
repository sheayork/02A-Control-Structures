#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = ''
while (color != 'red'):
    color = input("What is my favorite color? ")
    color = color.lower().strip()
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')

##BEFORE: This puts the question inside of the while loop instead, and while the answer is not red, 
##          the program will continue to ask the person the question until they get it right. I'm not
##          sure if it will end since there is no break, so it may keep asking even after they get the
##          answer right. 

##AFTER: It did end, but otherwise I was correct. I guess the 'while' statement did kind of count as a break.