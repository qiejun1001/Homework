# 练习10-1：Python学习笔记

# from importlib.resources import contents


# with open ('Txt\learning_python.txt') as L:contents =L.read()
# print(contents.rstrip())

# with open ('Txt\learning_python.txt') as L:
#     for line in L:
#         print(line.rstrip())

# with open ('Txt\learning_python.txt') as L:
#     lines= L.readlines()
#     for line in lines:
#         print(line.rstrip())

# 练习10-3：访客

# name = '请输入您的姓名：'
# with open('guest.txt','w') as L:
#     contents= L.write(input(name))

# 练习10-4：访客名单

# from importlib.resources import contents


# prompt = '请输入你的名字:'
# name = 1
# while name:
#     name= input(prompt)
#     if name == 'q':
#         break

#     print(f'亲爱的{name}，这是一条和蔼的问候语')
#     with open('Txt\guest_book.txt','a') as L:
#         contents = L.write(f'{name}\n')

# 练习10-6：加法运算

# try:
#     a=int(input('请输入数字a：'))
#     b=int(input('请输入数字b：'))
# except ValueError:
#     print('请输入阿拉伯数字谢谢配合')
# else:
#     print(f'a+b={a+b}')


# 练习10-7：加法计算器 

# while True:
#     try:
#         a=int(input('请输入数字a：'))
#         b=int(input('请输入数字b：'))
#     except ValueError:
#         print('请输入阿拉伯数字谢谢配合')
#     else:
#         print(f'a+b={a+b}')

# 练习10-11：喜欢的数

# import json
# import numbers
# number = input ('请输入你喜欢的数字：')

# with open('Txt/f_number.txt','w') as N:
#     json.dump(number,N)
# with open('Txt/f_number.txt') as N:
#     f_number = json.load(N)
#     print(f'我晓得你喜欢的数字是哪个！肯定是{f_number}')

# 练习10-12：记住喜欢的数

# from importlib.resources import contents
# import json
# number = input('请输入你喜欢的数字：')
# with open('Txt/f_number.txt') as N:
#     content = N.read()
#     if (number in content):
#         print(f'我晓得你喜欢的数字是哪个！肯定是{number}')
#     else :
#         with open('Txt/f_number.txt','w') as N:
#             json.dump(number,N)
#         with open('Txt/f_number.txt') as N:
#             f_number = json.load(N)
#             print(f'我晓得你喜欢的数字是哪个！肯定是{f_number}')


# 附加题1
# with open('Txt/pai.txt') as file:
#     lines = file.readlines()

# pi_string = ''
# for line in lines:
#     pi_string += line.strip()

# import datetime
# import json

# start_date = datetime.datetime.strptime("20220101", '%Y%m%d')
# end_date = datetime.datetime.strptime("20221231", '%Y%m%d')
# date_list = []
# while start_date <= end_date:
#     date_list.append(start_date.strftime('%m%d'))
#     start_date += datetime.timedelta(days=1)

# result_list = []
# for date_str in date_list:
#     if date_str in pi_string:
#         result_list.append(date_str)

# print(result_list)


# start_date = datetime.datetime.strptime("20010101", '%Y%m%d')
# end_date = datetime.datetime.strptime("20201231", '%Y%m%d')
# date_list = []
# while start_date <= end_date:
#     date_list.append(start_date.strftime('%Y%m%d'))
#     start_date += datetime.timedelta(days=1)

# result_list = []
# for date_str in date_list:
#     if date_str in pi_string:
#         result_list.append(date_str)

# print(result_list)


# zh_name = '佩佩'.encode('utf-8')
# en_name = 'Zhang San'.encode('utf-8')

# hex_zh_name = bytes(zh_name.hex(), encoding='utf-8')
# hex_en_name = bytes(en_name.hex(), encoding='utf-8')

# decimal_zh_name = int(hex_zh_name, 16)
# decimal_en_name = int(hex_en_name, 16)

# if str(decimal_zh_name) in pi_string:
#     print("佩佩在pai中出现了！")
# else:
#     print("佩佩在pai中没有出现！")
# if str(decimal_en_name) in pi_string:
#     print("Zhang san在pai中出现了！")
# else:
#     print("Zhang san在pai中没有出现！")


# 附加题2
with open('Txt/alice.txt',encoding='utf-8') as file:
    lines = file.readlines()

text = ''
for line in lines:
    text += line.strip().lower()

word_list = text.split()

frequency = {}
for word in word_list:
    frequency[word] = frequency.get(word, 0) + 1

print("书中出现次数最多的7个英文单词是：", end="")
for i in range(7):
    max_word = max(frequency, key=frequency.get)
    print(max_word, end=' ')
    del frequency[max_word]

print()
print("长度大于等于5的英语单词中，出现次数最多的7个英文单词是：", end="")
for i in range(7):
    max_word = max(frequency, key=lambda x: frequency[x] if len(x) >= 5 else 0)
    print(max_word, end=' ')
    del frequency[max_word]


# 附加题3
# import json


# username = input("请输入用户名：")
# password = input("请输入密码：")
# user = {
#     'username': username,
#     'password': password
# }

# with open('user.json', 'w') as file:
#     json.dump(user, file)
#     print("用户数据保存成功！")

# username = input("请输入用户名：")
# password = input("请输入密码：")

# with open('user.json') as file:
#     user = json.load(file)
#     if username == user['username'] and password == user['password']:
#         print("登录成功！")
#     else:
#         print("登录失败！")

# username = input("请输入用户名：")
# password = input("请输入密码：")
# new_password = input("请输入新密码：")

# with open('user.json') as file:
#     user = json.load(file)

# if username == user['username'] and password == user['password']:
#     if password != new_password:
#         user = {
#             'username': username,
#             'password': new_password
#         }
#         with open('user.json', 'w') as file:
#             json.dump(user, file)
#         print("修改密码成功！")
#     else:
#         print("新密码不能与旧密码相同！")
# else:
#     print("用户名或密码错误！")










