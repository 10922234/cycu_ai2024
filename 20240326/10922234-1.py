
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
import os
import glob

# 定義基本網址
base_url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/"

# 遍歷所有的小時數
for hour in range(24):
    # 生成對應的網址
    url = base_url + str(hour).zfill(2) + "/"

    # 獲取網頁內容
    response = requests.get(url)

    # 檢查請求是否成功
    if response.status_code == 200:
        # 使用BeautifulSoup來解析獲取的網頁內容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 找到所有的CSV檔案連結
        links = soup.find_all('a')

        for link in links:
            if '.csv' in link.get('href'):
                csv_url = url + link.get('href')

                # 下載CSV檔案
                csv_response = requests.get(csv_url)

                if csv_response.status_code == 200:
                    # 定義檔案名稱和儲存位置
                    filename = link.get('href')
                    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "csv")
                    file_path = os.path.join(desktop_path, filename)

                    # 將內容寫入到一個CSV檔案中
                    with open(file_path, "w") as file:
                        file.write(csv_response.text)
    else:
        print("Failed to retrieve data from", url)



# 定義CSV檔案的路徑
csv_folder_path = "C:\\Users\\User\\Desktop\\csv"

# 找到資料夾中的所有CSV檔案
csv_files = glob.glob(os.path.join(csv_folder_path, "*.csv"))

# 創建一個空的DataFrame來儲存所有的數據
df = pd.DataFrame()

# 遍歷所有的CSV檔案
for file in csv_files:
    # 讀取CSV檔案
    data = pd.read_csv(file)

    # 將讀取的數據添加到DataFrame中
    df = df.append(data, ignore_index=True)

# 定義新的CSV檔案名稱和儲存位置
new_filename = "combined.csv"
new_file_path = os.path.join(os.path.expanduser("~"), "Desktop", new_filename)

# 將DataFrame寫入到一個新的CSV檔案中
df.to_csv(new_file_path, index=False)