import json

# 以 'utf-8' 编码读取文件
with open('output.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 以 'utf-8' 编码写入文件
with open('polu1.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)  # 设置 ensure_ascii=False 可以确保写入非 ASCII 字符
