import sys
import msvcrt as m
import time

try:
	f = (open(str(sys.argv[1]), "r"))
except:
	f = open("text.sol", "r")
text = []
for iterate in f:
	text += [iterate]
tokens = [
	"out", 
	'"', 
	"outln",
	"vent", 
	"var", 
	"=", 
	"|"
]
tokensdicc = {
	"out": "FUNC", 
	'"': "STRING", 
	"outln": "FUNC", 
	"vent": "FUNC", 
	"var": "DECLARE", 
	"=": "ASSIGNMENT", 
	"|": "VARUSE"
}
storedvars = {}

#* Pairs function from lua
def pairs(o):
    if isinstance(o,dict):
        return o.items()
    else:
        return enumerate(o)

#-----------------------------------------------------------------|
#-                                                                |
#-                           Lexer                                |
#-                                                                |
#-----------------------------------------------------------------|

#* This turns the code into a Lexed List that the Parser can understand and run
def Lexer(text):
	for i, index in pairs(text):
		text[i] = text[i].rstrip("\n")
	iterate = 0
	Lexed = []
	while iterate != len(text):
		check = ""
		for char in text[iterate]:
			check += char
			if check in tokens:
				if check == "out":
					if text[iterate][0:5] == "outln":
						Lexed += ["outln"]
						check = ""
					else:
						Lexed += [check]
						check = ""
				else:
					Lexed += [check]
					check = ""
			elif char in tokens:
				#_ This gets the value inside of the of the Quotes
				if char == '"' and Lexed[-1] == '"':
					Lexed += [f"{check[:-1]}/S"]
					Lexed += [f"{char}"]
					check = ""
				#_ Get's the inline var, var name
				elif char == '|' and Lexed[-1] == '|':
					Lexed += [f"{check[:-1]}/V"]
					Lexed += [f"{char}"]
					check = ""
				#_ Get Assignment operator and name of the var
				elif char == "=":
					Final = check
					Final == Final[:-3]
					Final = Final.replace(" ", "")
					Final = Final.split("=")
					Final[1] = "="
					Lexed += Final
					check = ""	
				else:
					Lexed += [char]
					check = ""
		iterate += 1
	return Lexed

#* This tokenizes to make it understandable for the Parser
def Tokinzier(Lexed):
	iterate = 0
	Tokenized = []
	while iterate != len(Lexed):
		try:
			Tokenized += [[Lexed[iterate], tokensdicc[Lexed[iterate]]]]
		except:
			LexedEnd = Lexed[iterate][-2:]
			if LexedEnd == "/S":
				Final = Lexed[iterate]
				Final = Final[:-2]
				Tokenized += [[Final, "STRING"]]
			elif LexedEnd == "/V":
				Final = Lexed[iterate]
				Final = Final[:-2]
				Tokenized += [[Final, "VAR"]]
			elif Lexed[iterate-1] == "var":
				Tokenized += [[Lexed[iterate], "VARNAME"]]
		iterate += 1
	return Tokenized
	

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
	try:
		def wait():
			m.getch()
		print("\n\nPress any key to continue...")
		wait()
	except:
		os.system('read -s -n 1 -p "Press any key to continue..."')
	exit()

#-----------------------------------------------------------------|
#-                                                                |
#-                           Parser                               |
#-                                                                |
#-----------------------------------------------------------------|

#* This checks the Lexed code and parses it and runs it 
def Parser(text):
	iterate = 0
	while iterate != len(text):
		#_ Look for the word out and make sure it has the type of FUNC
		if text[iterate][1] == "FUNC":
			if text[iterate+1][1] == "STRING" and text[iterate+2][1] == "STRING" and text[iterate+3][1] == "STRING":
				if text[iterate][0] == "out":
					outFUNC(text[iterate+2][0])
				elif text[iterate][0] == "outln":
					outlnFUNC(text[iterate+2][0])
		elif text[iterate][0] == "vent" and text[iterate][1] == "FUNC":
			vent()
		#_ Look for the word var and make sure it has the type of DECLARE
		elif text[iterate][0] == "var" and text[iterate][1] == "DECLARE":
			print()
		iterate += 1

#-----------------------------------------------------------------|
#-                                                                |
#-                        Run The Code                            |
#-                                                                |
#-----------------------------------------------------------------|

LexedVersion = Lexer(text)
Tokinzied = Lexer(LexedVersion)
Parser(Tokinzied)
#time.sleep(10)
try:
	def wait():
		m.getch()
	print("\n\nPress any key to continue...")
	wait()
except:
	os.system('read -s -n 1 -p "Press any key to continue..."')
