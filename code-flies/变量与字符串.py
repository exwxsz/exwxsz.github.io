print('123') 
print("let's go") #字符串双引号成对，双引号中可以包含单引号避免出错
print('"let love i waht "') #单引号出现，包输出包括双引号
print('\"Life is short, Let\'s Lean Python\"') #\\反斜杠(\) ; \' 单引号(') ; \" 双引号(") ; \n 换行 ; \t 制表符 ; \a 响铃(BEL) ; \b 退格符 ; \r 回车符 ; \f 换页符 ; \ooo 八进制数 ; \xhh 十六进制数
print("D:\\three\\two\\one") #原始字符串，\t就相当于手动tab对齐缩进
print("""
跨行字符串
无需\n繁琐结尾
""")
print("     \n\
      1     \n\
      23    \n\
      456   \n\
      7890   \n")#若\n后面再加\则未结尾需要写完，\n即为结果

# guess = input("用户输入内容并返回给python，但输入的内容需要判断为数字时需要转义")

import random #导入random模块，random模块包含了很多函数，可以用来生成随机数，随机选择等功能.alt+p是重复上次输入的内容，alt+shift+p是重复上次输入的内容并且在末尾添加一个换行符
save_state = random.getstate() #保存当前的随机数生成器的状态，getstate()函数返回一个对象，包含了当前随机数生成器的状态，可以用来恢复随机数生成器的状态
answer = random.randint(1,10) #生成一个1到10之间的随机整数，randint(a,b)函数返回一个a到b之间的随机整数，包括a和b
random.setstate(save_state) #恢复之前保存的随机数生成器的状态，setstate(state)函数将随机数生成器的状态设置为state，这样就可以恢复之前保存的状态


const = 3
# while const > 0:
      # print("const is less than 3")
      # const = const - 1 # 循环，当const大于0时，输出const is less than 3，并且每次循环结束后const减1，直到const不大于0时结束循环
while const > 0: #这里以前错了，以前是const < 3导致无法运行。所有内容都必须在while循环，就像刚刚27-31行，不会进行循环
      temp = input("请输入一个数字：")
      guess = int(temp) #进行提取整数数字，只能输入的是数字才能提取
      print("你输入的数字是：", guess) #一般来说，print输出是会直接输出双引号单引号的内容，若没有引号则会直接输出原本形式，若为变量则直接是变量的内容，且需要以英文形式下的逗号隔开
#普通if判断类型：（==）是判断是否相等；(!=)是判断左右两边不相等；(is)是判断左右两边是否是同一个对象，(is not)是判断左右两边是否不是同一个对象
# const = 3
# while const > 0:
      # print("const is less than 3")
      # const = const - 1 # 循环，当const大于0时，输出const is less than 3，并且每次循环结束后const减1，直到const不大于0时结束循环
# while const < 3:
      if guess == answer :
            print("yes\njust yes on more things")
            break #break必须在此时的作用，用户输入正确就跳出循环，错误就跳出  当guess不等于5时，输出scorry,小了或者大了，并且每次循环结束后const减1，直到const不小于3时结束循环，并且当guess不等于5时，直接跳出循环，不再继续判断guess是否小于5或者大于5
      else:
            if answer > guess: #输入错误，if缩进下继续，else接着，继续if函数判断
                  print("scorry,小了")
            else:
                  print("大了")
            const = const - 1 #当const小于3时，判断guess是否等于5，若等于5则输出yes，否则判断guess是否小于5，若小于5则输出scorry,小了，否则输出大了，并且每次循环结束后const减1，直到const不小于3时结束循环
      #并且，const必须跟else对齐，否则会出现语法错误，python是通过缩进来判断代码块的开始和结束的
      #踏马的这里多写了一个break导致无法循环 当guess不等于5时，输出scorry,小了或者大了，并且每次循环结束后const减1，直到const不小于3时结束循环，并且当guess不等于5时，直接跳出循环，不再继续判断guess是否小于5或者大于5
print("user is yes  ",answer) #当guess等于5时，输出yes，并且每次循环结束后const减1，直到const不小于3时结束循环，并且当guess等于5时，直接跳出循环，不再继续判断guess是否小于5或者大于5


# 总结，对于上面的情况，获取的为随机数：先getstaet()保存当前的随机数生成器的状态，然后使用randint()生成一个随机整数，最后使用setstate()恢复之前保存的随机数生成器的状态，这样就可以保证每次运行程序时生成的随机数都是相同的，方便调试和测试。、
# 但是，无法利用这种方法在下次获取随机数时得到第一次获取的相同随机数，只能单次重复调用。下面复刻重复随机数，但无法用在上面， 用在上面要os模块的文件操作，保存状态到文件中，下次运行程序时从文件中读取状态并恢复，这样就可以在多次运行程序时得到相同的随机数。
