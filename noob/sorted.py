# x = sorted([36,12,-7,2,-19,33],key=abs,reverse=True)
# print(x)

# 用tuple表示学生名字和成绩，用sorted()对列表按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t): #按名字排序
    return t[0].lower()

def by_score(t): #按成绩排序
    return t[1]

# print(list(map(by_name,L)))
L1 = sorted(L,key=by_name)
print(L1)

L2 = sorted(L,key=by_score)
print(L2)