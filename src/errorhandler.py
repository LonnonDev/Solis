from enum import Enum
import sys
from Color_Console import ctext

#-----------------------------------------------------------------|
#-                                                                |
#-                        Error Handler                           |
#-                                                                |
#-----------------------------------------------------------------|

#* This Just gets the filename of the inputted file
def GetFileName():
	file = ""
	try:
		file = str(sys.argv[1])
		f = (open(file, "r"))
	except:
		file = "text.sol"
		f = open(file, "r")
	return file

#* This Creates Errors and prints them to console
class Error():
	def __init__(self):
		self.file = GetFileName()

	#_ This Throws an error into the console
	def throw(self, errortype, line, message: str = ""):
		if errortype == ErrorType.InvalidString:
			if message == "":
				message = "Invalid String Format"
			ErrorMessage = Error().create(message, line)
			ctext(ErrorMessage, text="red", bg="black")
	
	#_ This Creates errors and returns them to be printed
	def create(self, message: None, line: None):
		if message and line:
			return f"In {self.file} at line {line}\n    {message}"
		elif message and not line:
			return f"In {self.file}\n\t{message}"
		elif not message and line:
			return f"In {self.file} at line {line}"
		else:
			return f"In {self.file}"

#* Enum Class for ErrorTypes
class ErrorType(Enum):
	InvalidString = 0
