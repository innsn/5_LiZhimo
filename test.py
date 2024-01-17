import pandas as pd
import glob

# 创建一个空DataFrame来存储所有的数据
total_df = pd.DataFrame()

# 使用glob来获取所有符合条件的文件
files = glob.glob("D:/计算机大三上/大数据分析实践/project/CN-Reanalysis201301/201301/CN-Reanalysis-daily-201301*.csv")

# 循环读取每个文件并将数据合并到total_df中
for file in files:
    df_temp = pd.read_csv(file, dtype={'Value': float})
    total_df = total_df.add(df_temp, fill_value=0)

# 计算均值
average_df = total_df / len(files)

print(average_df)
