import pandas as pd

#讀取"C:\Users\waes3\Downloads\原始檔案\整合45.csv"檔案
df3 = pd.read_csv(r"C:\Users\waes3\Downloads\原始檔案\整合45.csv")

# 讀取"C:\Users\waes3\Downloads\7oa16-zs5py_1.xlsx"檔案
df1 = pd.read_excel(r"C:\Users\waes3\Downloads\7oa16-zs5py_1.xlsx")

# 使用 merge 函數來合併'StartETagGantryID'和'EndETagGantryID'欄位相同的資料
merged_df = pd.merge(df3, df1, left_on=['StartETagGantryID', 'EndETagGantryID'], right_on=['StartETagGantryID', 'EndETagGantryID'], how='outer')


# 將合併後的 DataFrame 儲存為新的 CSV 檔案
merged_df.to_csv(r'C:\Users\waes3\Downloads\merged3.csv', index=False)