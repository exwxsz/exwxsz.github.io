'''
#对象.方法名(内容)
#函数名(对象)
s="Hello"
print(s.upper())
shopping_list = ['apple','banana','orange']
shopping_list.append('pear')
shopping_list.remove('banana')
print(shopping_list)#去掉banana,添加pear
number_list = [1,65,21,64,23,14]
number_list.sort() # 重新排序
print(number_list,len(number_list))#打印number_list并打印长度
print(min(number_list),max(number_list))#打印最小值和最大值
'''

'''slang_dict = {"川然":"暖我一晚，哈哈",
              "散落的晓星尘":"感谢UP主 , 我是初中学历 , 每天学一课 , 学了差不多一个月多 , 每天练习一点 , 在学到26课面向对象编程前给自己做了一个小复习 (刚用金山打字通练会盲打). 因为初中小学基本上没有学 , 写单词的时候以及 , 进行数学计算的时候很吃力 , 所以我准备学完这套课程后去补一下数学以及英语 , 感谢UP主的教导 !",
              "卡密-神马":"我最讨厌一些教学机构学编程语言就教你什么算水仙花数，质数啥的，学了半天都不知道怎么导包，引入第三方库把学的语言真正变成你的生产力工具",
              }
#原先定义的一个字典，{键:值}
slang_dict["yamami_kana"]="没看完看了2/3，一个晚上加一个上午然后考期末过了（75分选择题25分编程，编程在后面的内容时间不够没看到后面所以没写出来，也就是说选择题基本全对），前来还愿，感谢up！！！"
slang_dict["为啥昵称总是修改失败"]="感谢up帮助本纯零基础小白启蒙！标题写的3小时，我花了5天时间才看完，现在依旧处于半懂不懂的状态。我觉得up视频的最大意义就是能够帮我这种纯小白快速建立知识体系，对python的各种应用场景有一点模糊且粗糙的认知。接下来再学各种几十个小时的视频的时候心里就有底了，而不是被直接劝退。非常喜欢up这种less is more的教学方式，期待up更多作品！"
slang_dict["阿拉斯塔西亚"]="全员体温正常的情况下，怎么才能让输出内容只有一次“其余人员体温正常”？"
#在原先已经定义的字典，添加新的字典；字典名["键"]="值"
query = input("请输入你想了解的词汇：")
if query in slang_dict:
  print(slang_dict[query])
else:
  print("抱歉，没有找到该词汇的解释。")
  print(f"当前已收录词汇:{len(slang_dict)}条")
'''

'''
def changfangxingdemianji(w,h):
  minaji_area = w*h
  return minaji_area #如果没有return，下面的输入打印只有None；
#因为此时的mianji_area只在函数里面显示，return相当于在函数外面定义了一个临时变量
print(changfangxingdemianji(4,5))
'''