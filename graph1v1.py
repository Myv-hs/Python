import sys
import pickle

def load(file):
	f = open(file,'r')
	return pickle.load(f)

def save(file, obj):
	f = open(file,'w')
	pickle.dump(obj,f)


class graph:
	def __init__(self,size,names,matrix):
		self.size = size
		self.names = names
		self.matrix = matrix

	def matrixToString(self):
		out = ""
		for i in range(self.size):
			#out += str(j)+" "
			for each in [str(self.matrix[i][j]) for j in range(self.size)]:
				out+=each
			if i != self.size-1:
				out+="\n"

		return out

	def __str__(self):
		return str(self.names)

	def addPlayer(self,name):
		self.size+=1
		self.names.append(name)
	
		for l in self.matrix:
			l.append(0)
		self.matrix.append([0 for i in range(self.size)])

	def loggame(self,w,l):
		self.matrix[w][l]+=1

def main(graph):
	g = load(graph)
	if(len(sys.argv)<2):
		return
	if(sys.argv[1]=="p++" and (len(sys.argv)==3)):
		g.addPlayer(sys.argv[2])

	elif(sys.argv[1]=="ls"):
		print(g)
		return

	elif(sys.argv[1]=="mtrx"):
		print(g.matrixToString())
		return

	elif(sys.argv[1][1]==">"):
		print(str(sys.argv[1][0])+">"+str(sys.argv[1][2]))
		g.loggame(int(sys.argv[1][0]),int(sys.argv[1][2]))

	elif(sys.argv[1]=="reset"):
		makeGraphFile(graph)
		return

	elif((sys.argv[2]=="vanquished" or sys.argv[2]=="beat") and (len(sys.argv)==4)):
		print(str(g.names.index(sys.argv[1]))+">"+str(g.names.index(sys.argv[3])))
		g.loggame(g.names.index(sys.argv[1]),g.names.index(sys.argv[3]))
	else:
		return

	save(graph,g)

def makeGraphFile(name):
	g = graph(0,[],[])
	save(name,g)

filename="chess.graph"
print(len(sys.argv))
print(sys.argv)
main(filename)
#mtrx = [[1,0,0],[0,1,0],[0,0,1]]
#print(mtrx)