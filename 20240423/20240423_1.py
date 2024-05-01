import requests
from bs4 import BeautifulSoup

# 發送HTTP請求並獲取網頁內容
response = requests.get('https://tisvcloud.freeway.gov.tw/history/motc20/LiveTraffic.xml')

# 使用BeautifulSoup解析XML內容
soup = BeautifulSoup(response.content, 'lxml')

# 找到所有的標籤
tags = {tag.name for tag in soup.find_all()}

# 打印出所有的標籤
for tag in tags:
    print(tag)