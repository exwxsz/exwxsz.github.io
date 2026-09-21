'''for i in range(1, 10):
    for j in range(1, i + 1):
        c = i * j
        if c >= 10:
          print(f"{j}X{i}={i*j}", end=" ") 错在哪儿？
        else:
          print(f"{j}X{i}= {i*j}", end=" ")
    print("") 错误版本'''

'''for i in range(1, 10):
    for j in range(1, i + 1):
        c = i * j
        if c >= 10:
          print(f"{i}X{j}={i*j}", end=" ") # 错在{i}X{f}={i*f}
        else:
          print(f"{i}X{j}= {i*j}", end=" ") # 而不是{j}X{i}= {i*j}
    print("")
'''

'''s = []
a = []
j = input("")
for i in j :
  if i.isdigit():
    s.append(i) #判断是否为数字，是就添加到s列表，否就全部添加a列表
  else:
    a.append(i) 
print("车牌{0}中的最后一个数字为{1}".format(j,s[-1]),end="")'''



#关于素数：除1以外；除了它本身和1能够整除它，其他数不能除以它；偶数基本都不是(除了2)
#例如421只能被421或1整除
s = 0 #初始化
for i in range(2,1001): # 直接从2开始
    is_sushu = True #需要从遍历开始就默认认为是素数，下一个For遍历才判断是不是，
    # s = 0 不能for里面初始化，因为每次for循环都会重新初始化
    for j in range(2,i): 
        if i % j == 0 :
            is_sushu = False
            break #跳出判断i此时的i % j的判断，直接遍历下一个数i进行判断素数
    if is_sushu == True:
        print(f"{i:<5}", end="")
        s += 1 # 没for一次i打印一次就加1
        if s == 10: #每10个换行
          print()
          s = 0   #重置s = 0，每10个换行