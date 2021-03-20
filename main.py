f = (open("text.sol", "r"))
text = []
for x in f:
	text += [x]
print(text)
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
		print(text[x])
		for char in text[x]:
			check += char
			if check in tokens:
				Lexed += [check]
				check = ""
			elif char in tokens:
				Lexed += [char]
		x += 1

	return Lexed

LexedVersion = Lexer(text)
print(LexedVersion)