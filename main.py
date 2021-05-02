import sys
import msvcrt as m
import time

from src.lexer import Lexer
from src.parser import Parser
from onoff import toggle

try:
	f = (open(str(sys.argv[1]), "r"))
except:
	f = open("text.sol", "r")
text = []
for iterate in f:
	text += [iterate]
storedvars = {}

#-----------------------------------------------------------------|
#-                                                                |
#-                        Run The Code                            |
#-                                                                |
#-----------------------------------------------------------------|

LexedVersion = Lexer(text)
print(LexedVersion)
Parser(LexedVersion)
#time.sleep(10)
if toggle == True:
	try:
		def wait():
			m.getch()
		print("\nPress any key to continue...")
		wait()
	except:
		os.system('read -s -n 1 -p "Press any key to continue..."')
