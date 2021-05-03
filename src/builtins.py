import sys
import msvcrt as m
import time

#-----------------------------------------------------------------|
#-                                                                |
#-                      Built in Functions                        |
#-                                                                |
#-----------------------------------------------------------------|

#& Prints text without a newline
def outFUNC(text):
	text = text.replace("\\n", "\n")
	print(f"{text}", end='')

#& Prints text with a new line at the end
def outlnFUNC(text):
	text = text.replace("\\n", "\n")
	print(f"{text}", end='\n')
    
#& Exits the program
def vent():
	exit()
