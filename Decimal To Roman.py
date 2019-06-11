s=int(input())
a=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
b=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
n=""
i=0
while(s>0):
    while(s>=a[i]):
        s-=a[i]
        n+=b[i]
    i+=1
print(n)    
    
    
    
