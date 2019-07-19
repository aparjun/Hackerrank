s=input()
l=0
r=1
m=0
while(r<=len(s)):
    a=s[l:r]
    if(m<r-l):
        m=r-l
    r=r+1
    if(r-1<len(s) and s[r-1] in a):
        l=l+a.index(s[r-1])+1
print(m)            
            
