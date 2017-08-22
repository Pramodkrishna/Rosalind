#!/usr/bin/python
val1 = "ATTGC"
val2 = "ACCGC"
count = 0
#print count
res = sum(i != j for i,j in zip(val1,val2))
print res
