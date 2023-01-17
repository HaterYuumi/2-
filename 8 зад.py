#8
from itertools import product
nums=product('0123456',repeat=4)
k=0
n='24 44 64 84 42 46 48'
nn=n.split()
for n in nums:
    numb=''.join(n)
    sp=[]
    if numb.count('4')==1 and numb[0]!='0':
        for x in nn:
            if x in numb:
                sp.append(x)
        if not sp: 
            k+=1
print(k)
