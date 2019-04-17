
# 输出1000以内的素数
# def _not_divisible(n):
#     return lambda x: x % n > 0

# def _odd_iter():
#     n = 1
#     while True:
#         n = n+2
#         yield n

# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n=next(it)
#         yield n
#         it = filter(_not_divisible(n),it)

# for n in primes():
#     if n<1000:
#         print(n)
#     else:
#         break


#筛选范围内所有回数，12321，909（从左往右和从右往左一样）
def is_palindrome(n):
        s = 0
        k = n
        while True:
                if n>=1:
                        s=(s+n%10)*10
                        n=(n-n%10)/10
                else:
                        s=s/10
                        break
        return s==k


# print(fn(121))
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')