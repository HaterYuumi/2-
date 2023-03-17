from math import factorial
sp=[1,2,3,4,6,8,10]
k=0
for x in sp:
    if x%2==0:
        k+=1
print(k*(len(sp)-1)-(factorial(k)/factorial(k-2)/factorial(2)))