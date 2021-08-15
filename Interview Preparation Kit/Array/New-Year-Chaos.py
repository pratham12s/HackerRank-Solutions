#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    n = len(q)
    i=n-1
    bribe=0
    while i>=0:
        corr_pos = i+1
        if corr_pos!=q[i]:
            if i>=1 and corr_pos==q[i-1]:
                bribe+=1
                q[i],q[i-1]=q[i-1],q[i]
            elif i>=2 and corr_pos==q[i-2]:
                bribe+=2
                q[i-1],q[i-2]=q[i-2],q[i-1]
                q[i],q[i-1]=q[i-1],q[i]
            else:
                print("Too chaotic")
                return
        i-=1
    print(bribe)
    return

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
