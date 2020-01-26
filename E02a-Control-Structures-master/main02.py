#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
print(color)

##BEFORE: Just as before, but only it will print out whatever color name, or just anything in general, that
##          is typed in. After repeating after the user, the program will end.

##AFTER: Correct. Since the programmer said, "Okay, whatever the user says, I want you to repeat," the program
##          actually did something rather than end so quickly. 