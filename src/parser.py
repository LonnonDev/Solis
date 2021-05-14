from src.builtins import *
from src.errorhandler import Error, ErrorType
from src.extras import *
from onoff import debugmode

outtypes = [
	"STRING", 
	"NUMBER", 
	"NONETYPE", 
	"BOOLEAN"
]

operations = [
	"ADD",
	"SUB",
	"MUL",
	"DIV",
	"MOD"
]

#-----------------------------------------------------------------|
#-                                                                |
#-                           Parser                               |
#-                                                                |
#-----------------------------------------------------------------|

#* This checks the Lexed code and parses it and runs it
def Parser(text):
	iterate = 0
	while iterate != len(text):
		try:
			if text[iterate][1] == "NUMBER":
				if text[iterate+1][1] in operations and text[iterate+2][1] == "NUMBER":
					answer = Math(text[iterate], text[iterate+1], text[iterate+2])
					del text[iterate]
					del text[iterate]
					text[iterate][0] = str(answer)
					iterate = 0
		except:
			pass
		iterate += 1
	iterate = 0
	text = ConvertVars(text)
	for iterate in range(len(text)):
		text[iterate] = tuple(text[iterate])
	if debugmode == True:
		print(text)
	for iterate in range(len(text)):
		#$ Look for the word out and make sure it has the type of FUNC
		if text[iterate][1] == "FUNC":
			try:
				if text[iterate+1][1] in outtypes:
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
	for iterate in range(len(lexed)):
		lexed[iterate][0] = lexed[iterate][0].replace(" ", "")
		iterate += 1
	for iterate in range(len(lexed)):
		if not storedvars:
			storedvars = {}
		if lexed[iterate][0] == "var" and lexed[iterate][1] == "DECLARE":
			def AddVar(value, datatype):
				try:
					newdict = {lexed[iterate+1][0]: [
						value,
						datatype,
						lexed[iterate-1][2],
						lexed[iterate+3][3]
					]}
				except:
					newdict = {lexed[iterate+1][0]: [
						'none', 
						'NONETYPE', 
						lexed[iterate+1][2], 
						lexed[iterate+3][3]
					]}
				return newdict
			if lexed[iterate+2][0] == "!=" and lexed[iterate+2][1] == "NOTASSIGNMENT":
				value, datatype = Opposite(lexed[iterate+3])
				newdict = AddVar(value, datatype)
			else:
				newdict = AddVar(lexed[iterate+3][0], lexed[iterate+3][1])
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

def Math(first, operation, second):
	final = eval("1 + 1")
	return final