import pandas as pd
import json

# 读取 Excel 文件
df = pd.read_excel('桑葚图.xlsx')
# 获取年份和其他列名作为节点
years = df['年份'].tolist()
columns = df.columns.tolist()[1:]  # 获取除了年份列外的其他列名

nodes = [{'name': year} for year in years] + [{'name': col} for col in columns]

# 构建 links
links = []
for year in years:
    for col in columns:
        value = df.loc[df['年份'] == year, col].values[0]
        links.append({'source': year, 'target': col, 'value': float(value)})

# 创建 JSON 数据
json_data = {'nodes': nodes, 'links': links}

# 将数据写入 JSON 文件
with open('output.json', 'w') as f:
    json.dump(json_data, f, indent=4)
