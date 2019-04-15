from collections import Iterable  #可被迭代的对象称为Iterable（迭代对象）
from collections import Iterator  #可被next()调用并可迭代的为Iterator（迭代器）
# a = isinstance (range(1,2),Iterable)
# print(a)

it = iter([1,2,3,4,5])
print(isinstance(it,Iterator))
print(list(it))
# 循环:
# while True:
#     try:
#         # 获得下一个值：
#         x = next(it)
#         print(x)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         print("StopIteration!")
#         break