tokens = [
	"out",
	'"',
	"outln",
	"vent",
	"var ",
	"=",
	"|"
]
tokensdict = {
	"out": "FUNC",
	'"': "STRING",
	"outln": "FUNC",
	"vent": "FUNC",
	"var ": "DECLARE",
	"=": "ASSIGNMENT",
	"|": "VARUSE"
}
