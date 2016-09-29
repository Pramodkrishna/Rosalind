#!/usr/bin/env python
#alist = ['pramodramakrishna']
#blist = ['krishnapillutla']
#value = zip(alist,blist)
########################################
s1 = 'ATCAGCTAGCA'
s2 = 'ACTAGCATCAG'
#value = []
#print sum([i != k for i, k in zip(s1, s2)])

##IN this we are using the zip function
# i != k means all values of i which are not equal to K
# Zip prints the two lists at the same time side by side

###########################################
cnt = 0
for i in range(len(s1)):
    print s1[i]
    #if s1[i] != s2[i]: cnt+=1
#print cnt

#A better solution
# We set a counter at zero
# then write a if conditon to see which of the vaules
# Are not matching to each other
#

#################################################
