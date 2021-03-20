f = (open("text.sol", "r"))
text = []
for x in f:
	text += [x]
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
	x = 0
	y = 0
	Lexed = []
	while x != len(text):
		check = ""
		for char in text[x]:
			check += char
			if check in tokens:
				Lexed += [check]
				check = ""
			elif char in tokens:
				Lexed += [char]
		x += 1

	return Lexed

def Tokeninator(text):
	x = 0
	Tokeninated = []
	while x != len(text):
		Tokeninated += [dict({text[x]: tokensdicc[text[x]]})]
		x += 1

	return Tokeninated



LexedVersion = Lexer(text)
TokinatedVersion = Tokeninator(LexedVersion)
print("Lexed Version: ", LexedVersion)
print("Tokinated Version: ", TokinatedVersion)