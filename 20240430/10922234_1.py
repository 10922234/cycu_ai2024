import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import requests
import pandas as pd
from io import StringIO

# 網頁 URL
base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240429/"

# 儲存所有的 DataFrame
dfs = []

# 遍歷每個小時
for hour in range(24):
    # 遍歷每個五分鐘的時間段
    for minute in range(0, 60, 5):
        # 建立 URL
        url = f"{base_url}{str(hour).zfill(2)}/TDCS_M03A_20240429_{str(hour).zfill(2)}{str(minute).zfill(2)}00.csv"
        
        # 嘗試下載 CSV 檔案
        try:
            response = requests.get(url, verify=False)
            df = pd.read_csv(StringIO(response.text), usecols=[0, 1, 2, 3, 4, 5], 
                             names=['time', 'GantryID', 'Direction', 'VehicleType', 'Traffic'], 
                             index_col=0, parse_dates=True)
            dfs.append(df)
        except Exception as e:
            print(f"Failed to download {url}: {e}")

# 合併所有的 DataFrame
dfs = pd.concat(dfs,axis=0)

# 依照索引排序
dfs.sort_index(inplace=True)

# 輸出為一個新的 CSV 檔案
dfs.to_csv("C:\\Users\\User\\Desktop\\csv\\output1.csv")