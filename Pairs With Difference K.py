#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    c=0
    arr=sorted(arr)
    l=0
    r=0
    d=0
    while(r<len(arr)):
        d=arr[r]-arr[l]
        if(d==k):
            c+=1
            l+=1
            r+=1
        elif(d<k):
            r+=1
        else:
            l+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
