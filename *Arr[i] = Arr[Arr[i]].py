n=int(input())
li=list(map(int,input().split()))
for i in range(n):
	li[i]=(li[li[i]]%n)*n+li[i]
for i in range(n):
	li[i]=li[i]//n
print(li)	
	
