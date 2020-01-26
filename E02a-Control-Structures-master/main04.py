#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red' or color == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')

##BEFORE: Same as before, but this time they accept 'red' as an answer as well. If the user puts any of the two
##          different ways to 'say' red, they're correct; anything else doesn't work.

##AFTER: Correct.