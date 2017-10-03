import string
import random
if __name__=="__main__":
	print "Enter Predicate logic, with each part seperated by space"
#	pred=raw_input()	
	pred="(( A and not B ) implies C ) and (( not A ) iff ( B and C ))"
	tokens=pred.split(' ')
	entities=list(string.ascii_lowercase) + list(string.ascii_uppercase)
	inputs=[]
	for t in xrange(len(tokens)):
		if tokens[t]=='implies':tokens[t]=">="
		if tokens[t]=='iff':tokens[t]="=="
		if tokens[t] in entities and tokens[t] not in inputs:
			inputs.append(tokens[t])
	n=2**(len(inputs))
	res=[]
	for i in xrange(0,n):
		 ins=list(bin(i)[2:])
		 while len(ins)<len(inputs):ins=['0']+ins
		 print ins,":",
		 e_pred=""
		 for t in tokens:
		 	if t in inputs:t=ins[inputs.index(t)]
		 	e_pred+=t+" "
		  res.append(eval(e_pred))
	print "Quiz Time! For given inputs, enter the output" 
	print "Enter number of questions you would like, less than",n
	q=int(raw_input())-1
	qi=random.shuffle(range(0,n))
	while q>=0:
		q-=1
		ques=qi[q]
		ins=list(bin(ques)[2:])
		while len(ins)<len(inputs):ins=['0']+ins
		print "Q: If,"
		for i in inputs:print i,":",bool(ins[inputs.index(i)])
		print "Enter Conclusion as True or False"
		ans=raw_input()
		if ans==res[ques]:print "Correct!"
		else:print "Incorrect!"
	print "Game Over!"
