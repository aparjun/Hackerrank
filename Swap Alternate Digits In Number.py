n=input()
pow=1
l=0
if(len(n)%2!=0):
	n=int(n)
	l=n%10
	n=n-l
	n=n//10
while(n>=pow):
	r=(n//pow)%100
	n=n-(r)*pow+(((r%10)*10)+r//10)*pow
	pow*=100
n=n*10+l	
print(n)	
