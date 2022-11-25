# #类
# class person:
# 	def __init__(self,name,height,weight):
# 		self.name = name
# 		self.height = height
# 		self.weight = weight

# 	def say_name(self):
# 		print("my name is"+self.name) 

# 	def say_hellow(self,target_name):
# 		print("my name is"+self.name+",he is"+target_name)

# person1 = person("黄",180,140)
# person2 = person("林",170,120)

# person2.say_name()	#my name is林
# print(person1.height)	#180
# person1.say_hellow("李")		#my name is黄he is李


# d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59}
# # 更新dict
# d['Paul'] = 72  # 如果 key 已经存在，则赋值会用新的 value 替换掉原来的 value
# # 遍历dict
# for i in d:
#     print(i,':',d[i])

import random
print("########  猜数字小游戏   #########")
print("#  1.开始游戏  2.任意键退出游戏  #")
print("#    注：猜错三次游戏自动退出.   #")
print("##################################")
put = input("请输入：")
if put == "1":
    number = 3
    secret = random.randint(1, 100)
    while number > 0:
        temp = input("不妨猜一下我现心里想的数字是几：")
        temp2 = temp.strip()
        if temp2.isdigit():
            temp1 = int(temp2)
            if temp1 == secret:
                exit("哼,我心里想的数是%s，你居然猜中了，猜中也没有奖励^_^ 游戏结束！"%secret)
            elif number == 1:
                exit("没想到你那么笨三次机会都没有猜到!不妨告诉你,我心理想的数字是:%s" % (secret))
            elif temp1 > secret:
                print("我心想的数字比%s小,还是剩%s次机会"%(temp1,number-1))
            else:
                print("我心想的数字比%s大,还是剩%s次机会"%(temp1,number-1))
        else:
            print("Error:'%s'不是一个数字，请输入一个整数" % temp)
            number += 1
        number -= 1
else:
    exit("退出游戏成功!")
