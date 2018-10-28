#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The runtime of our algorithm depends on our choice of pivot. 
In the best-case, if we pick a pivot that ends up at position k, the runtime is O(n). 
In the worst case, we pick always pick pivot that is the minimum or maximum value in the array. 
The runtime is T(n) = T(n-1) + O(n).

@author: Kefei Wu
"""

import random
import time
import matplotlib.pyplot as plt

total = []

def partition(L, l, r):
    """
    input: L is the list that we want to find kth smalles element in it
           l is the left most index
           r is the right most index
    partition method is repeated partitioning the list
    """
    x = L[r]
    i = l-1
    for j in range(l, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
    return i+1

def randomPartition(L, l, r):
    """
    input: L is the list that we want to find kth smalles element in it
           l is the left most index
           r is the right most index
    randomPartition method is repeated partitioning the list around randomly chosen pivot.
    """
    if l == r:
        return l
    i = random.randint(l, r) # randomly chose pivot
    L[i], L[r] = L[r], L[i]
    return partition(L, l, r)


def randomSelect(L, l, r, i):
    """
    input: L is the list that we want to find kth smallest element in it
           l is the left most index
           r is the right most index
           i is the index of value that we want to find
    randomSelect method finds the kth elemenet by repeated partitioning the list.
    """
    if l == r:
        return L[l]
    q = randomPartition(L, l, r)
    k = q - l + 1
    if i == k:
        return L[q]
    elif i < k:
        return randomSelect(L, l, q-1, i)
    else:
        return randomSelect(L, q+1, r, i-k)


def kthMin(L, k):
    """
    input: k is the index of value
           n is the length of the list
    This method let us to finds the kth minimum of a list by calling method randomSelect
    """
    if L is None or k < 0 or k > len(L):
        return None
    value = randomSelect(L, 0, len(L)-1, k)
#    print(L)
    print ("{}th smallest value is: {}".format(k, value))

kthMin([1,6,3,8,0,-3],3)
# test if this is linear on graph    
size = [10, 100, 1000, 10000, 50000, 100000, 300000, 400000, 500000, 600000, 800000, 1000000]
for i in size:
    #print(i)
    L = [random.random() for j in range(i)]
    #print(L)
    k = 5
    start = time.time()
    kthMin(L, i)
    end = time.time()
    cost = end-start
    total.append(cost)

plt.scatter(total, size)
