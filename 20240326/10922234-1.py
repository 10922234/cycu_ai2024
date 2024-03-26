
import requests
from bs4 import BeautifulSoup
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

        # 取得所有csv檔案的路徑
        csv_files = glob.glob(os.path.join(desktop_path, "*.csv"))

        # 定義合併後的檔案路徑
        merged_file_path = os.path.join(desktop_path, "merged.csv")

        # 開啟合併後的檔案
        with open(merged_file_path, "w") as merged_file:
            # 遍歷所有csv檔案
            for csv_file in csv_files:
                # 開啟csv檔案
                with open(csv_file, "r") as file:
                    # 讀取csv檔案內容
                    csv_content = file.read()
                    # 將csv內容寫入合併後的檔案
                    merged_file.write(csv_content)