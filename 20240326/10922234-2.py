import pandas as pd
import os
import glob

# 定義CSV檔案的路徑
csv_folder_path = "C:\\Users\\User\\Desktop\\csv"

# 找到資料夾中的所有CSV檔案
csv_files = glob.glob(os.path.join(csv_folder_path, "*.csv"))

# 定義欄位名稱
column_names = ['時間', '起點', '終點', '車種', '中位數時間', '交通量']

# 創建一個空的DataFrame來儲存所有的數據
df = pd.DataFrame()

# 遍歷所有的CSV檔案
for file in csv_files:
    # 讀取CSV檔案，並指定欄位名稱
    data = pd.read_csv(file, names=column_names)

    # 將讀取的數據添加到DataFrame中
    df = df.append(data, ignore_index=True)

# 定義新的CSV檔案名稱和儲存位置
new_filename = "combined.csv"
new_file_path = os.path.join(os.path.expanduser("~"), "Desktop", new_filename)

# 將DataFrame寫入到一個新的CSV檔案中
df.to_csv(new_file_path, index=False)