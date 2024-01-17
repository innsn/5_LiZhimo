import json

# 读取第一个文件
with open('output.json', 'r', encoding='utf-8') as file1:
    data1 = json.load(file1)

# 读取第二个文件
with open('output3.json', 'r', encoding='utf-8') as file2:
    data2 = json.load(file2)

# 读取第三个文件
with open('output2.json', 'r', encoding='utf-8') as file3:
    data3 = json.load(file3)

# 合并数据
merged_data = {
    'nodes': data1['nodes'] + data2['nodes'] + data3['nodes'],
    'links': data1['links'] + data2['links'] + data3['links']
}

# 将合并后的数据写入新文件
with open('merged_output.json', 'w', encoding='utf-8') as output_file:
    json.dump(merged_data, output_file, ensure_ascii=False, indent=4)
