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
	iterate = 0
	Tokenized = []
	lastchar = ""
	line = 1
	charnumber = 0
	while iterate != len(text):
		check = ""
		for char in text[iterate]:
			check += char
			#_ If newline add one to Line
			if "\n" in check:
				if text[iterate][0] == "#":
					Tokenized += [[f"{check[:-1]}/C", line, charnumber]]
					check = ""
				line += 1
				charnumber = 0
			elif check.replace(" ", "") in tokens or check in tokens:
				checkns = check.replace(" ", "")
				if check == "out":
					if text[iterate][0:5] == "outln":
						Tokenized += [["outln", line, charnumber]]
						check = ""
					else:
						Tokenized += [[check, line, charnumber]]
						check = ""
				elif checkns == "true" or checkns == "false":
					Tokenized += [[f"{check}/B", line, charnumber]]
				elif checkns == "none":
					Tokenized += [[f"{check}/U", line, charnumber]]
				else:
					Tokenized += [[check, line, charnumber]]
					check = ""
			elif char in tokens:
				print(char)
				#_ This gets the value inside of the of the Quotes
				if char == '"' and Tokenized[-1][0] == '"':
					Tokenized.pop(-1)
					Tokenized += [[f"{check[:-1]}/S", line, charnumber]]
					check = ""
				#_ Get's the inline var, var name
				elif char == '|' and Tokenized[-1][0] == '|':
					Tokenized.pop(-1)
					Tokenized += [[f"{check[:-1]}/V", line, charnumber]]
					check = ""
				#_ Get NotAssignment operator and name of the var
				elif check.replace(" ", "")[-2:] == "!=":
					Final = check
					Final == Final[:-3]
					Final = Final.replace(" ", "")
					Final = Final.split("=")
					Final[1] = "="
					Tokenized += [[f"{Final[0][:-1]}/D", line, charnumber]]
					Tokenized += [["!=", line, charnumber]]
					check = ""
				#_ Get Assignment operator and name of the var
				elif char == "=":
					Final = check
					Final == Final[:-3]
					Final = Final.replace(" ", "")
					Final = Final.split("=")
					Final[1] = "="
					Tokenized += [[f"{Final[0]}/D", line, charnumber]]
					Tokenized += [[Final[1], line, charnumber]]
					check = ""
				else:
					print(char)
					Tokenized += [[char, line, charnumber]]
					check = ""
			#_ See if the user typed a number and then define it
			elif char in numbers and Tokenized[-1][0] != '"' and Tokenized[iterate-1][0] != '"':
				if lastchar in numbers:
					newchar = Tokenized[-1][0].replace("/N", "")
					Tokenized[-1] = [f"{newchar+char}/N", line, charnumber]
					lastchar = char
				else:
					lastchar = char
					Tokenized += [[f"{char}/N", line, charnumber]]
			charnumber += 1
		iterate += 1
	Lexed = Lex(Tokenized)
	return Lexed

#* This Lexes the Tokenized list to make it understandable for the Parser
def Lex(Tokenized):
	iterate = 0
	Lexed = []
	iterate = 0
	while iterate != len(Tokenized):
		Tokenized[iterate][0] = Tokenized[iterate][0].replace(" ", "")
		print(Tokenized[iterate])
		iterate += 1
	print(Tokenized)
	while iterate != len(Tokenized):
		try:
			if Tokenized[iterate][0] == "var ":
				Lexed += [[
					"var",
					tokensdict["var "],
					Tokenized[iterate][1],
					Tokenized[iterate][2]
				]]
			else:
				Lexed += [[
					Tokenized[iterate][0], 
					tokensdict[Tokenized[iterate][0]],
					Tokenized[iterate][1],
					Tokenized[iterate][2]
				]]
		except:
			def CreateLexed(Name):
				Final = Tokenized[iterate][0]
				Final = Final[:-2]
				Lexed = [[
					Final,
				 	Name,
					Tokenized[iterate][1],
					Tokenized[iterate][2]
				]]
				return Lexed
			TokenizedEnd = Tokenized[iterate][0][-2:]
			Final = []
			if TokenizedEnd == "/S":
				Final = CreateLexed("STRING")
			elif TokenizedEnd == "/V":
				Final = CreateLexed("VAR")
			elif TokenizedEnd == "/D":
				Final = CreateLexed("VARNAME")
			elif TokenizedEnd == "/N":
				Final = CreateLexed("NUMBER")
			elif TokenizedEnd == "/C":
				Final = CreateLexed("COMMENT")
			elif TokenizedEnd == "/B":
				Final = CreateLexed("BOOLEAN")
			elif TokenizedEnd == "/U":
				Final = CreateLexed("NONETYPE")
			Lexed += Final
		iterate += 1
	return Lexed
