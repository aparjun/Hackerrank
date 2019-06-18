#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minTime function below.
def minTime(machines, goal):
    fast=min(machines)
    slow=max(machines)
    minday=math.ceil(goal/len(machines))*fast
    maxday=math.ceil(goal/len(machines))*slow
    while(minday<maxday):
        day = (maxday + minday)//2
        sum=0
        for m in machines:
            sum+=(day//m)
        if(sum>=goal):    
            maxday = day
        else:
            minday = day + 1
    return minday        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
