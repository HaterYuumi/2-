a=[150,147, 145, 144, 140, 138,  132, 129, 128, 127, 120, 112, 109, 101, 100, 109, 110, 113, 117, 124, 127,128, 130, 134, 136, 141, 144, 146, 148, 149, 150, 158, 160, 161, 163, 167, 178, 179, 181, 183, 185, 186, 189, 193, 199, 200]
b=[]
c=[]
while True:
    print(a)
    l=len(a)//2
    r=a[l-1]
    y=a[l]
    for x in range(l):
        b.append(a[x])
    print(b)
    for x in range(l, len(a)):
        c.append(a[x])
    print(c)
    a.clear()
    if r>y:
        a.extend(c)
    else:
        a.extend(b)
    b.clear()
    c.clear()
    input()
