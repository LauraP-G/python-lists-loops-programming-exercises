all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here
def generate_li(color):
    return f'<li>{color["label"]}</li>'

def filter_colors(list):
    return list['sexy']


color_sexy=list(filter(filter_colors, all_colors))
list_li = list(map(generate_li, color_sexy))

print(list_li)

