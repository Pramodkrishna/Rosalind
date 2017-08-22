"""
phone   = {'Zoe':'232-43-58',
            'Alice':'165-88-56'}

#print phone['Zoe']

phone['Bill'] = '33-44-878'
print phone['Bill']
"""

"""
val1 = "ATTGC"
val2 = "ACCGC"
count = 0
#print count
res = sum(i != j for i,j in zip(val1,val2))
print res
"""
"""
lis1 = ["A","B","C","D"]
lis2 = range(1,5)
#print lis2
newdic = dict(zip(lis1,lis2))
#print newdic
"""

"""
line = "Heywassupman,Im,good,how are you?"
#This is a string

lis = ["heymanwassup"]
#This is a list

#print line.split(',',2)
#No one splits a string, very uncommon

#print lis.split('',1)
n = 3
l = zip(line[::3],line[2::4])
print map(''.join,l)
#print line[1::2]
"""

"""
samp = range(10)
print samp
s = []
for sam in samp:
    if sam >= 5:
        s.append(sam)
        print sum(s)
"""

#print ['Hello'] * 3

"""
s_array =  [1,"A","B",4,"C","D",5]

print len(s_array)
"""





"""
using lists in function

def sol(a =[],b =[]):

    d = len(a)- len(b)
    if d%2 == 1:
        print "list are not same "
    else:
        print "Lists are same length"


sol([1,2,3,4],[1,2,3,4,5,6])
"""
