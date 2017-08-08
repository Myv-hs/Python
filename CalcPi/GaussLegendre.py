import sys
import decimal

decimals = int(sys.argv[1])
iterations = int(sys.argv[2])

iterated = 0

a0 = 1
b0 = 1/(2**0.5)
t0 = 1/4
p0 = 1

def Fanplus1 (an, bn):
	return (an+bn)/2

def Fbnplus1 (an, bn):
	return (an*bn)**0.5

def Ftnplus1 (an, bn, tn, pn):
	return tn-pn*((an-Fanplus1(an, bn))**2)

def Fpnplus1 (pn):
	return 2*pn

def Pi (al, bl, tl):
	return ((al+bl)**2)/(4*tl)

def iterate (an, bn, tn, pn):
	anplus1 = Fanplus1(an,bn)
	bnplus1 = Fbnplus1(an,bn)
	tnplus1 = Ftnplus1(an,bn,tn,pn)
	pnplus1 = Fpnplus1(pn)

	global iterated
	iterated = iterated + 1

	if iterated < iterations:
		iterate(anplus1, bnplus1, tnplus1, pnplus1)
	else:
		print(Pi(anplus1,bnplus1,tnplus1))


iterate(a0,b0,t0,p0)