import pandas as pd

data = pd.read_csv("test.csv")

# 数据过滤
df_filter = data.loc[(data['from_level'] == '一般节点') & (data['traffic'] != 0)]
df_filter

# 加权采样
conversion = {'一般节点': 1, '网络核心': 5}
data_weight = data.copy()
data_weight['to_level'].replace(conversion, inplace=True)
df_weight = data_weight.sample(n=50, weights='to_dev', random_state=1)
df_weight.head(5)

# 分层采样
data['to_level'].value_counts()  # 查看一般节点和网络核心数量,得到分层抽样个数：一般19 网络31
group = data.groupby('to_level')
df_stratified = group.apply(lambda x: x.sample(n=31) if x.name == '网络核心' else x.sample(n=19))

# 随机采样
df_rand = data.sample(n=50, random_state=1)
df_rand.head()