#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red'):
    print('Correct!')
else:
    print('Sorry, try again.')

##BEFORE: This time, it has an actual answer. If the person gets it exactly right, they're correct. Else, it ends.
##          There is no 'while True' function so the user has to reload this over and over again. Additionally, 
##          if the user says 'red' or 'RED' - just anything other than 'Red,' the program will assume it isn't right.

##AFTER: Correct. Python doesn't exactly know if 'red' or 'RED' is an answer because it isn't specified by 
##          the programmer. 