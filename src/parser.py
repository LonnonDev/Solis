from src.builtins import *

#-----------------------------------------------------------------|
#-                                                                |
#-                           Parser                               |
#-                                                                |
#-----------------------------------------------------------------|

#* This checks the Lexed code and parses it and runs it
def Parser(text):
	iterate = 0
	while iterate != len(text):
		#_ Look for the word out and make sure it has the type of FUNC
		if text[iterate][1] == "FUNC":
			try:
				if text[iterate+1][1] == "STRING" and not text[iterate+1][0] == '"':
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
				vent()
		#_ Look for the word var and make sure it has the type of DECLARE
		elif text[iterate][0] == "var" and text[iterate][1] == "DECLARE":
			print(text[iterate])
			declarevar(text[iterate])
		iterate += 1
