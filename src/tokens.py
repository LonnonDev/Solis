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
	" none",

	#% Scopes
	"{",
	"}",

	#% If Statements/Conditions
	"if ",
	" & ",
	" | ",
	" !== "
]
tokensdict = {
	#% Vars
	"var ": "DECLARE",
	"=": "ASSIGNMENT",
	"!=": "NOTASSIGNMENT",
	"|": "VARUSE",

	#% Functions
  	"out": "FUNC",
	"outln": "FUNC",
	"vent": "FUNC",

	#% Types
	'"': "STRING",
	" none": "NONETYPE",
	
	#% Scopes
	"{": "STARTSCOPE",
	"}": "ENDSCOPE",

	#% If Statements/Conditions
	"if ": "IFSTATEMENT",
	" & ": "AND",
	" | ": "OR",
	" !== ": "NOTEQUALTO",
}
