import pandas as pd

# 讀取CSV檔案
df = pd.read_csv('C:/Users/User/Desktop/all_data.csv')

# 將 'time' 欄位的值轉換為 datetime 對象
df['time'] = pd.to_datetime(df['time'])

# 將時間以每5分鐘劃分為一個區段
df['time'] = df['time'].dt.floor('5T')

# 將時間區段轉換為類別，並獲取每個類別的編碼
df['time'] = pd.Categorical(df['time']).codes + 1

# 將 'Direction' 欄位的值轉換為對應的標籤
df['Direction'] = df['Direction'].map({'N': '1', 'S': '2'})

# 將處理後的數據儲存到一個新的CSV檔案中
df.to_csv('C:/Users/User/Desktop/labelled_file.csv', index=False)