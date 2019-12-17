import requests
import pygal
from pygal.style import LightenStyle

#getting the response stored
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
res = requests.get(url)
print("Status code: ", res.status_code)
res_dict =res.json()
print('Total repos: ',res_dict['total_count'])
repo_dicts = res_dict['items']
print('Repos returned: ', len(repo_dicts))
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    if repo_dict['description']:
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink': repo_dict['html_url'],
        }
    else:
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': "N/A",
        }
    plot_dicts.append(plot_dict)
style = LightenStyle("#333366")

#defining a configuration
config = pygal.Config()
config.x_label_rotation = 45
config.show_legend = False
config.title_font_size = 24
config.label_font_size = 14
config.major_label_font_size = 18
config.truncate_label = 15
config.show_y_guides =False
config.width = 1000

#making the chart
chart = pygal.Bar(style=style, config=config)
chart.force_uri_protocol = 'http'
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
chart.add("", plot_dicts)
chart.render_to_file('visualizations\\python_repos.svg')