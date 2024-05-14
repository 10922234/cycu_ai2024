import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 讀取 csv 文件
df = pd.read_csv('C:\\Users\\User\\Documents\\GitHub\\cycu_ai2024\\20240507\\M05A_31.csv')

# 將 GantryFrom、GantryTo 欄位轉換成數值型態
df['GantryFrom'] = df['GantryFrom'].apply(lambda x: int(x[3:7]) * 10 if x[-1] == 'N' else int(x[3:7]) * 10 + 1)
df['GantryTo'] = df['GantryTo'].apply(lambda x: int(x[3:7]) * 10 if x[-1] == 'N' else int(x[3:7]) * 10 + 1)


# 創建新的欄位 GantryFromTo
df['GantryFromTo'] = df['GantryFrom'] * 100000 + df['GantryTo']

# 將 GantryFromTo 設定為 x，TrafficVolume 設定為 y
x = df['GantryFromTo'].values
y = df['TrafficVolume'].values

# 使用 scipy 的 CubicSpline 來擬合 x 對 y 的關係
cs = CubicSpline(x, y)

# 畫出擬合後的曲線
x_new = np.linspace(x.min(), x.max(), 100)
y_new = cs(x_new)

plt.figure(figsize=(8, 4))
plt.plot(x, y, 'o', label='原始數據')
plt.plot(x_new, y_new, label='Cubic Spline 擬合曲線')
plt.xlabel('Traffic Volume')
plt.ylabel('Gantry From To')
plt.title('Traffic Volume 對 Gantry From To 的 Cubic Spline 擬合')
plt.legend()
plt.show()