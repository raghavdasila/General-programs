import string
if __name__=="__main__":
#	pred=raw_input()
	print "Enter Predicate logic, with each part seperated by space"
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
	print "Inputs\tResult"
	print inputs
	for i in xrange(0,n):
		 ins=list(bin(i)[2:])
		 while len(ins)<len(inputs):
		 	ins=['0']+ins
		 print ins,":",
		 e_pred=""
		 for t in tokens:
		 	if t in inputs:
		 		t=ins[inputs.index(t)]
		 	e_pred+=t+" "
		 print int(eval(e_pred))
