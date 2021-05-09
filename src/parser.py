from src.builtins import *
from src.errorhandler import Error, ErrorType
from onoff import debugmode

#-----------------------------------------------------------------|
#-                                                                |
#-                           Parser                               |
#-                                                                |
#-----------------------------------------------------------------|

#* This checks the Lexed code and parses it and runs it
def Parser(text):
	iterate = 0
	text = ConvertVars(text)
	if debugmode == True:
		print(text)
	while iterate != len(text):
		#$ Look for the word out and make sure it has the type of FUNC
		if text[iterate][1] == "FUNC":
			try:
				if text[iterate+1][1] == "STRING" and not text[iterate+1][0] == '"' or text[iterate+1][1] == "NUMBER" or text[iterate+1][1] == "NONETYPE":
					if text[iterate][0] == "out":
						outFUNC(text[iterate+1][0])
					elif text[iterate][0] == "outln":
						outlnFUNC(text[iterate+1][0])
				elif text[iterate+1][1] == "STRING" and text[iterate+1][0] == '"':
					Error(ErrorType.INVALID_STRING, text[iterate][2]).errout()
			except:
				pass
			#$ Look for the word vent and make sure it has the type of FUNC
			if text[iterate][0] == "vent":
				break
		iterate += 1

#* Converts the vars to their values
def ConvertVars(lexed):
	storedvars = {}
	iterate = 0
	while iterate != len(lexed):
		lexed[iterate][0] = lexed[iterate][0].replace(" ", "")
		iterate += 1
	iterate = 0
	while iterate != len(lexed):
		if not storedvars:
			storedvars = {}
		if lexed[iterate][0] == "var" and lexed[iterate][1] == "DECLARE":
			try:
				newdict = {lexed[iterate+1][0]: [
					lexed[iterate+3][0],
					lexed[iterate+3][1], 
					lexed[iterate-1][2],
					lexed[iterate+3][3]
				]}
				storedvars = {**storedvars, **newdict}
			except:
				newdict = {lexed[iterate+1][0]: ['none', 'NONE', lexed[iterate+1][2]]}
				storedvars = {**storedvars, **newdict}
		elif lexed[iterate][1] == "VAR":
			var = storedvars[lexed[iterate][0]]
			lexed[iterate] = [
				var[0], 
				var[1], 
				var[2], 
				var[3]
			]
		iterate += 1
	return lexed
