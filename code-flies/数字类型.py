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