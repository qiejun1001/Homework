import requests

from plotly.graph_objs import Bar
from plotly import offline

#储存API调用的URL
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#显示要求使用该版本的API
headers = {'Accept': 'application/vnd.github.v3+json'}
#调用API
r = requests.get(url, headers=headers)
#核实调用是否成功
print(f"Status code: {r.status_code}")

# 将API响应赋给一个变量
response_dict = r.json()
#探索有关仓库信息
repo_dicts = response_dict['items']
#储存图表中出现的数据
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)


# 可视化
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

#使用字典定义图标布局
my_layout = {
    'title': 'GitHub上最受欢迎的Python项目',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': '仓库',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': '星数',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos2.html')
