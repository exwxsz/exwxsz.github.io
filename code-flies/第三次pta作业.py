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

s = 0  # 素数计数器（只数素数）
# 素数从2开始，排除1
for i in range(2, 1001):
    # 标记：先假设i是素数
    is_prime = True
    # 检查2~i-1能不能整除i
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break  # 找到因数，不用再查了
    
    # 只有是素数才打印+计数
    if is_prime:
        print(f"{i:<5}", end="")  # 左对齐占5列，新手也可以写f"{i:5d}" >右对齐，<前面就是填充字符，不写默认是空格
        s += 1
        # 每10个素数换行
        if s == 10:
            print()
            s = 0  # 重置计数器