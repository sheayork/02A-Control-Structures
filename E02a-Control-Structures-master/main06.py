#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower().strip() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')

##BEFORE: Same as before, but some people may put spaces in-between letter or right after typing something
##          (I know I have a bad habit of doing the latter when it comes to typing papers). So basically the program
##          will remove those spaces and change everything to lowercase letters to tell if the answer
##          is right or not. 

##AFTER:  It didn't do it for spaces in-between letters, but otherwise I was correct. 