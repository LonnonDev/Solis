import sys
import msvcrt as m

try:
	f = (open(str(sys.argv[1]), "r"))
except:
	f = open("text.sol", "r")
text = []
for iterate in f:
	text += [iterate]
tokens = ["out", '"', "outln", "vent"]
tokensdicc = {"out": "FUNC", '"': "STRING", "outln": "FUNC", "vent": "FUNC"}

#* Pairs function from lua
def pairs(o):
    if isinstance(o,dict):
        return o.items()
    else:
        return enumerate(o)

#$#################################################################
#$																  #
#$							  Lexer       						  #
#$																  #
#$#################################################################

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
				if char == '"' and Lexed[-1] == '"':
					Lexed += [check[:-1]]
					Lexed += [char]
					check = ""
				else:
					Lexed += [char]
					check = ""
		iterate += 1
	iterate = 0
	Tokenized = []
	while iterate != len(Lexed):
		try:
			Tokenized += [[Lexed[iterate], tokensdicc[Lexed[iterate]]]]
		except:
			Tokenized += [[Lexed[iterate], "STRING"]]
		iterate += 1

	return Tokenized

#$#################################################################
#$																  #
#$						Built In Functions						  #
#$																  #
#$#################################################################

def outFUNC(text):
	text = text.replace("\\n", "\n")
	print(f"{text}", end='')
def outlnFUNC(text):
	text = text.replace("\\n", "\n")
	print(f"{text}", end='\n')
def vent():
	try:
		def wait():
			m.getch()
		print("\n\nPress any key to continue...")
		wait()
	except:
		os.system('read -s -n 1 -p "Press any key to continue..."')
	exit()

#$#################################################################
#$																  #
#$							  Parser    						  #
#$																  #
#$#################################################################

#* This checks the Lexed code and parses it and runs it 
def Parser(text):
	iterate = 0
	while iterate != len(text):
		if text[iterate][0] == "out" and text[iterate][1] == "FUNC":
			if text[iterate+1][1] == "STRING" and text[iterate+2][1] == "STRING" and text[iterate+3][1] == "STRING":
				outFUNC(text[iterate+2][0])
		elif text[iterate][0] == "outln" and text[iterate][1] == "FUNC":
			if text[iterate+1][1] == "STRING" and text[iterate+2][1] == "STRING" and text[iterate+3][1] == "STRING":
				outlnFUNC(text[iterate+2][0])
		elif text[iterate][0] == "vent" and text[iterate][1] == "FUNC":
			vent()
		iterate += 1


LexedVersion = Lexer(text)
Parser(LexedVersion)
try:
	import msvcrt as m
	def wait():
		m.getch()
	print("\n\nPress any key to continue...")
	wait()
except:
	os.system('read -s -n 1 -p "Press any key to continue..."')