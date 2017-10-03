import os
import time
def is_near(P,Q):
	X=[max([P[0],Q[0]]),min([P[0],Q[0]])]
	Y=[max([P[1],Q[1]]),min([P[1],Q[1]])]
	if X[0]-X[1]<=1 and Y[0]-Y[1]<=1:return True
	return False
def find_in_obj(item,objects):
	for i in objects:
		if item in i:return objects.index(i)+1
def show_identified(visited,img,objects):
	os.system("clear")
	print "Orignal Image:"
	for i in img:
		for j in i:print j,
		print 
	print "Searching For Objects to Fill"
	for i in xrange(0,len(img)):
		for j in xrange(0,len(img[0])):
			if visited[i][j]:
				if img[i][j]:print find_in_obj([i,j],objects),
				else:print "_",
			else:print "?",
		print		
	time.sleep(1)
if __name__=="__main__":
	img=[
	[0,0,1,1,1,0],
	[0,0,0,1,1,0],
	[1,1,0,0,0,0],
	[1,1,1,0,1,1],
	[1,0,0,0,1,1]
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
							marked=True
							break
					if marked:break
				if not marked and not visited[i][j]:objects.append([[i,j]])
			visited[i][j]=True
			show_identified(visited,img,objects)
	colors=[]
	print "Enter Colour codes,single digit"
	for i in xrange(0,len(objects)):
		colors.append(raw_input())
	print "Colouring-"
	for i in xrange(0, len(objects)):
		color=colors[i]
		for item in objects[i]:
			img[item[0]][item[1]]=color
	print
	for i in img:
		for j in i:
			if j!=0:print j,
			else:print "_",
		print							
