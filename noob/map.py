from functools import reduce
# def f(x):
#     return x*x

# r=map(f,[1,2,3,4,5,6,7,8,9])
# for n in r:
#     print(n)

# m = list(map(str,[1,2,3,4,5,6,7,8,9]))
# print(m)

# def add(x,y):
#     return 10*x+y
# print(reduce(add,[1,2,3,4,5,6]))

# def char2num(s):
#     digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return digits[s]

# x = reduce(add,map(char2num,'13245'))
# print(x)
# print(isinstance(x,int))

# L = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# def char2num(s):
#     return L[s]
# def str2int(s):
#     return reduce(lambda x,y:x*10+y,map(char2num,s))

# print(str2int('532115'))

# 输入任意字符串list，把每个单词变成首字母大写
# def normalize(name):
#     name = str.title(name)
#     return name


# L1 = ['adam','LISA','barT']
# L2 = list(map(normalize,L1))
# print(L2)

# 利用reduce求列表乘积
# def mult(x,y):
#     return x*y

# def prod(L):
#     print(L)
#     return reduce(mult,L)
# print('3*5*7*9=',prod([3,5,7,9]))


# 把字符串'123.456'转换成float 123.456
def str2float(s):
    L = list(map(chr2float,s))
    S = []
    point = 1
    for n in range(len(L)-1,-1,-1):
        if L[n]=='.':
            point = n
            break
    for n in L[::-1]:
        if n=='.':
            break
        S.append(n)
    return reduce(lambda x,y:x*10+y,L[:point])+(reduce(lambda x,y:x/10+y,S)/10)

def chr2float(s):
    if s == '.':
        return s
    return int(s)

# str2float('123.456')
print('str2float(123.456) =',str2float('123.456'))