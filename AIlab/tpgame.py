#Tic-Tac-Toe game between two bots, both try to not lose 
#rather than trying to win resulting in an interesting game with wins, losses and draws!

import os
import random
from time import *
P={"X":1,"O":2}
Pi=["X","O"]
def disp(G):
	for i in xrange(0,len(G)):
		print G[i],
		if not (i+1)%3:print
def isWin(S):
	if len(S)==1 and "_" not in S:return True,P[list(S)[0]]
	return False,0
def chkWin(G):
	D1,D2={G[0],G[4],G[8]},{G[2],G[4],G[6]}
	if isWin(D1)[0]:return isWin(D1)
	if isWin(D2)[0]:return isWin(D2)
	for i in xrange(0,3):
		H,V={G[i*3],G[i*3+1],G[i*3+2]},{G[i],G[i+3],G[i+6]}
		if isWin(H)[0]:return isWin(H)
		if isWin(V)[0]:return isWin(V)
	return False,0
def rPos(B):
	p=random.sample(range(0,9),1)[0]
	if B[p]!="_":return rPos(B)
	return p
def cvt2Mtrx(B):
	M,MR=[],[]
	for i in xrange(0,3):
		m,mr="",""
		for j in xrange(0,3):m+=B[3*i + j]
		for j in xrange(0,3):mr+=B[3*j + i]
		M.append(m)
		MR.append(mr)
	return M,MR
def genNext(B,S,e2Win,Pl,MX):
	for i in S:
		if i.count(e2Win)==2 and "_" in i:
			B[S.index(i)*MX[0] + i.index("_")*MX[1]]=Pl
			return True
	return False
def play(B,Pl):
	e2Win=Pi[P[Pl]%2]
	H,V=cvt2Mtrx(B)
	D1,D2=[B[0],B[4],B[8]],[B[2],B[4],B[6]]
	if genNext(B,H,e2Win,Pl,(3,1)):return
	elif genNext(B,V,e2Win,Pl,(1,3)):return
	elif D1.count(e2Win)==2 and "_" in D1:B[D1.index("_")*4]=Pl
	elif D2.count(e2Win)==2 and "_" in D2:B[D2.index("_")*2+2]=Pl
	elif "_" in B:B[rPos(B)]=Pl
if __name__=="__main__":
	os.system('clear')
	B,p=["_"]*9,random.randint(0,8)
	B[p],i="X",0
	disp(B)
	while not chkWin(B)[0]:
		sleep(1)
		os.system('clear')
		if i%2:play(B,"X")
		else:play(B,"O")
		disp(B)
		i+=1
		if "_" not in B:break
	if chkWin(B)[0]:print chkWin(B)[1],"WINS!"
	else:print "It's a DRAW!"
