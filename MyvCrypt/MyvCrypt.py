import sys
from charcodes import codes

space = " "
eNDe = sys.argv[1]
psswrd = sys.argv[2]
inputstrings = sys.argv[3:len(sys.argv)]
string = space.join(inputstrings)
charlist = list(string)
inputNumberString = ''
inputNumber = 0
psswrdNumberString = ''
psswrdNumber = 0

for i in psswrd:
	print(i)
	for j in codes:
		if i == j[0]:
			psswrdNumberString += j[1]

for i in charlist:
	print(i)
	for j in codes:
		if i == j[0]:
			inputNumberString += j[1]

print(inputNumberString)
inputNumber = int(inputNumberString)
psswrdNumber = int(psswrdNumberString)

print(inputNumber*psswrdNumber)