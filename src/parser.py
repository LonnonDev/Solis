from src.builtins import *

#-----------------------------------------------------------------|
#-                                                                |
#-                           Parser                               |
#-                                                                |
#-----------------------------------------------------------------|

#* This checks the Lexed code and parses it and runs it
def Parser(text):
	iterate = 0
	text = ConvertVars(text)
	while iterate != len(text):
		#_ Look for the word out and make sure it has the type of FUNC
		print(text[iterate][1])
		if text[iterate][1] == "FUNC":
			try:
				if text[iterate+1][0][1] == "STRING" and not text[iterate+1][0] == '"' or text[iterate+1][1] == "NUMBER":
					if text[iterate][0] == "out":
						outFUNC(text[iterate+1][0])
					elif text[iterate][0] == "outln":
						outlnFUNC(text[iterate+1][0])
				elif text[iterate+1][1] == "STRING" and text[iterate+1][0] == '"':
					print(f"""\rToo Little or Too many \"'s at 
{text[iterate][0]} {text[iterate+1][0]}\n""")
			except:
				pass
			#_ Look for the word vent and make sure it has the type of FUNC
			if text[iterate][0] == "vent":
				exit()
		iterate += 1

def ConvertVars(lexed):
	storedvars = {}
	iterate = 0
	while iterate != len(lexed):
		if not storedvars:
			storedvars = {}
		if lexed[iterate][0] == "var" and lexed[iterate][1] == "DECLARE":
			newdict = {lexed[iterate+1][0]: lexed[iterate+3][0]}
			storedvars = {**storedvars, **newdict}
		elif lexed[iterate][1] == "VAR":
			lexed[iterate] = storedvars[lexed[iterate][0]]
		iterate += 1
	return lexed
