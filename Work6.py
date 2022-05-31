#练习7-2
# guest = input("请问有多少人用餐？\n")
# guest = int(guest)
# if guest <= 8:
#    print ("恭喜您，有空桌")
# else:
#    print ("很可惜，没有空桌")

# 练习7-4

# pizza = input("请输入您想吃的配料（结束请输入quit）：\n")
# while pizza != "quit":
#     print("我们会在披萨中添加" + pizza + "\n")
#     pizza = input("请输入您想吃的配料（结束请输入quit）：\n")
#     continue

#练习7-5

# age = input("请输入您的实际年龄（结束请输入quit）：\n")
# while age != "quit":
#     age = int (age)
#     if age < 3:
#         print("小宝宝可以免费观影哦~\n")
#         age = input("请输入您的实际年龄（结束请输入quit）：\n")
#         continue
#     elif age >=3 and age <= 12:
#         print("小朋友的票价是10美金哦\n")
#         age = input("请输入您的实际年龄（结束请输入quit）：\n")
#         continue
#     else:
#         print("青少年和大人朋友的票价是15美金哦\n")
#         age = input("请输入您的实际年龄（结束请输入quit）：\n")
#         continue

#练习7-6

# pizza = input("请输入您想吃的配料（结束请输入quit）：\n")
# while True:
#     print("我们会在披萨中添加" + pizza +"\n")
#     pizza = input("请输入您想吃的配料（结束请输入quit）：\n")
#     if pizza == "quit":
#         break

# pizza = input("请输入您想吃的配料：\n")
# active = True
# while active:
#     print("我们会在披萨中添加" + pizza +"\n")
#     pizza = input("请输入您想吃的配料（结束请输入quit）：\n")
#     if pizza == "quit":
#         active = False

#练习7-8

# sandwich_orders = ["帕尼尼","奶油香蕉","照烧鸡排"]
# finished_sandwiches = []
# print("三明治订单：")
# print(sandwich_orders)
# for order in sandwich_orders:
#     print("\n您的"+ order + "三明治已出炉！")
#     finished_sandwiches.append(order)
# for sandwich in finished_sandwiches:
#         print("\n制作完成的三明治有：" + sandwich)

#练习7-9

# sandwich_orders = ["帕尼尼","五香烟熏牛肉","照烧鸡排","五香烟熏牛肉","五香烟熏牛肉"]
# print("三明治订单：")
# print(sandwich_orders)
# print("五香烟熏牛肉已售罄！\n")
# while "五香烟熏牛肉" in sandwich_orders:
#     sandwich_orders.remove("五香烟熏牛肉")
# print("三明治订单：")
# print(sandwich_orders)

#附加题一
# wages = {}
# active2 = True
# while active2:
#      name = input("请输入您的名字：\n")
#      wage = input("请输入您的月收入：\n")
#      wage = int(wage)
#      wages[name] = wage
#      repeat = input("继续请输入y,结束请输入n：")
#      if repeat == "n":
#          active2 = False
# for name, wage in wages.items():
#     print(f"{name} 的月收入是：{wage}")

# list_w = [(name, wage) for name, wage in wages.items() if wage > 10000]
# print(list_w)

#附加题二

# text = '''
# Call me Ishmael. Some years ago - never mind how long precisely – having
# little or no money in my purse, and nothing particular to interest me
# on shore, I thought I would sail about a little and see the watery part
# of the world. It is a way I have of driving off the spleen, and
# regulating
# the circulation. - Moby Dick'''

# lines = [line for line in text .split('\n')] 
# print( lines )

# words = [word for line in text .split('\n') for word in line.split() if len(word) > 3]
# print (words)

# nested_list = [ [word for word in line.split() if len(word)>3] for line in text.split('\n')]
# print(nested_list)

#附加题三

# price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
# [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
# [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
# [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]
# price2 = [price[0][::2],price[1][::2],price[2][::2],price[3][::2]]
# print(price2)

#附加题四

# visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
#          'Safari', 'corrupted', 'Safari', 'corrupted',
#          'Chrome', 'corrupted', 'Firefox', 'corrupted']
# visitors[1::2] = visitors[::2]
# print(visitors)

#附加题五

# column_names = ['name', 'salary', 'job']
# db_rows = [('Alice', 180000, 'data scientist'),
# ('Bob', 99000, 'mid-level manager'),
# ('Frank', 87000, 'CEO')]

# tup1=db_rows[0]
# tup2=db_rows[1]
# tup3=db_rows[2]

# db_1 = [tup1[0],tup1[1],tup1[2]]
# db_2 = [tup2[0],tup2[1],tup2[2]]
# db_3 = [tup3[0],tup3[1],tup3[2]]

# r1 = dict(zip(column_names,db_1))
# r2 = dict(zip(column_names,db_2))
# r3 = dict(zip(column_names,db_3))

# list_all =[r1,r2,r3]
# print(list_all)


# 练习8-16：导入


from Work7 import messages
from Work7 import send_messages

messages

send_messages(messages)