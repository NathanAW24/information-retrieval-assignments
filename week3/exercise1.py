from typing import Literal
import pandas as pd

indices = ['car', 'auto', 'insurance', 'best']

table1 = {
    'Doc1': [27, 3, 0, 14],
    'Doc2': [4, 33, 33, 0],
    'Doc3': [24, 0, 29, 17]
}


df_table1 = pd.DataFrame(table1, index=indices)

# print(df_table1)

table2 = {
    'idf': [1.65, 2.08, 1.62, 1.5]
}

df_table2 = pd.DataFrame(table2, index=indices)

# print(df_table2)

def tf_idf(doc: Literal['Doc1', 'Doc2', 'Doc3'], index: Literal['car', 'auto', 'insurance', 'best']) -> float:
    # function implementation
    return ( df_table1[doc][index] / (df_table1[doc].sum()) ) * df_table2['idf'][index]

for doc in ['Doc1', 'Doc2', 'Doc3']:
    for index in ['car', 'auto', 'insurance', 'best']:
        print(f"tf_idf({doc}, {index}) = {tf_idf(doc,index)}")
