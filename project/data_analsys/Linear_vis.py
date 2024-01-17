import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import mpl
sns.set_theme(style="white",font_scale=2,font="simhei")
# Load the example mpg dataset
mpg = sns.load_dataset("mpg")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import mpl
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})
rc = {'axes.unicode_minus': False}
sns.set(context='notebook', style='ticks', font='SimHei', rc=rc)
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

result = pd.read_csv('./关联分析/result.csv', encoding='utf-8')

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 假设你有这些数据
# 以下是示例数据，请替换成你的实际数据
pm25_data = np.array(result['PM2.5'])
pm10_data = np.array(result['PM10'])
so2_data=np.array(result['SO2'])
o3_data=np.array(result['O3'])
co_data=np.array(result['CO'])
no2_data=np.array(result['NO2'])
electricity_data = np.array(result['发电量'])
gdp_per_capita_data = np.array(result['人均gdp'])

# 将数据转换为二维数组
X = np.column_stack((pm25_data, pm10_data,so2_data,o3_data,co_data,no2_data))

from sklearn.preprocessing import StandardScaler

# Concatenate the feature arrays into a 2D array
X = np.column_stack((pm25_data, pm10_data, so2_data, o3_data, co_data, no2_data))

# Normalize the feature variables using StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

# X_normalized now contains the normalized feature values


# 用电量和人均 GDP 作为目标变量
y_electricity = electricity_data
y_gdp_per_capita = gdp_per_capita_data

# 创建并训练用于拟合用电量的线性回归模型
model_electricity = LinearRegression()
model_electricity.fit(X, y_electricity)

# 创建并训练用于拟合人均 GDP 的线性回归模型
model_gdp_per_capita = LinearRegression()
model_gdp_per_capita.fit(X, y_gdp_per_capita)


# 用电量的拟合曲线
# 创建一个新的DataFrame保存原始数据和预测结果
# 预测电量和人均GDP
predicted_electricity = model_electricity.predict(X)
predicted_gdp_per_capita = model_gdp_per_capita.predict(X)

# 创建一个新的DataFrame保存原始数据和预测结果
plot_data = pd.DataFrame({
    'pm25_data': pm25_data,
    'pm10_data': pm10_data,
    'so2_data': so2_data,
    'o3_data': o3_data,
    'co_data': co_data,
    'no2_data': no2_data,
    '发电量': electricity_data,
    '发电量预测值': predicted_electricity,
    '人均gdp': gdp_per_capita_data,
    '人均gdp预测值': predicted_gdp_per_capita
})




# 绘制发电量实际值与预测值比较图
plt.figure(figsize=(10, 6))
plt.plot(plot_data.index, plot_data['发电量'], marker='o', label='实际发电量')
plt.plot(plot_data.index, plot_data['发电量预测值'], linestyle='--', marker='x', label='预测发电量')
plt.xlabel('样本编号')
plt.ylabel('发电量')
plt.legend()
plt.title('发电量的实际值与预测值比较')
plt.grid(True)
plt.tight_layout()
plt.show()

# 绘制人均 GDP 实际值与预测值比较图
plt.figure(figsize=(10, 6))
plt.plot(plot_data.index, plot_data['人均gdp'], marker='s', label='实际人均GDP')
plt.plot(plot_data.index, plot_data['人均gdp预测值'], linestyle='--', marker='d', label='预测人均GDP')
plt.xlabel('样本编号')
plt.ylabel('人均GDP')
plt.legend()
plt.title('人均GDP的实际值与预测值比较')
plt.grid(True)
plt.tight_layout()
plt.show()

coefficients_electricity = model_electricity.coef_
intercept_electricity = model_electricity.intercept_

# Extract coefficients and intercept for GDP per capita model
coefficients_gdp_per_capita = model_gdp_per_capita.coef_
intercept_gdp_per_capita = model_gdp_per_capita.intercept_

# Prepare data for plotting
parameters_data = {
    'Feature': ['PM2.5', 'PM10', 'SO2', 'O3', 'CO', 'NO2'],
    'Electricity Coefficients': coefficients_electricity,
    'GDP per Capita Coefficients': coefficients_gdp_per_capita
}

# Convert parameters data to a DataFrame
parameters_df = pd.DataFrame(parameters_data)

# Plotting the coefficients as a bar chart
plt.figure(figsize=(10, 6))

# Bar width
bar_width = 0.35

# Position of bars on x-axis
index = np.arange(len(parameters_df['Feature']))

# Plotting Electricity Coefficients
plt.bar(index, parameters_df['Electricity Coefficients'], bar_width, label='Electricity')
# Plotting GDP per Capita Coefficients
plt.bar(index + bar_width, parameters_df['GDP per Capita Coefficients'], bar_width, label='GDP per Capita')

# Labeling axes and title
plt.xlabel('Features')
plt.ylabel('Coefficients')
plt.title('Linear Regression Coefficients')
plt.xticks(index + bar_width / 2, parameters_df['Feature'])
plt.legend()
plt.tight_layout()

# Show plot
plt.show()