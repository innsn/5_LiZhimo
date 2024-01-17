import os
os.environ["PATH"] += os.pathsep + 'G:/program_files/graphviz/bin'

from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import export_graphviz
import graphviz

# 加载数据集
df = pd.read_csv("D:/计算机大三上/大数据分析实践/project/CN-Reanalysis201301/201301/CN-Reanalysis-daily-2013010100.csv", nrows=100)
df = df.drop(columns=[' '])
df['speed'] = df.apply(lambda row: (row[' lat']**2 + row[' lon']**2)**0.5, axis=1)
df = df.drop(columns=[' lat', ' lon'])

# 选择特征和目标变量
# Renaming columns to abbreviations
df.rename(columns={
    'PM2.5(微克每立方米)': 'PM2.5',
    ' PM10(微克每立方米)': 'PM10',
    ' NO2(微克每立方米)': 'NO2',
    ' CO(毫克每立方米)': 'CO',
    ' O3(微克每立方米)': 'O3',
    ' SO2(微克每立方米)': 'SO2',
    ' U(m/s)': 'U',
    ' V(m/s)': 'V',
    ' TEMP(K)': 'TEMP',
    ' RH(%)': 'RH',
    ' PSFC(Pa)': 'PSFC',
}, inplace=True)

# Reassigning X and y with abbreviated column names
X = df[['PM2.5', 'PM10', 'NO2', 'CO', 'O3', 'U', 'V', 'TEMP', 'RH', 'PSFC', 'speed']]  # Selecting feature columns
y = df['SO2']  # Selecting target variable column


# 构建随机森林回归模型
clf = RandomForestRegressor(n_estimators=100, random_state=42)
clf.fit(X, y)


def get_tree_paths(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != -2 else "undefined!"
        for i in tree_.feature
    ]

    paths = []

    def recurse(node, path):
        if tree_.feature[node] != -2:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            left_child = tree_.children_left[node]
            right_child = tree_.children_right[node]

            recurse(left_child, path + [f"{name} <= {threshold:.2f}"])
            recurse(right_child, path + [f"{name} > {threshold:.2f}"])
        else:
            paths.append({
                "value": tree_.value[node][0][0],
                "name": " ".join(path),
                "path": "/".join(path)
            })

    recurse(0, [])
    return paths


# Fetch tree paths and values for each tree in the Random Forest
tree_paths = []
for i, tree in enumerate(clf.estimators_):
    tree_paths.append({
        f'Tree_{i+1}': get_tree_paths(tree, X.columns)
    })

# Print or further process tree paths
for tree_path in tree_paths:
    print(tree_path)
    # Do something with each tree's paths

# Example of JSON output for the first tree paths
import json

# Assuming tree_paths contains the tree paths and values

# Write JSON data to a file with specific encoding
with open('tree_paths.json', 'w', encoding='utf-8') as f:
    json.dump(tree_paths[0], f, indent=4, ensure_ascii=False)
