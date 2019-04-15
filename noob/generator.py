# 斐波那契数列

# def fib(max):
#     n,a,b = 0,0,1
#     while n<max:
#         yield b
#         a,b = b,a+b
#         n = n+1
#     return 'done'

# g = fib(10)
# while True:
#     try:
#         x=next(g)
#         print('g:',x)
#     except StopIteration as e:
#         print ('Generator return value:',e.value)
#         break



##### 以generator输出杨辉三角

#定义一个函数，生成下一行list(每个list都以1开头，以1结尾)
def list(a):
    b = [1]  
    for n in range(0, len(a)-1):  #让上一个list两两相加，插入新的list
        b.append(a[n]+a[n+1])
    b.append(1)
    return b

#不断把list写入generator
def triangles(n):
    if n < 1:
        yield []
    if n >= 1:
        yield [1]
    if n >= 2:
        yield [1,1]
    if n > 2:
        a = [1,1]
        while n>2 :
            a = list(a)
            yield a
            n = n-1

#遍历generator(传入输出行数)
for n in triangles(10):
    print(n)
