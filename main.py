import sys
import msvcrt as m
import time

from src.lexer import Tokenize
from src.parser import Parser
from onoff import toggle

file = ""
try:
	file = str(sys.argv[1])
	f = (open(file, "r"))
except:
	file = "text.sol"
	f = open(file, "r")
text = []
for iterate in f:
	text += [r"{}".format(iterate)]

#-----------------------------------------------------------------|
#-                                                                |
#-                        Run The Code                            |
#-                                                                |
#-----------------------------------------------------------------|

LexedVersion = Tokenize(text)
Parser(LexedVersion)
if toggle == True:
	print("\nPress any key to continue...")
	m.getch()
