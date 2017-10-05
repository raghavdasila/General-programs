if __name__=="__main__":
	print "Medicine Accuracy Testing (Enter percentages)"
	print "Enter sensitivity"
	se=float(raw_input())/100.0
	print "Enter Specificity"
	sp=float(raw_input())/100.0
	print "Enter percentage of users"
	up=float(raw_input())/100.0
	print "Enter population"
	p=float(raw_input())
	pv=(se*up)/(se*up+(1.0-up)*(1.0-se))
	nv=(sp*up)/(sp*up+(1.0-up)*(1.0-sp))
	n_users=up*p
	users=p-n_users
	cf1=int(pv*p)
	cf2=int(nv*p)
	print "Positive's certainty factor, people:",pv,cf1
	print "Negative's certainty factor, people:",nv,cf2
	print "Medicine suitable for people?"
	if pv<.7 or nv<.7:print "NO"
	else:print "YES"
	
