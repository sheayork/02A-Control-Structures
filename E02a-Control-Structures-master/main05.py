#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')

##BEFORE: .lower means lowercase, I'm assuming, so if the user puts any kind of 'red' answer ('Red,' 'RED,' etc.),
##          the program will lowercase every letter for the person's answer. This makes it easier to ensure that
##          the program can accept any form of red. 

##AFTER: Correct.