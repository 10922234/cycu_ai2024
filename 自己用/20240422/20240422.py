import pandas as pd

# 讀取 Excel 檔案，並跳過第一行
df = pd.read_excel(r'C:\Users\waes3\Downloads\地震活動彙整_638494162915897482.xlsx', skiprows=1)

# 修改欄位名稱
df.columns = ['編號', '地震時間', '經度', '緯度', '規模', '深度', '相對位置']

# 將 DataFrame 儲存為新的 Excel 檔案
df.to_excel(r'C:\Users\waes3\Desktop\地震活動彙整.xlsx', index=False)

import folium
import folium.plugins as plugins
import pandas as pd

# 讀取 Excel 檔案
df = pd.read_excel(r'C:\Users\waes3\Desktop\地震活動彙整.xlsx')

# 建立一個台灣地圖
m = folium.Map(location=[23.5, 121], zoom_start=7)

# 將 DataFrame 轉換為 GeoJSON 格式
features = df.apply(
    lambda row: {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [row['經度'], row['緯度']]
        },
        "properties": {
            "time": row['地震時間'].date().__str__(),
            "style": {"color" : "red"},
            "icon": "circle",
            "iconstyle": {
                "fillColor": "red",
                "fillOpacity": 0.6,
                "stroke": "false",
                "radius": 10
            },
            "popup": f"""
            編號：{row['編號']}<br>
            地震時間：{row['地震時間']}<br>
            北緯：{row['緯度']}<br>
            東經：{row['經度']}<br>
            規模：{row['規模']}<br>
            深度：{row['深度']}<br>
            相對位置：{row['相對位置']}
            """
        }
    }, axis=1).tolist()

import folium.plugins as plugins

# 將 '地震時間' 欄位轉換為 datetime 格式，並排序
df['地震時間'] = pd.to_datetime(df['地震時間'])
df = df.sort_values('地震時間')

# 建立一個台灣地圖
m = folium.Map(location=[23.5, 121], zoom_start=7)

# 建立一個時間序列的動態地圖
features = []
for index, row in df.iterrows():
    features.append(
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [row['經度'], row['緯度']]
            },
            'properties': {
                'time': row['地震時間'].date().__str__(),
                'style': {'color' : 'red'},
                'icon': 'circle',
                'iconstyle':{
                    'fillColor': 'red',
                    'fillOpacity': 0.6,
                    'stroke': 'false',
                    'radius': 5
                },
                'popup': f"""
                編號：{row['編號']}<br>
                地震時間：{row['地震時間']}<br>
                北緯：{row['緯度']}<br>
                東經：{row['經度']}<br>
                規模：{row['規模']}<br>
                深度：{row['深度']}<br>
                相對位置：{row['相對位置']}
                """
            }
        }
    )

plugins.TimestampedGeoJson(
    {'type': 'FeatureCollection', 'features': features},
    period='P1D',
    add_last_point=True,
    auto_play=False,
    loop=False,
    max_speed=0.2,  # 修改此處
    loop_button=True,
    date_options='YYYY/MM/DD',
    time_slider_drag_update=True
).add_to(m)

# 儲存地圖到桌面
m.save(r'C:\Users\waes3\Desktop\台灣地震活動地圖.html')