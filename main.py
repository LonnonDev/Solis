import parser

f = (open("text.sol", "r"))
text = []
for iterate in f:
	text += [iterate]
tokens = ["out", '"', "hen"]
tokensdicc = {"out": "FUNC", '"': "STRING", "hen": "FUNC"}

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
				Lexed += [check]
				check = ""
			elif char in tokens:
				Lexed += [char]
		iterate += 1
	iterate = 0
	Tokeninated = []
	while iterate != len(Lexed):
		Tokeninated += [[Lexed[iterate], tokensdicc[Lexed[iterate]]]]
		iterate += 1

	return Tokeninated

def outFUNC(text):
	print(text)

def Parser(text):
	iterate = 0
	while iterate != len(text):
		iterate += 1
		iterateplusone = iterate + 1
		iterateminusone = iterate - 1
		if text[iterateminusone][0] == "out" and text[iterateminusone][1] == "FUNC":
			if text[iterate][1] == "STRING" and text[iterateplusone][1] == "STRING":
				print("yes")
	return "hi"


LexedVersion = Lexer(text)
print("Lexed Version: ", LexedVersion)
#print("Parsed Version: ", ParsedVersion)