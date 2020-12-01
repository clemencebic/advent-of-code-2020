
import pandas as pd

f = open('input.txt', 'r')
input = f.read().split('\n')[:-1]

df = pd.DataFrame({'num' : input, 'id': [1]*len(input)})
df['num'] = df['num'].astype('int')

# For two numbers
merged = df.merge(df, how = 'left', on='id')
merged['s'] = merged.num_x + merged.num_y
merged['m'] = merged.num_x * merged.num_y
merged[merged.s == 2020]

# For three numbers
merged = merged.merge(df, how='left', on='id')
merged['s'] = merged.num_x + merged.num_y + merged.num
merged['m'] = merged.num_x * merged.num_y * merged.num
merged[merged.s == 2020]
