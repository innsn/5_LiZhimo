import pandas as pd
import numpy as np

df = pd.read_csv("D:/计算机大三上/大数据分析实践/project/CN-Reanalysis201301/201301/CN-Reanalysis-daily-2013010100.csv")
for year in range(2013, 2019):
    for i in range(1, 13):
        for j in range(1, 32):
            month = str(i).zfill(2)
            day = str(j).zfill(2)
            try:
                with open(
                        "D:/homework/Bigdata_Analysis_Practice/{}_merge/{}{}/{}{}{}00_merge.csv".format(year, year,
                                                                                                        month, year,
                                                                                                        month, day),
                        encoding='utf-8') as f:
                    df_temp = pd.read_csv(f)
                    if year == 2013 & i == 1 & j == 1:
                        continue
                    df = pd.concat([df, df_temp])
            except FileNotFoundError:
                continue

df.set_index(['省', '市'], inplace=True)

max_layer = pd.read_csv("D:/homework/Bigdata_Analysis_Practice/big/data/max_layer.csv")
max_layer.set_index(['省', '市'], inplace=True)

# print(max_layer)


result = []
tYpe = ''
for row_id in range(df.shape[0]):
    df_lat = df.index[row_id][0]  # 修改这里以获取多级索引的值
    df_lon = df.index[row_id][1]  # 修改这里以获取多级索引的值
    df_PM2_5 = df.iloc[row_id]['PM2.5(微克每立方米)']
    df_PM10 = df.iloc[row_id][' PM10(微克每立方米)']
    df_SO2 = df.iloc[row_id][' SO2(微克每立方米)']
    df_NO2 = df.iloc[row_id][' NO2(微克每立方米)']
    df_CO = df.iloc[row_id][' CO(毫克每立方米)']

    # 修正获取 max_layer 中数据的方式
    max_all = max_layer.loc[(df_lat, df_lon)]

    max_PM2_5 = float(max_all['PM2.5(微克每立方米)'])
    max_PM10 = float(max_all[' PM10(微克每立方米)'])
    max_SO2 = float(max_all[' SO2(微克每立方米)'])
    max_NO2 = float(max_all[' NO2(微克每立方米)'])
    max_CO = float(max_all[' CO(毫克每立方米)'])

    if df_PM2_5 > max_PM2_5:
        tYpe = '偏二次型'
    elif df_PM10 > max_PM10:
        tYpe = '偏沙尘型'
    elif df_SO2 > max_SO2:
        tYpe = '偏燃煤型'
    elif (df_NO2 > max_NO2) & (df_CO > max_CO):
        tYpe = '偏机动车型'
    elif (df_PM2_5 > max_PM2_5) & (df_SO2 > max_SO2):
        tYpe = '偏烟花型'
    elif (df_SO2 > max_SO2) & (df_NO2 > max_NO2) & (df_CO > max_CO):
        tYpe = '偏钢铁型'
    else:
        tYpe = '标准型'

    result.append(tYpe)
    print(len(result))

df['type'] = result
# print(df.index[0][0])
# df = df.drop(index=df[(df.index[0][0] == '[]')].index.tolist())
# df.to_csv("all_date_type.csv")
df = df.drop(columns=['PM2.5(微克每立方米)', ' SO2(微克每立方米)', ' PM10(微克每立方米)', ' NO2(微克每立方米)', ' CO(毫克每立方米)'])
df.to_csv("D:/homework/Bigdata_Analysis_Practice/big/data/only_all_date_type.csv")
