n=input()
s=0
def isprime(m):
    for i in range(2,m//2):
        if(m%i==0):
            return False
    return True    
    
for i in range(0,len(n)):
    for j in range(i,len(n)):
        s+=int(n[j])
if(isprime(s)):
    st="00"
    while(len(st)>1):
        st=str(s)
        s=0
        for i in st:
            s+=int(i)    
    print(st)
else:
    print(s)
            
        
