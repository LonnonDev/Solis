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
Parser(file, LexedVersion)
#time.sleep(10)
if toggle == True:
	try:
		def wait():
			m.getch()
		print("\nPress any key to continue...")
		wait()
	except:
		os.system('read -s -n 1 -p "Press any key to continue..."')
