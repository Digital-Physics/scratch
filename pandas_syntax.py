import pandas as pd

df = pd.DataFrame({"col_one": [1,2,3], "col_two": [4,5,6], "col_three": [7,8,9], "col_four": [10,11,12]})

print(df.iloc[1, 3])
print(df.iloc[1].loc['col_four'])
print(df.loc[1, 'col_four'])
print(df.loc[df.index[1], 'col_four'])
print(df.at[1, 'col_four'])
print(df.iat[1, 3])
print(df.xs(1).loc['col_four'])
print(df.query("index == 1")['col_four'].iloc[0])
print(df[df.index == 1]['col_four'].values[0])