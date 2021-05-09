tokens = [
	"out",
	'"',
	"outln",
	"vent",
	"var ",
	"=",
	"|",
	" none",
	"if ",
	"{",
	"}"
]
tokensdict = {
	"out": "FUNC",
	'"': "STRING",
	"outln": "FUNC",
	"vent": "FUNC",
	"var ": "DECLARE",
	"=": "ASSIGNMENT",
	"|": "VARUSE",
	" none": "NONETYPE",
	"if ": "IFSTATEMENT",
	"{": "STARTSCOPE",
	"}": "ENDSCOPE"
}
