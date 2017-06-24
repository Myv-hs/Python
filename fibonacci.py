import sys

highestNum = 255
if len(sys.argv)>1:
	try:
		highestNum = int(sys.argv[1])
	except:
		print(" Use an int to define series limit")

a = 1
b = 1
c = 0

while(a<highestNum):
	print(a)
	c = a+b
	a = b
	b = c
