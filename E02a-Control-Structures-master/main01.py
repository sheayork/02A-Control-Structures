#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
input("What is my favorite color? ")

##BEFORE: I Expect this to just print "Greetings" as a string, then for the user to guess the color yet
##          not get a response back

##AFTER: It did just as I thought it would. I assume the program did know you are answering a question, 
##          but since there is no actual piece of code that has the answer nor does it have an if/else statement,
##          it just accepted anything and ended the program. 