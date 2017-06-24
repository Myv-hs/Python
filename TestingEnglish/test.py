import sys
def clear_screen(): print('\033c')
clear_screen()
print("Hello")
row = 3
col = 0
response = input("\033[%i;%iH" %(row, col))
if response == "hello buddy":
	print("Yay this works")