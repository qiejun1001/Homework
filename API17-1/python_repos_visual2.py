import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
 
# 获取语言前10个项目数据
def get_data(language):
	# 执行API调用并存储响应
	URL = 'https://api.github.com/search/repositories?q=language:' + language + '&sort=star'
	r = requests.get(URL)
	print("Status code:", r.status_code)
	# 将API响应存储在一个变量中
	response_dict = r.json()
	print("Total repositories:", response_dict['total_count'])
	# 研究有关仓库的信息
	repo_dicts = response_dict['items']
	
	plot_dicts = []
	for repo_dict in repo_dicts[:10]:
		
		plot_dict = {
			'value': repo_dict['stargazers_count'],
			'label': str(repo_dict['description']),
			'xlink': repo_dict['html_url'],
		}
		plot_dicts.append(plot_dict)
	return plot_dicts
 
 
# 可视化
my_config = pygal.Config()

my_config.show_legend = True
my_config.title_font_size = 24
my_config.label_font_size = 14

my_config.show_y_guides = True
my_config.width = 1000
 

chart = pygal.Bar(my_config)
chart.title = 'Most-Starred JavaScript, Ruby, C, Java, Perl, Haskell, Go Projects on GitHub'
chart.x_labels = range(1, 11)
 

languages = ['JavaScript', 'Ruby', 'C', 'Java', 'Perl', 'Haskell', 'Go']
for language in languages:
	plot_dicts = get_data(language)
	chart.add(language, plot_dicts)
 
chart.render_to_file('python_repos3.svg')