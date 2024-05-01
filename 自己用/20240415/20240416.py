import pandas as pd

# 讀取 Excel 檔案
df = pd.read_excel(r'C:\Users\waes3\Desktop\grouped2.xlsx')

# Find rows with duplicate values in 'last name' and 'fare' columns
duplicate_rows = df[df.duplicated(subset=['last name', 'fare'], keep=False)]

# Output the duplicate rows
print(duplicate_rows)

#存檔在桌面
duplicate_rows.to_excel(r'C:\Users\waes3\Desktop\duplicate_rows.xlsx', index=False)