
#-----------------------------------------------------------------|
#-                                                                |
#-                      Built in Functions                        |
#-                                                                |
#-----------------------------------------------------------------|

#& Prints text without a newline
def outFUNC(text):
	text = text.replace("\\n", "\n")
	print(f"{text}", end='')

#& Prints text with a new line at the end
def outlnFUNC(text):
	text = text.replace("\\n", "\n")
	print(f"{text}", end='\n')
    
#& Exits the program
def vent():
	try:
		def wait():
			m.getch()
		print("\n\nPress any key to continue...")
		wait()
	except:
		os.system('read -s -n 1 -p "Press any key to continue..."')
	exit()