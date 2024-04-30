import os
import glob
import pandas as pd

# 找到所有符合指定格式的檔案
files = glob.glob('C:/Users/User/Desktop/csv/TDCS_M03A_20240429_*.csv')

# 創建一個空的 DataFrame 來儲存所有的數據
all_data = pd.DataFrame()

# 對於每個找到的檔案
for file in files:
    # 讀取檔案
    df = pd.read_csv(file, header=None)
    
    # 設定新的欄位名稱
    df.columns = ['time', 'GantryID', 'Direction', 'VehicleType', 'Traffic']
    
    # 將這個 DataFrame 添加到 all_data 中
    all_data = pd.concat([all_data, df])

# 將所有的數據儲存到一個新的 CSV 檔案中
all_data.to_csv('C:/Users/User/Desktop/all_data.csv', index=False)