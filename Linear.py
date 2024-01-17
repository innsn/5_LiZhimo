import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv("D:/计算机大三上/大数据分析实践/project/CN-Reanalysis201301/201301/CN-Reanalysis-daily-2013010100.csv", nrows=100)
df = df.drop(columns=[' '])
df['speed'] = df.apply(lambda row: (row[' lat']**2 + row[' lon']**2)**0.5, axis=1)
data = df.drop(columns=[' lat', ' lon'])
X = data[['PM2.5(微克每立方米)', ' PM10(微克每立方米)',  ' NO2(微克每立方米)',
       ' CO(毫克每立方米)', ' O3(微克每立方米)', ' U(m/s)', ' V(m/s)', ' TEMP(K)',
       ' RH(%)', ' PSFC(Pa)']]  # 选择特征列
y_gdp = data[' SO2(微克每立方米)']
y_power = data['speed']

X_train_gdp, X_test_gdp, y_train_gdp, y_test_gdp = train_test_split(X, y_gdp, test_size=0.2, random_state=42)
model_gdp = LinearRegression()
model_gdp.fit(X_train_gdp, y_train_gdp)

X_train_power, X_test_power, y_train_power, y_test_power = train_test_split(X, y_power, test_size=0.2, random_state=42)
model_power = LinearRegression()
model_power.fit(X_train_power, y_train_power)

# 打印人均 GDP 的模型参数和分数
print("人均GDP模型参数:")
print("系数:", model_gdp.coef_)
print("截距:", model_gdp.intercept_)
print("训练集得分:", model_gdp.score(X_train_gdp, y_train_gdp))
print("测试集得分:", model_gdp.score(X_test_gdp, y_test_gdp))

# 打印发电量的模型参数和分数
print("\n发电量模型参数:")
print("系数:", model_power.coef_)
print("截距:", model_power.intercept_)
print("训练集得分:", model_power.score(X_train_power, y_train_power))
print("测试集得分:", model_power.score(X_test_power, y_test_power))

# 预测人均 GDP
y_pred_gdp = model_gdp.predict(X_test_gdp)

# 计算均方误差和R^2分数（人均 GDP）
mse_gdp = mean_squared_error(y_test_gdp, y_pred_gdp)
rmse_gdp = np.sqrt(mse_gdp)
r2_gdp = r2_score(y_test_gdp, y_pred_gdp)

print("\n人均GDP模型评价指标:")
print("均方误差 (MSE):", mse_gdp)
print("均方根误差 (RMSE):", rmse_gdp)
print("R^2 分数:", r2_gdp)

# 预测发电量
y_pred_power = model_power.predict(X_test_power)

# 计算均方误差和R^2分数（发电量）
mse_power = mean_squared_error(y_test_power, y_pred_power)
rmse_power = np.sqrt(mse_power)
r2_power = r2_score(y_test_power, y_pred_power)

print("\n发电量模型评价指标:")
print("均方误差 (MSE):", mse_power)
print("均方根误差 (RMSE):", rmse_power)
print("R^2 分数:", r2_power)