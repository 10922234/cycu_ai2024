import pandas as pd

# 讀取 csv 檔案
df_csv = pd.read_csv(r'C:\Users\waes3\Downloads\原始檔案\TDCS_M05A_20240228_000000_1.csv')

# 讀取 CSV 檔案
df_csv = pd.read_csv(r'C:\Users\waes3\Downloads\原始檔案\TDCS_M04A_20240228_000000_1.csv')



# 使用 merge 函數來合併'GantryFrom'和'GantryTo'的相同文字的資料
merged_df = pd.merge(df_csv, df_csv, left_on=['GantryFrom', 'GantryTo'], right_on=['GantryFrom', 'GantryTo'], how='outer')



# 將合併後的 DataFrame 儲存為新的 CSV 檔案
merged_df.to_csv(r'C:\Users\waes3\Downloads\merged.csv', index=False)