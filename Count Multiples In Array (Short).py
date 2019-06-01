n=int(input())
a=list(map(int,input().split()))
MAX=max(a)
s=[]
count=[0]*(MAX+1)
s=[0]*(n+1)
for i in range(n):
    count[a[i]]+=1
for i in range(1,n+1):
    for j in range(i,MAX+1,i):
        s[i]+=count[j]
b=sum(s)
print(b)
