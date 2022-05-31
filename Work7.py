#练习8-1：消息

# def display_message():
#     print("学习了传递实参。")
# display_message()


#练习8-3：T恤

# def make_shirt(size,word):
#     print(f"这件衣服的尺码是{size}，字样是{word}")
# make_shirt(1,2)


#练习8-4：大号T恤

# def make_shirt(size='大号',word='I Love Python'):
#     if (size==None) and (word==None):
#         print(f"这件衣服的尺码是大号，字样是I Love Python")
#     elif word==None:
#          print(f"这件衣服的尺码是{size}，字样是I Love Python")
#     else:
#         print(f"这件衣服的尺码是{size}，字样是{word}")
# make_shirt()
# make_shirt('中号')
# make_shirt(1,2)


#练习8-7：专辑 

# def make_album(singer,album):
#     information = {"singer":singer,"album":album}
#     return information
# print (make_album('Aqours','LIVE with a smile'))
# print (make_album('Aqours','i-n-g'))
# print (make_album('Aqours','JIMO-AI'))

# def make_album2(singer,album,song_number=None):
#     if song_number:
#         information = {"singer":singer,"album":album,"song_number":{song_number}}
#     else:
#         information = {"singer":singer,"album":album}
#     return information
# print (make_album2('Aqours','LIVE with a smile'))
# print (make_album2('Aqours','i-n-g','5'))


#练习8-8：用户的专辑

# def make_album(singer,album,song_number=None):
#     if song_number:
#         information = {"singer":singer,"album":album,"song_number":{song_number}}
#     else:
#         information = {"singer":singer,"album":album}
#     return information

# while True:
#     singer = '请输入歌手名：'
#     singer += '\n 输入\'q\' 停止进程'
#     album = '请输入专辑名称：'
#     album += '\n 输入\'q\' 停止进程'
#     singer_name = input(singer)
#     if singer_name == 'q':
#         break
#     album_name = input(album)
#     if album_name == 'q':
#         break
#     output = make_album(singer_name,album_name)
#     print(output)


# 练习8-9：消息

messages = ['太好听了吧！！！','你逢田姐当然会。。。','Hey guys~']
def show_messages(note):
    for message in messages:
        print(message)
show_messages(messages)


# 练习8-10：发送消息

# messages = ['太好听了吧！！！','你逢田姐当然会。。。','Hey guys~']
# sent_messages = []

# def send_messages(note):
#     print(f"messages:\n{messages}")
#     while note:
#         popped_message = note.pop()
#         sent_messages.append(popped_message)

# send_messages(messages)
# print(f"messages:\n{messages}")
# print(f"sent_messages:\n{sent_messages}")


# 练习8-11：消息归档

# messages = ['太好听了吧！！！','你逢田姐当然会。。。','Hey guys~']
# sent_messages = []

# def send_messages(note):
#     print(f"messages:\n{messages}")
#     while note:
#         popped_message = note.pop()
#         sent_messages.append(popped_message)

# send_messages(messages[:])
# print(f"messages:\n{messages}")
# print(f"sent_messages:\n{sent_messages}")


# 练习8-14：汽车

# from turtle import color


# def make_car(manufacturer,model,**args):
#     print(f"manufacturer is {manufacturer},model is {model},and {args}")
# car = make_car('subaru','outback',color='blue',tow_package=True)
# car

# 附加题1
# def add_place_values(number):
#     place_value = 0
#     while number > 0:
#         place_value += number % 10
#         number = number // 10
#     return place_value


# print(add_place_values(12345))

# my_list = [989, 123, 456, 789, 99, 923]
# my_list.sort(key=add_place_values)
# print(my_list)


# 附加题2
print(list(map(lambda x: x ** 2 + 1, range(1, 10))))

# 搜索违法的公司
companies = {
    'CoolCompany': {'Alice': 33, 'Bob': 28, 'Frank': 29},
    'CheapCompany': {'Ann': 4, 'Lee': 9, 'Chris': 7},
    'SosoCompany': {'Esther': 38, 'Cole': 8, 'Paris': 18}
}

print([company for company in companies if any(salary < 9 for salary in companies[company].values())])
