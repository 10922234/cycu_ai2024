import requests
from bs4 import BeautifulSoup
import os

# 定義網址
url = "https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/00/"

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
    print("Failed to retrieve data")