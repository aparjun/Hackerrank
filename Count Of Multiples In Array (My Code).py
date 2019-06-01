def solve (Ar):
    c=0
    for i in Ar:
        m=i//2
        if(n<m):
            m=n
        for j in range(2,m+1):
            if(i%j==0):
                c+=1
        if(i<=n):
            c+=1
    c+=len(Ar)
    return c            
    
n = int(input())
Ar = list(map(int,input().split()))
out_ = solve(Ar)
print (out_)
