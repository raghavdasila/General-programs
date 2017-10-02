def is_near(P,Q):
	X=[max([P[0],Q[0]]),min([P[0],Q[0]])]
	Y=[max([P[1],Q[1]]),min([P[1],Q[1]])]
	if X[0]-X[1]<=1 and Y[0]-Y[1]<=1:return True
	return False
if __name__=="__main__":
	img=[
	[0,0,1,1,1],
	[0,0,0,1,1],
	[1,1,0,0,0],
	[1,1,1,0,0],
	[1,0,0,0,0]
	]
	objects=[]
	visited=[]
	for i in xrange(0,len(img)):
		v=[]
		for j in xrange(0,len(img[0])):v.append(False)
		visited.append(v[:])
	for i in xrange(0,len(img)):
		marked=False
		for j in xrange(0,len(img[0])):
			if img[i][j]==1:
				objects.append([[i,j]])
				visited[i][j]=True
				marked=True
				break
		if marked:break
	for i in xrange(0,len(img)):
		for j in xrange(0,len(img[0])):
			if img[i][j]==1:
				marked=False
				for obj in objects:
					for item in obj:
						if is_near(item,[i,j]) and not visited[i][j]:
							obj.append([i,j])
							visited[i][j]=True
							marked=True
							break
					if marked:break
				if not marked and not visited[i][j]:objects.append([[i,j]])
	for i in xrange(0, len(objects)):
		print "Enter Colour for object ",i+1
		color=raw_input()
		for item in objects[i]:
			img[item[0]][item[1]]=color
	for i in img:
		for j in i:
			print j,
		print							
