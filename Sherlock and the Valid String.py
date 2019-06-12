#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    d={}
    count=0
    f=0
    for i in s:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1 
    count=d[s[0]]        
    if(len(s)>2 and d[s[0]]!=d[s[1]]):
        count=d[s[2]]
    for i in d:
        if(d[i]!=count):
            if(f!=0):
                return "NO"
            elif(d[i]!=1 and abs(d[i]-count)>1):
                return "NO"
            f=1
    return "YES"        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
