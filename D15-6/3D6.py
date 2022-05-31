import pygal
from die import Die
 
 #创建三个D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

#掷多次骰子，并将结果存储在列表里
results = []
#投掷次数为1000
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

#空列表，用于储存各个面出现的次数 
frenquncies = []
#计算出现的最大点数
max_reuslt = die_1.num_sides + die_2.num_sides +die_3.num_sides
#遍历可能的点数
for value in range(3, max_reuslt+1):
    #计算每种点数出现的次数
    frenquncy = results.count(value)
    #将值添加到空列表的末尾
    frenquncies.append((frenquncy))

# 绘制条形图 
hist = pygal.Bar()
hist.title= "同时投掷三个D6的筛子"

#设置坐标轴标签 
hist.x_labels = [x for x in range(3,19)]
hist.x_title = "结果"
hist.y_title = "结果频率"
 
hist.add("D6 + D6 + D6",frenquncies)
#生成条形图的svg文件
hist.render_to_file('3d6.svg')
