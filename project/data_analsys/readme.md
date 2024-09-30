## matplotlib 中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

## get_location.py
高德逆地理编码

## type.py
hxh用，横轴为时间，纵轴为城市，记录城市污染类型

## AQI.py
计算特征值，求得AQI

## rand_forest
随机森林
tree tree_image tree_paths 可视化随机森林

## type.py pollution_type.py
污染类型

## sangsheng
桑基图，分解节点

## llm
网络上爬取合适语料，以地区污染情况为输入，通过对llm进行lora微调，希望llm得到合适的全国空气质量总结。
