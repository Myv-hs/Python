import sys
from random import randint
from TestEngQuestAns import Questions_and_Answers

correctAns = 0

def Test():
	global correctAns
	iRan = randint(0,len(Questions_and_Answers)-1)
	print(Questions_and_Answers[iRan][0])
	response = input().lower()
	if response == Questions_and_Answers[iRan][1]:
		print("That is correct")
		correctAns += 1
	else:
		print("Wrong")

def Main(arguments):
	print("This program will give you sentences with blanks \"___\".\nFill in the blacks with the correct word.\nTip: there are as many \"_\" as letters in the answer\n\n")

	currentQuestion = 0
	questions = 10

	try:
		if len(arguments) > 1:
			questions = int(arguments[1])
			print()
	except:
		print("\n",arguments[1],"is Invalid")
		print("use Int to choose how many questions")
		return

	while(currentQuestion<questions):
		Test()
		currentQuestion += 1
		print("%i / %i (total: %i)\n" %(correctAns, currentQuestion, questions))

Main(sys.argv)