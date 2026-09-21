'''
import time

# 计时装饰器 """这是一个计时装饰器的实现装饰器可以用来在不修改原函数的情况下，给函数添加额外的功能这里实现的装饰器可以计算被装饰函数的执行时间"""
def count_time(func):
    def wrapper(*args, **kwargs):
        start = time.time() #  记录开始时间
        result = func(*args, **kwargs) #  执行原函数并获取结果
        end = time.time() #  记录结束时间
        print(f"函数 {func.__name__} 运行耗时：{end - start:.4f}秒") #  打印函数执行耗时，保留4位小数
        return result #  返回原函数的执行结果
    return wrapper

# 给求和函数加上计时功能 """使用@语法将装饰器应用到求和函数上这样调用calc_sum函数时，实际上会先执行wrapper函数"""
@count_time
def calc_sum(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

# 调用 calc_sum函数，计算0到1000000的和，并打印结果
print(calc_sum(1000000))

'''

'''math	数学运算（如平方根、三角函数等）
os	操作系统相关功能（如文件、目录操作）
sys	系统相关的参数和函数
random	生成随机数
datetime	处理日期和时间
json	处理 JSON 数据
re	正则表达式操作
collections	提供额外的数据结构（如 defaultdict、deque）
itertools	提供迭代器工具
functools	高阶函数工具（如 reduce、lru_cache）'''

'''
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
mode 参数有：

模式	描述
t	文本模式 (默认)。
x	写模式，新建一个文件，如果该文件已存在则会报错。
b	二进制模式。
+	打开一个文件进行更新(可读可写)。
U	通用换行模式（Python 3 不支持）。
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

默认为文本模式，如果要以二进制模式打开，加上 b 。

file 对象
file 对象使用 open 函数来创建，下表列出了 file 对象常用的函数：

序号	方法及描述
1	
file.close()

关闭文件。关闭后文件不能再进行读写操作。

2	
file.flush()

刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。

3	
file.fileno()

返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。

4	
file.isatty()

如果文件连接到一个终端设备返回 True，否则返回 False。

5	
file.next()

Python 3 中的 File 对象不支持 next() 方法。

返回文件下一行。

6	
file.read([size])

从文件读取指定的字节数，如果未给定或为负则读取所有。

7	
file.readline([size])

读取整行，包括 "\n" 字符。

8	
file.readlines([sizeint])

读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。

9	
file.seek(offset[, whence])

移动文件读取指针到指定位置

10	
file.tell()

返回文件当前位置。

11	
file.truncate([size])

从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。

12	
file.write(str)

将字符串写入文件，返回的是写入的字符长度。

13	
file.writelines(sequence)

向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
'''

#判断字符串是否为数字

'''def is_number(s):
  try: #一种新的判断方法;跟if类似
    float(s)  # 尝试将字符串转换为浮点数
    return True  # 如果成功，返回True
  except ValueError: # 如果转换失败，抛出ValueError异常
    pass

  try:
    # from unicodedata import numeric  # 导入unicodedata模块中的numeric函数
    # numeric(s)  # 尝试将字符串转换为数字
    import unicodedata  # 导入unicodedata模块
    unicodedata.numeric(s)  # 尝试将字符串转换为数字
    return True # 如果成功，返回True
  except (TypeError, ValueError):
    pass

    return False # 如果两种方法都失败，返回False

input_str = input("请输入一个字符串：") # 获取用户输入的字符串
print(is_number(input_str)) # 调用is_number函数判断输入的字符串是否为数字，并打印结果
'''

'''
def great():
  print("来自example的问候")
  print("测试")
if __name__=="__main__":
  print("该great()函数正在直接运行")
  great()
else:
  print("该great()函数正在被导入")
  great()
'''


#面向编程
#面向类

'''class NameOfClass:
  #构造函数
  def __init__(self,cat_name,cat_size,cat_color):   #第一个字符永远是self必须不变
    self.name = cat_name  #self.name是实例属性，如果没有self就单纯是变量了
    self.size = cat_size
    self.color = cat_color
  def speak(self,contents,times):
    self.contents = contents
    self.times = times
    print(f'{self.name}说{self.contents}，重复了{self.times}次')
  #实例方法
cat1 = NameOfClass("汐汐","大","白色")  #创建一个实例对象cat1
cat2 = NameOfClass("小美","小","粉色")  #创建一个实例对象cat2
cat3 = NameOfClass("心夏","小","灰色")  #创建一个实例对象cat3 
cat1.speak("喵",3)  #调用实例方法
print(f'第一个猫的名字是{cat1.name}，它的体型是{cat1.size}，它的颜色是{cat1.color}')
print(f'第二个猫的名字是{cat2.name}，它的体型是{cat2.size}，它的颜色是{cat2.color}')
print(f'第三个猫的名字是{cat3.name}，它的体型是{cat3.size}，它的颜色是{cat3.color}')
print(f'{cat1.name}刚刚说的是{cat1.contents}且重复了{cat1.times}次')
'''


'''

#案例，
# 汽车，宝马，奔驰，大众，特斯拉
# 2024款，2025款，2026款
# 喷漆:普通喷漆，金属喷漆，哑光喷漆
# 车身颜色：白色，黑色，红色，蓝色，绿色，黄色，紫色，粉色，灰色
# 轮胎：普通轮胎，运动轮胎，越野轮胎
# 车灯：普通车灯，LED车灯，氙气车灯
# 车身尺寸：小型车，中型车，大型车
# 是否为痛车
# 是否为新能源车

class Car:
  def __init__(self,name,model,color,paint_type,tire_type,light_type,size,is_pain,is_new_energy):
    self.name = name
    self.model = model #日期
    self.color = color #样式
    self.paint_type = paint_type #喷漆
    self.tire_type = tire_type#轮胎
    self.light_type = light_type#车灯
    self.size = size#车型
    self.is_pain = is_pain#是否为痛车
    self.is_new_energy = is_new_energy#是否为新能源
  def speed(self,max_speed,重量):
    self.max_speed = max_speed
    self.重量 = 重量
car_1 = Car("宝马","2024款","白色","普通喷漆","普通轮胎","普通车灯","中型车","爱莉希雅痛车","新能源车")
car_2 = Car("奔驰","2025款","黑色","金属喷漆","运动轮胎","LED车灯","大型车","纱凪痛车","是新能源车")
car_1.speed(200,1.7)
car_2.speed(250,1.8)
print(f'{car_1.model}的{car_1.name}是{car_1.color}，是{car_1.paint_type}，是{car_1.tire_type}，是{car_1.light_type}，是{car_1.size}，是{car_1.is_pain}，是{car_1.is_new_energy}；而且{car_1.name}的最高速度是{car_1.max_speed}公里/小时,并且重量是{car_1.重量}吨')  
print(f'{car_2.name}的最高速度是{car_2.max_speed}公里/小时,并且重量是{car_2.重量}吨')
'''


'''
#引入pathlib模块的Path类
from pathlib import Path
# 获取当前脚本所在的文件夹路径，再拼接 text.txt
file_path = Path(__file__).parent / "text.txt"  


with open(file_path,"r") as f:
  line = f.readline()
  while line !="": #判断该行是否为空
    print(line)
    line = f.readline()
  lines = f.readlines()
  for i in  lines: #如果用for循环，就会打出跟上面一样的内容
    #如果不用for循环就会把整个列表打印出来
    print(i)    

with open(file_path,"r+") as f:
  f.write("123\n456\n789\n")
with open(file_path,"a") as f:
  f.write("this is new contents\n")
with open(file_path,"r+") as f:
  print(f.read())
'''



def getFilelastName(filename):
  return filename[filename.rfind(".") -1:] #就是切片，从点开始，点位0位，点后面位1位开始切，所以是+1
print(getFilelastName("example.txt")) # 输出 "e.txt"
print(getFilelastName("example.tar.gz")) # 输出 "r.gz"  

from pathlib import Path
with open(Path(__file__).parent / "text.txt","w+") as f:
  f.write("不错，很好\n666\n") #新建一个文件，此时写入，文件读取到最后一行，打印读取是空
  s= f.tell() #返回文件当前位置
  f.seek(0,0)#移动文件对象到最初,也是切片方法
  str = f.read()
  print(s,'\n',str,len(str)) #打印当前位置，读取的内容，读取内容的长度

