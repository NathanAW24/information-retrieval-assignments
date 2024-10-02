import pandas as pd

table1 = {
    'Doc1': [27, 3, 0, 14],
    'Doc2': [4, 33, 33, 0],
    'Doc3': [24, 0, 29, 17]
}

index = ['car', 'auto', 'insurance', 'best']

df_table1 = pd.DataFrame(table1, index=index)

print(df_table1)
