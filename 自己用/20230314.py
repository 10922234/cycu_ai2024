import requests
from bs4 import BeautifulSoup
import pandas as pd

# 網址
url = 'https://tisvcloud.freeway.gov.tw/history/motc20/ETagPair.xml'

# 發送 GET 請求
response = requests.get(url)

# 解析 XML
soup = BeautifulSoup(response.content, 'lxml')

# 找到所有的 record 標籤
records = soup.find_all('record')

# 將每個 record 的資料轉換成字典，並加入到 list 中
data = []
for record in records:
    record_dict = {}
    for tag in record.find_all():
        record_dict[tag.name] = tag.text
    data.append(record_dict)

# 將 list 轉換成 DataFrame
df = pd.DataFrame(data)

# 印出 DataFrame
print(df)