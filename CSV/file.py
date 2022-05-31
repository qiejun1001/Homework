import csv
from shutil import which
from datetime import datetime
import matplotlib.pyplot as plt
from pyparsing import alphas

filename = r'E:\2022作业\Python\VSCode\CSV\sitka_weather_2018_simple.csv'
#打开文件并将返回的文件对象赋给f
with open(filename) as f:
    #创建一个与该文件相关的阅读器对象
    reader = csv.reader(f)
    #储存该文件的第一行
    header_row = next(reader)
    #从文件中获取日期、最高温度和最低温度
    dates,highs,lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#根据日期、最高温度和最低温度绘制图形
plt.style.use('seaborn')
fig,ax = plt.subplots()
#将数据点绘制为红色
ax.plot(dates,highs,c='red',alpha=0.5)
#将数据点绘制为蓝色
ax.plot(dates,lows,c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#设置图形格式
ax.set_title('锡特卡2018年每日最高温度',fontsize=24,fontproperties='SimHei')
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('温度 (F)',fontsize=16,fontproperties='SimHei')
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()
