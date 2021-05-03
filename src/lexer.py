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

#* This turns the code into a Tokenized List and then Turns that into a Lexed List that the Parser can understand and run
def Tokenize(text):
	for i, index in pairs(text):
		text[i] = text[i].rstrip("\n")
	iterate = 0
	Tokenized = []
	while iterate != len(text):
		check = ""
		for char in text[iterate]:
			check += char
			if check in tokens:
				if check == "out":
					if text[iterate][0:5] == "outln":
						Tokenized += ["outln"]
						check = ""
					else:
						Tokenized += [check]
						check = ""
				else:
					Tokenized += [check]
					check = ""
			elif char in tokens:
				#_ This gets the value inside of the of the Quotes
				if char == '"' and Tokenized[-1] == '"':
					Tokenized[-1] = ""
					Tokenized += [f"{check[:-1]}/S"]
					check = ""
				#_ Get's the inline var, var name
				elif char == '|' and Tokenized[-1] == '|':
					Tokenized[-1] = ""
					Tokenized += [f"{check[:-1]}/V"]
					check = ""
				#_ Get Assignment operator and name of the var
				elif char == "=":
					Final = check
					Final == Final[:-3]
					Final = Final.replace(" ", "")
					Final = Final.split("=")
					Final[1] = "="
					Tokenized += [f"{Final[0]}/D"]
					Tokenized += Final[1]
					check = ""
				else:
					Tokenized += [char]
					check = ""
		iterate += 1
	Lexed = Lex(Tokenized)
	return Lexed

#* This Lexes the Tokenized list to make it understandable for the Parser
def Lex(Tokenizied):
	iterate = 0
	Tokenized = []
	while iterate != len(Tokenizied):
		try:
			if Tokenizied[iterate] == "var ":
				Tokenized += [["var", tokensdict["var "]]]
			else:
				Tokenized += [[Tokenizied[iterate], tokensdict[Tokenizied[iterate]]]]
		except:
			TokeniziedEnd = Tokenizied[iterate][-2:]
			if TokeniziedEnd == "/S":
				Final = Tokenizied[iterate]
				Final = Final[:-2]
				Tokenized += [[Final, "STRING"]]
			elif TokeniziedEnd == "/V":
				Final = Tokenizied[iterate]
				Final = Final[:-2]
				Tokenized += [[Final, "VAR"]]
			elif TokeniziedEnd == "/D":
				Final = Tokenizied[iterate]
				Final = Final[:-2]
				Tokenized += [[Final, "VARNAME"]]
		iterate += 1
	return Tokenized
