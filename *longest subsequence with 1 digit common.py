n=int(input())
li=list(input().split())
a=[0]*100001
ind=0
for i in li:
	s=set(i)
	for j in s:
		ind=int(j)
		a[ind]=a[ind]+1
print(max(a))		
