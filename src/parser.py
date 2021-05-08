from src.builtins import *
from src.errorhandler import Error, ErrorType

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
		if text[iterate][1] == "FUNC":
			print(text[iterate-1])
			try:
				if text[iterate+1][1] == "STRING" and not text[iterate+1][0] == '"' or text[iterate+1][1] == "NUMBER":
					if text[iterate][0] == "out":
						outFUNC(text[iterate+1][0])
					elif text[iterate][0] == "outln":
						outlnFUNC(text[iterate+1][0])
				elif text[iterate+1][1] == "STRING" and text[iterate+1][0] == '"':
					Error().throw(ErrorType.InvalidString, text[iterate][2])
			except:
				pass
			#_ Look for the word vent and make sure it has the type of FUNC
			if text[iterate][0] == "vent":
				break
		iterate += 1

#* Converts the var with a space to var with no space
def ConvertVars(lexed):
	storedvars = {}
	iterate = 0
	while iterate != len(lexed):
		if not storedvars:
			storedvars = {}
		if lexed[iterate][0] == "var" and lexed[iterate][1] == "DECLARE":
			newdict = {lexed[iterate+1][0]: [lexed[iterate+3][0], lexed[iterate+3][1]]}
			storedvars = {**storedvars, **newdict}
		elif lexed[iterate][1] == "VAR":
			var = storedvars[lexed[iterate][0]]
			lexed[iterate] = [var[0], var[1]]
		iterate += 1
	return lexed
