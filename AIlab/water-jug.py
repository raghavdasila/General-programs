A=["Empty Jar ","Fill Jar "," is poured to "]
def op(i,v):return " J"+i+" has "+str(v)
def solve(J,d,il,ir):
	c=l=r=0
	s=[]
	while l!=d and r!=d:
		a=""
		if l==0:l,a=J[0],A[1]+il
		elif r==J[1]:r,a=0,A[0]+ir
		else:
			pr,r=r+l,min(r+l,J[1])
			l,a=max(pr-r,0),il+A[2]+ir
		a+="\t"+op(il,l)+op(ir,r)
		s.append(a)
		c+=1
	return c,s
if __name__=="__main__":
	print "Enter desired amount "
	d,c,s=int(raw_input()),0,""
	print "Enter Jug's sizes (Jug 1 and Jug 2)"
	I=raw_input().split(" ")
	J=[int(I[0]),int(I[1])]
	c1,s1=solve(J,d,"1","2")
	c2,s2=solve(J[::-1],d,"2","1")
	if c1==min(c1,c2):c,s=c1,s1
	else:c,s=c2,s2
	for i in s:print i
	print "total steps",c
