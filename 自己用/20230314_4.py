import pandas as pd

# 讀取 CSV 檔案
df1 = pd.read_csv(r'C:\Users\waes3\Downloads\原始檔案\TDCS_M05A_20240228_000000_1.csv')
df2 = pd.read_csv(r'C:\Users\waes3\Downloads\原始檔案\TDCS_M04A_20240228_000000_1.csv')

# 將 df2 中的 'TravelTime' 欄位加入到 df1 中
df1['TravelTime'] = df2['TravelTime']

# 將合併後的 DataFrame 儲存為新的 CSV 檔案
df1.to_csv(r'C:\Users\waes3\Downloads\原始檔案\merged.csv', index=False)


