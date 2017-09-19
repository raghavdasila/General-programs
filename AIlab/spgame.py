import os
from time import *
def mvup(G,P):G[P[0]],G[P[0]-3],P[0]=G[P[0]-3],G[P[0]],P[0]-3
def mvdn(G,P):G[P[0]],G[P[0]+3],P[0]=G[P[0]+3],G[P[0]],P[0]+3
def mvlt(G,P):G[P[0]],G[P[0]-1],P[0]=G[P[0]-1],G[P[0]],P[0]-1
def mvrt(G,P):G[P[0]],G[P[0]+1],P[0]=G[P[0]+1],G[P[0]],P[0]+1
def isSol(G):return G==range(1,9)+[0]
def getD(G):return sum(map(lambda x,y:(x-y)*((x>y)-(y>x)),G,range(1,10)))-G.index(0)-1
def genNext(G,P):
	OG,OP,next=G[:],P[:],[]
	if P[0]>2:
		mvup(G,P)
		next.append(G)
		G,P=OG[:],OP[:]
	if P[0]<6:
		mvdn(G,P)
		next.append(G)
		G,P=OG[:],OP[:]
	if P[0]%3:
		mvlt(G,P)
		next.append(G)
		G,P=OG[:],OP[:]
	if (P[0]-2)%3:
		mvrt(G,P)
		next.append(G)
		G,P=OG[:],OP[:]
	return next
def index(a,V):
	for i in xrange(0,len(V)):
		if V[i]==a:return i
	return -1
def getNext(N,V,B):
	next,mx=[],45
	for i in N:
		if getD(i)<mx and V.count(i)<2:
			if len(V)-index(i,V)!=2:mx,next=getD(i),i
	if next==[]:
		print "heuristic failed, backtracking"
		B[0]+=1
		return []
	V.append(next)
	return next[:]
def disp(G):
	for i in xrange(0,len(G)):
		print G[i],
		if not (i+1)%3:print
if __name__=="__main__":
	os.system('clear')
	G=[1,2,3,7,4,5,0,8,6]
	G=[4,1,3,7,2,6,5,8,0]
	V,B,P,steps=[G],[1],[G.index(0)],0
	while not isSol(G):
		disp(G)		
		sleep(1)
		os.system('clear')
		N=genNext(G,P)
		G=getNext(N,V,B)
		if G==[]:G=V[len(V)-B[0]]
		P,steps=[G.index(0)],steps+1
	disp(G)
	print "Steps",steps
#	for i in V:
		#disp(i)
#		print
