L1 = ['Hello','World',18,'Apple',None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]  #可以使用if筛选，true则通过
print(L2)