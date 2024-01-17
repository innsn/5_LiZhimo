import pandas as pd
import numpy as np

# 读取数据并删除重复项
df = pd.read_csv("only_all_date_type.csv", index_col=False)
df = df.drop_duplicates(subset=["省", "市", "date", "type"], keep='first')

df = df.drop(df[(df['省'] == '[]') & (df['市'] == '[]')].index)
df['市'].replace('[]', np.nan, inplace=True)
df['市'].fillna(df['省'], inplace=True)

pivot_df = df.pivot(index=['省','市'], columns='date', values='type')
pivot_df.columns.name = None
pivot_df = pivot_df.reset_index()
pivot_df.to_csv('city_type_date.csv',index=False)