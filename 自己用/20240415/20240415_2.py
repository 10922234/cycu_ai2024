import pandas as pd

import matplotlib.pyplot as plt

# 讀取 CSV 檔案
df = pd.read_csv(r'C:\Users\waes3\Downloads\titanic - 複製.csv')

# 創建一個新的 DataFrame，其中包含 'age'、'survival=0 時的數目'、'survival=1 時的數目' 和 '前兩項的加總' 這四個欄位
pivot_df = df.pivot_table(index='age', columns='survival', aggfunc='size', fill_value=0)
pivot_df.columns = ['survival=0', 'survival=1']
pivot_df['total'] = pivot_df['survival=0'] + pivot_df['survival=1']

# 將 'age' 每 20 為一個區段放在 x 軸
pivot_df['age_group'] = pd.cut(pivot_df.index, bins=range(0, 101, 20), right=False)


# 繪製長條圖
pivot_df[['survival=0', 'survival=1']].plot(kind='bar')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.title('Survival Count by Age Group')
plt.show()