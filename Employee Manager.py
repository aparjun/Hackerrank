emp=list(map(int,input().split()))
man=list(map(int,input().split()))
for i in emp:
	if i not in man:
		print(i,"-> not a manager")
	else:
		print(i,"-> ",end="")
		for j in range(len(man)):
			if(i==man[j] and emp[j]!=man[j]):
				print(emp[j],end=" ")
		print()		
		
