#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    d1={}
    d2={}
    c=0
    for i in s1:
        if(i in d1):
            d1[i]+=1
        else:
            d1[i]=1
    for i in s2:
        if(i in d2):
            d2[i]+=1
        else:
            d2[i]=1
    for i in d1:
        if(i in d2):
            if(d1[i]<d2[i]):
                c+=d1[i]
            else:
                c+=d2[i]
    return (len(s1)-c+len(s2)-c)                   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
