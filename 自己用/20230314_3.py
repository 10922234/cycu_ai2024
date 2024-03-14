import pandas as pd

# 讀取 csv 檔案
df_csv = pd.read_csv(r'C:\Users\waes3\Downloads\原始檔案\TDCS_M05A_20240228_000000_1.csv')

# 讀取 CSV 檔案
df_csv = pd.read_csv(r'C:\Users\waes3\Downloads\原始檔案\TDCS_M04A_20240228_000000_1.csv')


#擷取欄位'TravelTime'的資料，顯示前5筆
print(df_csv['TravelTime'].head())