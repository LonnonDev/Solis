
#-----------------------------------------------------------------|
#-                                                                |
#-                           Extras                               |
#-                                                                |
#-----------------------------------------------------------------|

#* Gets opposite of an input
def Opposite(text):
	value = text[0]
	datatype = text[1]
	finalvalue = ""
	if datatype == "STRING":
		finalvalue = value[::-1]
	elif datatype == "NUMBER":
		finalvalue = f"-{value}"
	elif datatype == "BOOLEAN":
		finalvalue = value.capitalize()
		finalvalue = str(not eval(finalvalue)).lower()
	elif datatype == "NONETYPE":
		finalvalue = "none"
	return finalvalue, datatype