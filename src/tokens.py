tokens = [
	#% Vars
	"var ",
	"=",
	"!=",
	"|",

	#% Functions
  	"out",
	"outln",
	"vent",

	#% Types
	'"',
	"none",
	"false",
	"true",

	#% Scopes
	"{",
	"}",

	#% If Statements/Conditions
	"if ",
	" & ",
	" | ",
	" !== "

	#% Comment
	"#",

	#% Math
	"+",
	"-",
	"*",
	"/",
	"%",
]
tokensdict = {
	#% Vars
	"var ": "DECLARE",
  	"|": "VARUSE",
	"=": "ASSIGNMENT",
	"!=": "NOTASSIGNMENT",

	#% Functions
  	"out": "FUNC",
	"outln": "FUNC",
	"vent": "FUNC",

	#% Types
	'"': "STRING",
	" none": "NONETYPE",
	"true": "BOOLEAN",
	"false": "BOOLEAN",
	
	#% Scopes
	"{": "STARTSCOPE",
	"}": "ENDSCOPE",

	#% If Statements/Conditions
	"if ": "IFSTATEMENT",
	" & ": "AND",
	" | ": "OR",
	" !== ": "NOTEQUALTO",

	#% Comments
	"#": "COMMENT",

	#% Math
	"+": "ADD",
	"-": "SUB",
	"*": "MUL",
	"/": "DIV",
	"%": "MOD",
}

ValidNumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

TokenizedEndList = [
	"S",
	"V",
	"D",
	"N",
	"C",
	"B",
	"U",
]
TokenizedEndDict = {
	"S": "STRING",
	"V": "VAR",
	"D": "VARNAME",
	"N": "NUMBER",
	"C": "COMMENT",
	"B": "BOOLEAN",
	"U": "NONETYPE",
}