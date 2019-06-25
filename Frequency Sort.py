import operator
from collections import OrderedDict 
li=list(map(int,input().split()))
d=OrderedDict()
for i in li:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
for i in sorted_d:
    for j in range(i[1]):
        print(i[0],end=" ")
