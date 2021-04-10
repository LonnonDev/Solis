
f = (open("text.sol", "r"))
text = []
for iterate in f:
	text += [iterate]
tokens = ["out", '"', "outln", "lnout"]
tokensdicc = {"out": "FUNC", '"': "STRING", "outln": "FUNC", "lnout": "FUNC"}

def pairs(o):
    if isinstance(o,dict):
        return o.items()
    else:
        return enumerate(o)

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

def outFUNC(text):
	print(text, end='')
def outlnFUNC(text):
	print(text, end='\n')
def lnoutFUNC(text):
	print(f"\n{text}", end='')

def Parser(text):
	iterate = 0
	while iterate != len(text):
		if text[iterate][0] == "out" and text[iterate][1] == "FUNC":
			if text[iterate+1][1] == "STRING" and text[iterate+2][1] == "STRING" and text[iterate+3][1] == "STRING":
				outFUNC(text[iterate+2][0])
		elif text[iterate][0] == "outln" and text[iterate][1] == "FUNC":
			if text[iterate+1][1] == "STRING" and text[iterate+2][1] == "STRING" and text[iterate+3][1] == "STRING":
				outlnFUNC(text[iterate+2][0])
		elif text[iterate][0] == "lnout" and text[iterate][1] == "FUNC":
			if text[iterate+1][1] == "STRING" and text[iterate+2][1] == "STRING" and text[iterate+3][1] == "STRING":
				lnoutFUNC(text[iterate+2][0])
		iterate += 1


LexedVersion = Lexer(text)
print("Lexed Version: ", LexedVersion)
Parser(LexedVersion)