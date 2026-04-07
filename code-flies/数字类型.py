print(0.1 + 0.2) 
print(0.3 == 0.1 + 0.2)
i = 0
while i < 1:
  i = i + 0.1
  print(i)

import decimal #引入decimal模块
a,b =decimal.Decimal('0.1'),decimal.Decimal('0.2') #使用Decimal类创建Decimal对象
print('换行','\n') #换行
print(a+b) #Decimal对象相加
c = decimal.Decimal('0.3')
print(a+b == c,"\n")
# 数字+E+位数是科学计数法
# 123e4表示123*10的4次方
# 123e-4表示123*10的-4次方
complex_num = 1 + 2j #复数，实部为1，虚部为2
print(complex_num)
print(complex_num.real,'换行\n',complex_num.imag) #获取复数的实部和虚部\

print(-3/2,'换行\n',-3//2) #除法和地板除，除法结果为-1.5，地板除结果为-2，地板除是向下取整的除法
# 其实就是以前学过的[x]方式，往下去整数不超过x本身的最大整数，负数则是往下去整数不超过x本身的最小整数
print(3%2,6%2,7%2,'换行\n') #取余数，余数是除法后剩下的数\

print(divmod(-3,2),'\n') # divmod(a,b)函数返回a除以b的商和余数，结果为一个元组，商为-2，余数为1
#先点出，再用%取余数
print(abs(complex_num),'换行\n') #复数的绝对值，复数的绝对值是实部和虚部的平方和的平方根，结果为2.23606797749979
print(int(-99.321314),'换行\n') # int是直接去掉小数点后面的所有
#float(x)是将整数转换为浮点数
# complex(re,im)是内容转换为复数，re为实部，im为虚部
print(float('1000323'),float(+2e4),'换行\n') #float()中加单引号是将字符串的数字转换为浮点数，float()中加+号是将数字转换为浮点数，不加单引号就是直接将整数或者其他数字类型转换为浮点数
print(complex(-1 - 45j),'换行\n','不加空格的字符串形式也就是双引号里面加\n',complex("23-312j")) #complex()中加单引号是将字符串的数字转换为复数，complex()中加+号是将数字转换为复数，不加单引号就是直接将整数或者其他数字类型转换为复数
print(pow(4,2),'换行\n',2 ** 3,'换行\n',pow(4,2,3),'换行测试\n',4 ** 2 % 3) #pow(x,y)函数返回x的y次幂，pow(x,y,z)会将幂运算的结果对z进行求余的运算

a = eval(input('请输入一个数字：')) #eval()函数将输入的字符串当成有效的表达式来求值，并返回结果
b = eval(input('请输入另一个数字：')) #input()函数用于获取用户输入的字符串，eval()函数将输入的字符串当成有效的表达式来求值，并返回结果
c = eval(input('请输入一个数字：')) #input()函数用于获取用户输入的字符串，eval()函数将输入的字符串当成有效的表达式来求值，并返回结果
d = a+b+c
e = (a+b+c)/3
print(f'你输入的三个数字的和是：{d},平均数是：{e:.2f}',sep='') #f-string格式化字符串，使用花括号{}来引用变量，输出结果为你输入的三个数字的和是：d，平均数是：e

todaydate = input('输入今天的日期，格式为xxxx.xx.xx：')
print(f'今天是{todaydate},我第一次独立写程序啦！',sep=',') #f-string格式化字符串，使用花括号{}来引用变量，输出结果为今天是todaydate，我第一次独立写程序啦！


userbay = input('').split('和') #input()函数用于获取用户输入的字符串，split()方法将输入的字符串按照空格分割成一个列表
float_userbay_1 = float(userbay[0]) #直接用上面split('')进行捕获。split的括号里面跟的就是你要并列的字符，例如我这里是“和”字，那么输入一个数就跟一个“和”字，但不需要空格。如果你输入的数据超过下面变量的内容，那么多出的内容就会没有捕获。它split就相当于把你输入的数据整理成了一个定义在你input前面的变量里面。而且split只能接input用户输入的形式
float_userbay_2 = float(userbay[1]) #将列表中的字符串转换为浮点数
float_userbay_3 = float(userbay[2]) 
all_userbay = float_userbay_1 + float_userbay_2 + float_userbay_3

print(f'应付{all_userbay:.1f}元') #f-string格式化字符串，使用花括号{}来引用变量，输出结果为应付all_userbay元，保留两位小数


x_str = input('请输入一个数字：').split(',')#input()函数用于获取用户输入的字符串
import decimal #引入decimal模块
x_int_1 = decimal.Decimal(x_str[0])
x_int_2 = decimal.Decimal(x_str[1])
print(f'{x_int_1}*{x_int_2}={x_int_1*x_int_2}') #f-string格式化字符串，使用花括号{}来引用变量，输出结果为x_int_1*x_int_2=x_int_1*x_int_2 '''

song_words = "爱我中华,五十六个星座五十六枝花,五十六族兄弟姐妹是一家,五十六种语言汇成一句话,爱我中华爱我中华爱我中华,爱我中华,健儿奋起的步伐,爱我中华,建设我们的国家,爱我中华,中华雄姿英发,爱我中华,五十六族兄弟姐妹,五十六种语言汇成一句话,爱我中华。"
song_tages = input('请输入要查找的字符串：') 
song_tages_count = song_words.count(song_tages) #变量.count(变量)的形式来查找内容，并计算次数
print(f'{song_tages}出现{song_tages_count}次')

user_input_words = input('').lower() #input()函数用于获取用户输入的字符串，lower()方法将输入的字符串转换为小写字母
user_input_words_long = len(user_input_words) #len()函数返回字符串的长度
user_input_words_lower = user_input_words.lower() #lower()方法将字符串转换为小写字母
print(f'{user_input_words_lower[0:5]}') #输出字符串的前6个字符


