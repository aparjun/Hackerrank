n=input()
d=0
li={"H":10000,"G":5000,"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
for i in range(0,len(n)-1):
	if(li[n[i]]<li[n[i+1]]):
		d=d+li[n[i+1]]-li[n[i]]
	else:
		d+=li[n[i]]
d+=li[n[len(n)-1]]
print(d)
