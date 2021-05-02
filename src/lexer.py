from src.tokens import tokens, tokensdict

#* Pairs function from lua
def pairs(o):
    if isinstance(o, dict):
        return o.items()
    else:
        return enumerate(o)


#-----------------------------------------------------------------|
#-                                                                |
#-                    Lexer & Tokenizier                          |
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
					Lexed[-1] = ""
					Lexed += [f"{check[:-1]}/S"]
					check = ""
				#_ Get's the inline var, var name
				elif char == '|' and Lexed[-1] == '|':
					Lexed[-1] = ""
					Lexed += [f"{check[:-1]}/V"]
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
	Tokenizied = Tokinzier(Lexed)
	return Tokenizied

#* This tokenizes to make it understandable for the Parser
def Tokinzier(Lexed):
	iterate = 0
	Tokenized = []
	while iterate != len(Lexed):
		try:
			Tokenized += [[Lexed[iterate], tokensdict[Lexed[iterate]]]]
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
