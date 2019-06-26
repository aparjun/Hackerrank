emp=list(map(int,input().split()))
man=list(map(int,input().split()))
li=[]
def rec(employee):
	for i in employee:
		li.clear()
		if i not in man:
			print(i,"-> not a manager")
		else:
			print(i,"-> ",end="")
			for j in range(len(man)):
				if(i==man[j] and employee[j]!=man[j]):
					print(employee[j],end=" ")
					li.append(employee[j])
		if li:
			rec(li)
		print()	
		
		
rec(emp)
