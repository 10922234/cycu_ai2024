import requests
from bs4 import BeautifulSoup
import pandas as pd

# 獲取網頁內容
response = requests.get('https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx')

# 解析網頁內容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的表格元素
tables = soup.find_all('table')

# 將 HTML 表格轉換為 DataFrame
df1 = pd.read_html(str(tables[0]))[0]
df2 = pd.read_html(str(tables[1]))[0]

# 印出 DataFrame
print(df1)
print(df2)

# 將 DataFrame 寫入 CSV 檔案
df2.to_csv("C:/Users/USER/Desktop/oil.csv", index=False)

# df2 只保留前5個欄位的資料
df2 = df2.iloc[:, :2]

# 去除值是NaN的資料
df2 = df2.dropna()
import requests
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib.font_manager import FontProperties

#https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx
# 獲取 2019年前的網頁內容
response = requests.get('https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx')
soup = BeautifulSoup(response.text, 'html.parser')
tables = soup.find_all('table')
df3 = pd.read_html(str(tables[1]))[0]

print(df3)

# 獲取網頁 2000 後的內容
response = requests.get('https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx')
# 解析網頁內容
soup = BeautifulSoup(response.text, 'html.parser')
# 找到所有的表格元素
tables = soup.find_all('table')
# 將 HTML 表格轉換為 DataFrame
df2 = pd.read_html(str(tables[1]))[0]

#將df3 與 df2 合併 變成 df2 
df2 = pd.concat([df3, df2])

# 將 DataFrame 寫入 CSV 檔案
df2.to_csv("C:/Users/USER/Desktop/oil.csv", index=False)

# df2 只保留前5個欄位的資料
df2 = df2.iloc[:, :5]

# 去除值是NaN的資料
df2 = df2.dropna()

print (df2)

# 把第一欄的資料型態 轉成 datetime
#df2[df2.columns[0]] = pd.to_datetime(df2[df2.columns[0]])

print (df2)

# 使用 matplotlib x,y 折線圖 , x 軸是日期 , 後面四個欄位是 油價 ，分別是 92無鉛汽油,95無鉛汽油,98無鉛汽油,超級柴油 
import matplotlib.pyplot as plt
# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['xtick.labelsize'] = 6
# 設定 x 軸刻度間隔
plt.xticks(rotation=100)

# 設定圖片大小
plt.figure(figsize=(10, 6))
# 繪製折線圖
plt.plot(df2[df2.columns[0]], df2[df2.columns[1]], label='92無鉛汽油')
plt.plot(df2[df2.columns[0]], df2[df2.columns[2]], label='95無鉛汽油')
plt.plot(df2[df2.columns[0]], df2[df2.columns[3]], label='98無鉛汽油')
plt.plot(df2[df2.columns[0]], df2[df2.columns[4]], label='超級柴油')


# 設定圖例
plt.legend()
# 顯示圖片
plt.show()
plt.savefig("C:/Users/USER/Desktop/oil.png")
print
# 把第一欄的資料型態 轉成 datetime
df2[df2.columns[0]] = pd.to_datetime(df2[df2.columns[0]])

print (df2)

