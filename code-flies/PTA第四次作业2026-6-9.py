'''
str = input()
str_1 = str[1:-1]
str_2 = str_1.split(',')
y = []
for i in str_2:
    y.append(int(i))
x = []
for s in y :
    if s % 2 == 0:
        x.append(s)
    else:
        x.append(s*s)
print(f'{x}')
'''
'''
第二题
coffee=('意式','美式','拿铁','摩卡')
ch=('冰','冷','热','烫')
a = input().split() #以空格分隔，分别是，第一个是coffee的值，第二个是ch的值，第三个是数量
str_1 =int(a[0]) #coffee的值
str_2 =int(a[1]) #ch的值
b = coffee[str_1] #获取coffee的值
c = ch[str_2] #获取ch的值
print(f'{a[2]}杯{c}{b}') #读取顺序是 数量，温度，咖啡
'''

'''
第三题
a = "abcxadabxsabcib"
b = "ab"
print(a.count(b, 0,len(a)))'''


'''
第四题

# 读取输入的数字（转成整数）
n = int(input())
# 用多分支条件判断，每个数字对应一个星期
if n == 1:
    print("星期一")
elif n == 2:
    print("星期二")
elif n == 3:
    print("星期三")
elif n == 4:
    print("星期四")
elif n == 5:
    print("星期五")
elif n == 6:
    print("星期六")
elif n == 7:
    print("星期日")
'''

'''
第五题
# 1. 读取输入的字符串（带[]和逗号）
input_str = input()
# 2. 去掉首尾的方括号，只保留中间的数字部分
input_str = input_str[1:-1]  
# 3. 按逗号分割成单个字符串，再去掉每个字符串前后的空格，转成整数列表
str_parts = input_str.split(',')
nums = []
for p in str_parts:
    num = int(p.strip())  # strip()去掉逗号后的空格，比如" 3" → "3"
    nums.append(num)
# 4. 去重：遍历列表，把没出现过的学号加入新列表
unique_nums = []
for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)
# 5. 按学号递增排序（升序）
unique_nums.sort()
# 6. 输出结果（Python列表直接打印就是题目要求的格式）
print(unique_nums)
'''

'''
第六题
# 1. 读取输入的投票字符串，处理成整数集合（自动去重）
voted_str = input().strip()
# 分割字符串 → 转成整数列表 → 转成集合（自动去重）
voted_set = set(map(int, voted_str.split(',')))
# 2. 定义第二小队的所有队员序号（6-10）
second_team = {6, 7, 8, 9, 10}
# 3. 求差集：第二小队 - 已得票队员 = 未得票队员
no_vote_members = second_team - voted_set
# 4. 按升序排序，再用空格拼接输出
print(' '.join(map(str, sorted(no_vote_members))))
'''

'''
第七题
a = 0
b = 0
c = 0
d = 0
e = 0
x = input().split()
y = []
for s in x :
    y.append(int(s))
for i in y :
    if i >= 90:
        a = a+1
    elif 80 <= i < 90:
        b = b+1
    elif 70 <= i < 80:
        c = c+1
    elif 60 <= i < 70:
        d = d+1
    else:
        e = e+1
print(f'A:{a}')
print(f'B:{b}')
print(f'C:{c}')
print(f'D:{d}')
print(f'E:{e}')
'''