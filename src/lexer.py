from src.tokens import tokens, tokensdict
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

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
		line = 1
		for char in text[iterate]:
			check += char
			if check in tokens:
				if check == "out":
					if text[iterate][0:5] == "outln":
						Tokenized += [["outln", line]]
						check = ""
					else:
						Tokenized += [[check, line]]
						check = ""
				else:
					Tokenized += [[check, line]]
					check = ""
			elif char in tokens:
				#_ This gets the value inside of the of the Quotes
				if char == '"' and Tokenized[-1][0] == '"':
					Tokenized.pop(-1)
					Tokenized += [[f"{check[:-1]}/S", line]]
					check = ""
				#_ Get's the inline var, var name
				elif char == '|' and Tokenized[-1][0] == '|':
					Tokenized.pop(-1)
					Tokenized += [[f"{check[:-1]}/V", line]]
					check = ""
				#_ Get Assignment operator and name of the var
				elif char == "=":
					Final = check
					Final == Final[:-3]
					Final = Final.replace(" ", "")
					Final = Final.split("=")
					Final[1] = "="
					Tokenized += [[f"{Final[0]}/D", line]]
					Tokenized += [[Final[1], line]]
					check = ""
				else:
					Tokenized += [[char, line]]
					check = ""
			elif char in numbers and Tokenized[-1][0] != '"' and Tokenized[iterate-1][0] != '"':
				Tokenized += [[f"{char}/N", line]]
			elif check == "\\n":
				line += 1
		iterate += 1
	Lexed = Lex(Tokenized)
	print(Lexed)
	return Lexed

#* This Lexes the Tokenized list to make it understandable for the Parser
def Lex(Tokenized):
	iterate = 0
	Lexed = []
	while iterate != len(Tokenized):
		try:
			if Tokenized[iterate][0] == "var ":
				Lexed += [["var", tokensdict["var "]]]
			else:
				Lexed += [[Tokenized[iterate][0], tokensdict[Tokenized[iterate][0]]]]
		except:
			TokenizedEnd = Tokenized[iterate][0][-2:]
			if TokenizedEnd == "/S":
				Final = Tokenized[iterate][0]
				Final = Final[:-2]
				Lexed += [[Final, "STRING"]]
			elif TokenizedEnd == "/V":
				Final = Tokenized[iterate][0]
				Final = Final[:-2]
				Lexed += [[Final, "VAR"]]
			elif TokenizedEnd == "/D":
				Final = Tokenized[iterate][0]
				Final = Final[:-2]
				Lexed += [[Final, "VARNAME"]]
			elif TokenizedEnd == "/N":
				Final = Tokenized[iterate][0]
				Final = Final[:-2]
				Lexed += [[Final, "NUMBER"]]
		iterate += 1
	return Lexed
