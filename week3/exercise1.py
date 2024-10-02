import pandas as pd

index = ['car', 'auto', 'insurance', 'best']

table1 = {
    'Doc1': [27, 3, 0, 14],
    'Doc2': [4, 33, 33, 0],
    'Doc3': [24, 0, 29, 17]
}


df_table1 = pd.DataFrame(table1, index=index)

# print(df_table1)

table2 = {
    'idf': [1.65, 2.08, 1.62, 1.5]
}

df_table2 = pd.DataFrame(table2, index=index)

# print(df_table2)
