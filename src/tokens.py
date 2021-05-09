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

	#% Comment
	"#",
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
}
