
ans = []
def countSieve(arr, n): 
	
	MAX=max(arr) 
	global ans 

	ans = [0]*(MAX + 1) 
	cnt = [0]*(MAX + 1) 
	for i in range(n): 
		cnt[arr[i]] += 1
	for i in range(1, MAX+1): 
		for j in range(i, MAX+1, i): 
			ans[i] += cnt[j] 

def countMultiples(k): 
	return(ans[k]) 

if __name__ == "__main__":
	
	m=int(input())
	arr = list(map(int,input().split()))
	n=len(arr) 
	countSieve(arr, n)
	c=0
	for i in range(1,m+1):
		c+=countMultiples(i)
	print(c)	
