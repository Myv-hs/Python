import sys

space = " "
inputstrings = sys.argv[1:len(sys.argv)]
string = space.join(inputstrings)
letterlist = list(string)
charlist = []

for i in range(0, len(letterlist)):
	charlist.append(ord(letterlist[i]))

for i in range(0, len(charlist)):
	if charlist[i] == 32:
		charlist[i] = 32
	elif charlist[i]%2 == 0:
		charlist[i]=charlist[i]-3
	else:
		charlist[i]=charlist[i]+3

newletterlist = [chr(i) for i in charlist]

newstring = ""
for i in range(0,len(newletterlist)):
	newstring += newletterlist[i]

print(newstring)