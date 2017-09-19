class sol:
	def __init__(self,J,p):self.J,self.p=J,p
def operate(p,J):
	l,r=p[0],p[1]
	if l==0:l=J[0]
	elif r==J[1]:r=0
	else:
		pr,r=r+l,min(r+l,J[1])
		l=max(0,pr-r)
	return [l,r]
def dfs(L,R,d,J):
	t1,t2,c1,c2=L,R,0,0
	while d not in set(t1.J):
		n=sol(operate(t1.J,J),t1)
		t1,c1=n,c1+1
	while d not in set(t2.J):
		n=sol(operate(t2.J,J[::-1]),t2)
		t2,c2=n,c2+1
	if c1==min(c1,c2):return t1,1
	return t2,-1
if __name__=="__main__":
	print "Enter desired amount "
	d=int(raw_input())
	print "Enter Jug's sizes (Jug 1 and Jug 2)"
	I=raw_input().split(" ")
	J=[int(I[0]),int(I[1])]
	root,Path=sol([0,0],0),[]
	L,R=sol([J[0],0],root),sol([J[::-1][0],0],root)
	T,r=dfs(L,R,d,J)
	while type(T)!=int:
		Path.append(T.J)
		T=T.p
	for i in Path[::-1]:print i[::r]
	print "steps",len(Path)-1
