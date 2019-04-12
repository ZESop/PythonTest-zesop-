def MinMax(s):
    if len(s)==0:
        return (None,None)
    max = min = s[0]
    for n in s:
        if n > max:
            max = n
        if n < min:
            min = n
    return min,max

s=[]
print(MinMax(s))
print((None,None))

