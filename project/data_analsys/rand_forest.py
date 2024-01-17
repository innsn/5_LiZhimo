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
X = df[['PM2.5(微克每立方米)', ' PM10(微克每立方米)',  ' NO2(微克每立方米)',
       ' CO(毫克每立方米)', ' O3(微克每立方米)', ' U(m/s)', ' V(m/s)', ' TEMP(K)',
       ' RH(%)', ' PSFC(Pa)', 'speed']]  # 选择特征列
y = df[' SO2(微克每立方米)']  # 选择目标变量列

# 构建随机森林回归模型
clf = RandomForestRegressor(n_estimators=100, random_state=42)
clf.fit(X, y)

# 获取特征重要性
feature_importances = clf.feature_importances_

# 从数据集中获取特征名称
feature_names = X.columns.tolist()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 创建特征重要性的条形图
plt.figure(figsize=(10, 6))
plt.barh(feature_names, feature_importances, align='center')
plt.xlabel('Feature Importance')
plt.title('Random Forest Feature Importance')
plt.show()

tree = clf.estimators_[0]

# 导出单棵决策树为dot文件
export_graphviz(
    tree,
    out_file='tree.dot',
    feature_names=X.columns.tolist(),  # 转换列索引为列表类型
    filled=True,
    rounded=True
)

# 将dot文件转换为PNG图像
with open('tree.dot', encoding='utf-8') as file:
    dot_graph = file.read()

graphviz.Source(dot_graph).render("tree_image", format="png", cleanup=True)
