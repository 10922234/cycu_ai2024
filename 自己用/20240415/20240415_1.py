import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv(r'C:\Users\waes3\Downloads\titanic.csv')

#輸出資料的行數和列數
rows, cols = df.shape
print(f'The DataFrame has {rows} rows and {cols} columns.')

# 獲得 'age' 欄位的最大值和最小值
max_age = df['age'].max()
min_age = df['age'].min()

print(f'The maximum age is {max_age} and the minimum age is {min_age}.')

#去除'age'欄位中的最大值
df = df.drop(df[df['age'] == max_age].index)

#計算'age'欄位的平均值、中位數和標準差
mean_age = df['age'].mean()
median_age = df['age'].median()
std_age = df['age'].std()

print(f'The mean age is {mean_age}, the median age is {median_age}, and the standard deviation is {std_age}.')