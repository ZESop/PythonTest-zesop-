from math import sqrt
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum

# f = lazy_sum(1,3,5,7,9)
# f1 = lazy_sum(4,8,1,4)
# print(f()+f1())

# 1、2、3的平方和
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1,4): #每次执行仅调用1次循环
#         fs.append(f(i))
#         print(i)
#     return fs

# f1,f2,f3 = count()
# print(f1(),f2(),f3())

# 利用闭包返回一个计数器函数，每次调用它返回递增整数
# def createCounter():
#     x =[0]
#     def counter():
#         x[0] += 1
#         return x[0]   
#     return counter
# f1 = createCounter()
# print(f1(),f1(),f1())

#用闭包实现一个点与点之间的距离计算
# def point(x,y):
#     def get_distance(u,v):
#         return sqrt((x-u)**2 + (y-v)**2)
#     return get_distance

# pt = point(7,2)
# print(pt(10,6),pt(4,5))

# 匿名函数筛选奇数
L = list(filter(lambda n:n%2==1,range(1,20)))
print(L)

