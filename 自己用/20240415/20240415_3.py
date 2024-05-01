import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv(r'C:\Users\waes3\Downloads\titanic.csv')

# 選擇 'job' 欄位為 'Businessman' 的所有資料
businessman_df = df.loc[df['job'] == 'Businessman']

# 去除 'age' 欄位為 9999 的所有資料
businessman_df = businessman_df[businessman_df['age'] != 9999]

# 計算 'age' 欄位的中位數、平均值和標準差
median_age = businessman_df['age'].median()
mean_age = businessman_df['age'].mean()
std_age = businessman_df['age'].std()

print('Businessman:')

print(f'The median age is {median_age}, the mean age is {mean_age}, and the standard deviation of age is {std_age}.')

#輸出分隔線
print('-' * 50)

# 選擇 'job' 欄位為 'Trimmer' 的所有資料
trimmer_df = df.loc[df['job'] == 'Trimmer']

# 去除 'age' 欄位為 9999 的所有資料
trimmer_df = trimmer_df[trimmer_df['age'] != 9999]

# 計算 'age' 欄位的中位數、平均值和標準差
median_age = trimmer_df['age'].median()
mean_age = trimmer_df['age'].mean()
std_age = trimmer_df['age'].std()

print('Trimmer:')

print(f'The median age is {median_age}, the mean age is {mean_age}, and the standard deviation of age is {std_age}.')

#輸出分隔線
print('-' * 50)

# 選擇 'job' 欄位為 'Steward' 的所有資料
steward_df = df.loc[df['job'] == 'Steward']

# 去除 'age' 欄位為 9999 的所有資料
steward_df = steward_df[steward_df['age'] != 9999]

# 計算 'age' 欄位的中位數、平均值和標準差
median_age = steward_df['age'].median()
mean_age = steward_df['age'].mean()
std_age = steward_df['age'].std()

print('Steward:')

print(f'The median age is {median_age}, the mean age is {mean_age}, and the standard deviation of age is {std_age}.')

#輸出分隔線
print('-' * 50)

# 選擇 'job' 欄位為 'Waiter' 的所有資料
waiter_df = df.loc[df['job'] == 'Waiter']

# 去除 'age' 欄位為 9999 的所有資料
waiter_df = waiter_df[waiter_df['age'] != 9999]

# 計算 'age' 欄位的中位數、平均值和標準差
median_age = waiter_df['age'].median()
mean_age = waiter_df['age'].mean()
std_age = waiter_df['age'].std()

print('Waiter:')
print(f'The median age is {median_age}, the mean age is {mean_age}, and the standard deviation of age is {std_age}.')

#輸出分隔線
print('-' * 50)

# 選擇 'job' 欄位為 'General Labourer' 的所有資料
general_labourer_df = df.loc[df['job'] == 'General Labourer']

# 去除 'age' 欄位為 9999 的所有資料
general_labourer_df = general_labourer_df[general_labourer_df['age'] != 9999]

# 計算 'age' 欄位的中位數、平均值和標準差
median_age = general_labourer_df['age'].median()
mean_age = general_labourer_df['age'].mean()
std_age = general_labourer_df['age'].std()

print('General Labourer:')
print(f'The median age is {median_age}, the mean age is {mean_age}, and the standard deviation of age is {std_age}.')

