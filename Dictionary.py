#!/usr/bin/python

"""
How to create dictionary and access the key and values in them

phone   = {'Zoe':'232-43-58',
            'Alice':'165-88-56'}

#print phone['Zoe']

phone['Bill'] = '33-44-878'
print phone['Bill']
"""

from collections import Counter

"""
values = ['apple','apple','egg','bread',]
counts =  Counter(values)
print values.most_common(n=None)
"""


"""
Find the unique count of words in a list and return them
Given:   A  string     of  length  at  most  10000  letters.
Return:   How  many  times  any  word  occurred  in  string.  Each  letter  case  (upper  or  lower)  in  word
matters.  Lines  in  output  can  be  in  any  order
"""


#values = "We  tried  list  and  we  tried  dicts  also  we  tried  Zen"
#vals = values.split(' ')
#vals_count = Counter(vals)
#print vals_count
#print vals_count.most_common(n =None)









def solution(A, X):
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l < r:
        m = (l + r) // 2
        if A[m] > X:
            r = m - 1
        else:
            l = m
        if A[l] == X:
            return l
    return -1

print solution([1,2,3], 4)
