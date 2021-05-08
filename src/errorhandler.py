import sys
from Color_Console import ctext

from src.errortype import ErrorType

#-----------------------------------------------------------------|
#-                                                                |
#-                        Error Handler                           |
#-                                                                |
#-----------------------------------------------------------------|

#* This just gets the filename of the inputted file
def GetFileName():
	file = ""
	try:
		file = str(sys.argv[1])
		f = (open(file, "r"))
	except:
		file = "text.sol"
		f = open(file, "r")
	return file

#* Class containing ErrorType, and maybe file and line if needed
class Error(): 
	#* Initializer, takes ErrorType and optionally file and line
	def __init__(self,err,line=None,file=None): 
		#$ If err is of type ErrorType, set initializer values, otherwise, raise a TypeError.
		if isinstance(err,ErrorType):
			#_ Set fields equal to initializer values
			self.err = err
			self.file = file or GetFileName()
			self.line = line
		else:
			raise TypeError("Error(err,file,line) -- type of err must be ErrorType enum!")
	def __str__(self):
		#$ If no file AND no line,
		if self.file is None and self.line is None:
			return f"Error:\n    {self.err}"
		#$ Else if there is a file erroring but no specific line,
		elif self.line is None:
			return f"Error in file '{self.file}'\n    {self.err}"
		#$ Otherwise (if there is a file and a line),
		else:
			return f"Error in file '{self.file}' on line {self.line}\n    {str(self.err)}"
	def errout(self):
		ctext(str(self), text="red", bg="black")