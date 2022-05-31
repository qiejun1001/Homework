from fileinput import filename
import json
import plotly.express as px
import pandas as pd

from isort import file
from matplotlib.pyplot import title

#探索数据结构
filename = r'E:\2022作业\Python\VSCode\JSON\eq_data_30_day_m1.json'
with open(filename) as f:
    #加载文件数据并进行储存
    all_ep_data=json.load(f)
#创建列表，其中包含地震的各种信息
all_ep_dicts = all_ep_data['features']

#创建空列表用于储存震级、标题、经度、纬度
mags,titles,lons,lats = [],[],[],[]
for eq_dict in all_ep_dicts:
    #每次地震的震级储存在字典properties的mag键下
    mag = eq_dict['properties']['mag']
    #提取字典properties的title键下对应的值
    title = eq_dict['properties']['title']
    #提取与coordinates相关联的列表的第一个值：经度
    lon = eq_dict['geometry']['coordinates'][0]
    #提取与coordinates相关联的列表的第二个值：纬度
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

#将需要的数据进行封装
data = pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']
)
data.head()

#创建一个fig实例
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
)

#将可视化图保存为html文件   
fig.write_html('global_earthquakes10.html')