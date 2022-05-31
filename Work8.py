# 练习9-1：餐馆

from operator import index
from unicodedata import name
from unittest import result

class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def describe_restaurant(self):
        print(f"这个餐馆的名字是{self.name}这是一家{self.type}的餐馆。")
    def open_restaurant(self):
        print("餐厅正在营业。")


# My_Restaurant=Restaurant("好洽铺子","很辣")
# My_Restaurant.describe_restaurant()
# My_Restaurant.open_restaurant()

# 练习9-4：就餐人数

# class Restaurant:
#     def __init__(self,name,type,number_served):
#         self.name = name
#         self.type = type
#         self.number_served = 0
#     def describe_restaurant(self):
#         print(f"这个餐馆的名字是{self.name}这是一家{self.type}的餐馆。")
#     def open_restaurant(self):
#         print("餐厅正在营业。")
#     def set_number_served(self,a):
#         self.number_served = a
#         print(f"就餐人数为{self.number_served}。")
#     def increment_number_served(self,b):
#         self.number_served = b + self.number_served
#         print(f"每天参观可接待的用餐人数为{self.number_served}")
 
# My_Restaurant=Restaurant("好洽铺子","很辣",200)
# My_Restaurant.describe_restaurant()
# My_Restaurant.open_restaurant()
# My_Restaurant.set_number_served(100)
# My_Restaurant.increment_number_served(50)

# 附加

# restaurant = [("一号","很甜",100), ("二号","很酸",200), 
#               ("三号","很辣",300), ("四号","很苦",400), ("五号","很咸",500)]

# 练习9-6：冰激凌小店

# class IceCreamStand(Restaurant):
#     def __init__(self, name, type):
#         super().__init__(name, type)
#         self.flavors = []
#     def list_IceCream(self):
#         for flavor in self.flavors:
#             print(f"本店有{flavor}等多种口味。")
# My_IceCreamStand=IceCreamStand("蜜雪冰城","便宜")
# My_IceCreamStand.flavors=["柠檬冰淇淋","草莓冰淇淋","哈密瓜冰淇淋"]
# My_IceCreamStand.list_IceCream()

# # 练习9-13：骰子

# from random import randint

# class Die():
#     def __init__(self,sides=6):
#         self.sides = sides

#     def roll_die(self):
#         return randint(1,self.sides)

# die6 = Die()
# results = []
# for i in range(10):
#     result = die6.roll_die()
#     results.append(result)
# print(results)

# die10 = Die(sides=10)
# results = []
# for i in range(10):
#     result = die10.roll_die()
#     results.append(result)
# print(results)

# die20 = Die(sides=20)
# results = []
# for i in range(10):
#     result = die20.roll_die()
#     results.append(result)
# print(results)


# 练习9-14：彩票 

# number_word = [1,2,3,4,5,6,7,8,9,10,"a","s","d","f","g"]
# prize = []

# i=0
# while i<4:
#     index = randint(0,14)
#     prize.append(number_word[index])
#     i+=1

# print(prize)


# 练习9-15：彩票分析

# my_ticket = ["a","g",2,2]
# n = 0
# prize = []
# while my_ticket != prize:
#     prize = []
#     i = 0
#     while i<4:
#         index = randint(0,14)
#         prize.append(number_word[index])
#         i+=1
#     n += 1
# print(f"您将在第{n}次时获奖")


# 附加题：

# class Money:
#     def __init__(self,amount,currency):
#         self.amount = amount
#         self.currency = currency
#     def __str__(self):
#         return "面值是：%d，币种是：%s" %(self.amount,self.currency)
#     def __add__(self,other):
#         if self.currency != other.currency:
#            print("币种不同，无法相加")
#         else:
#            return Money(self.amount + other.amount,self.currency)
#     def __sub__(self,other):
#         if self.currency != other.currency:
#            print("币种不同，无法相减")
#         else:
#            return Money(self.amount - other.amount,self.currency)
#     def __mul__(self,other):
#         return Money(self.amount * other,self.currency)
#     def __truediv__(self,other):
#         return Money(self.amount / other,self.currency)
#     def __lt__(self,other):
#         if self.currency != other.currency:
#            print("币种不同，无法比较")
#         else:
#             return self.amount < other.amount
#     def __gt__(self,other):
#         if self.currency != other.currency:
#            print("币种不同，无法比较")
#         else:
#             return self.amount > other.amount
#     def __eq__(self,other):
#         if self.currency != other.currency:
#            print("币种不同，无法比较")
#         else:
#             return self.amount == other.amount

# My_Money1=Money(100,"rmb")
# My_Money2=Money(50,"rmb")
# My_Money3=Money(100,"rmb")
# My_Money4=Money(50,"$")
# My_Money5=My_Money1+My_Money2
# My_Money6=My_Money1-My_Money2
# My_Money7=My_Money1*2
# My_Money8=My_Money1/5
# print(My_Money1<My_Money2)
# print(My_Money1==My_Money2)
# print(My_Money1>My_Money2)
# print(My_Money1<My_Money4)
# My_Money9=My_Money1+My_Money4
# print(My_Money1)
# print(My_Money5)
# print(My_Money6)
# print(My_Money7)
# print(My_Money8)

# 附加题：

from dataclasses import dataclass

@dataclass

class Money:
    amount: int
    currency: str
    
My_Money=Money(50,"rmb")
print(f"面值是：{My_Money.amount}，币种是：{My_Money.currency}")