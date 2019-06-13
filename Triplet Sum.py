#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a=list(sorted(set(a))) 
    b=list(sorted(set(b))) 
    c=list(sorted(set(c)))
    # To Remove Duplicates
    count=0
    j=0
    k=0
    for i in b:
        while(j<len(a) and a[j]<=i):
            j+=1
        while(k<len(c) and c[k]<=i):
            k+=1
        count+=(j*k)    
    return count        
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
