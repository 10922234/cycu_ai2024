import pandas as pd

# 讀取 Excel 檔案
df_excel = pd.read_excel(r'C:\Users\waes3\Downloads\7oa16-zs5py.xlsx')

# 讀取 CSV 檔案
df_csv = pd.read_csv(r'C:\Users\waes3\Downloads\TDCS_M05A_20240228_000000.csv')



# 使用 merge 函數來合併有相同文字的資料
merged_df = pd.merge(df_csv, df_excel, left_on=['EndETagGantryID', 'StartETagGantryID'], right_on=['EndETagGantryID', 'StartETagGantryID'], how='inner')



# 將合併後的 DataFrame 儲存為新的 CSV 檔案
merged_df.to_csv(r'C:\Users\waes3\Downloads\merged.csv', index=False)