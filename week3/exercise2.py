from typing import Literal
import pandas as pd
from math import log2

co_occurence_matrix = {
    'c1': [2, 3],
    'c2': [4, 1],
    'c3': [3, 7]
}

index = ['w1', 'w2']

df_co_occurence_matrix = pd.DataFrame(co_occurence_matrix, index=index)

# print(df_co_occurence_matrix)

def ppmi(w: Literal["w1","w2"], c: Literal["c1","c2","c3"]):
    total_sum = df_co_occurence_matrix.values.sum()
    prob_w_c = df_co_occurence_matrix[c][w] / total_sum
    prob_w = df_co_occurence_matrix.loc[w].sum() / total_sum
    prob_c = df_co_occurence_matrix[c].sum() / total_sum
    
    pmi = log2(prob_w_c / (prob_c * prob_w))
    return max(pmi, 0)

for w in ["w1", "w2"]:
    for c in ["c1", "c2", "c3"]:
        print(f"ppmi({w}, {c}) = {ppmi(w, c)}")