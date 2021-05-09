tokens = [
	"out",
	'"',
	"outln",
	"vent",
	"var ",
	"=",
	"|",
	" none"
]
tokensdict = {
	"out": "FUNC",
	'"': "STRING",
	"outln": "FUNC",
	"vent": "FUNC",
	"var ": "DECLARE",
	"=": "ASSIGNMENT",
	"|": "VARUSE",
	" none": "NONETYPE"
}
