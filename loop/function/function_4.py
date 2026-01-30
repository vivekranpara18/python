import shutil
# 1	 Without return value without argument
width = shutil.get_terminal_size().columns
def printline():
    print("-"*100)

# 2	Without return value with argument

def printmessage(message):
    print(message.center(width))

printline()
printmessage('THE EASYLEARN')
printline()