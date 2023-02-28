with open('26.txt') as f:
    k=1
    s=[int(x) for x in f]
    s.sort(reverse=True)
    mini=s[0]
    s.pop(0)
    for i in range(0,  len(s)-1):
        if s[i]+3<=mini:
            k+=1
            mini=s[i]
print(k, mini)
