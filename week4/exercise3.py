from typing import List, Dict
from collections import defaultdict
import math

def tf_(doc: List[str]):
    frequencies = defaultdict(int)
    for letter in doc:
        frequencies[letter] += 1

    return dict(frequencies)

input = ['a','b','b','c','d']
print(f"tf_({input}) = {tf_(input)}")

def df_(docs: List[List[str]]):
    df = defaultdict(int)

    for doc in docs:
        for letter in doc:
            df[letter] += 1

    return dict(df)

input = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
print(f"df_({input}) = {df_(input)}")


def idf_(df, corpus_size):
    idf = {}
    for term, freq in df.items():
        idf[term] = round(math.log((corpus_size) / (freq)),2)
    return idf

print(f"idf_({df_(input)}) = {idf_(df_(input), len(input))}")


def _score(query, doc, docs, k1=1.5, b=0.75):
    score = 0.0
    tf = tf_(doc)
    df = df_(docs)
    idf = idf_(df, len(docs))
    avg_doc_len = sum(len(doc) for doc in docs)/len(docs) # calculate average document length
    for term in query:
        if term not in tf.keys():
            continue

        numerator = (k1+1) * tf[term]
        denominator = k1 * ( (1-b) + b*len(doc)/avg_doc_len ) + tf[term]

        score += idf[term] * numerator/denominator
    return score


query = ['b', 'c', 'e']
doc = ['b', 'c', 'd']
docs = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]
print(f"_score({query}, {doc},\n{docs}) = {_score(query, doc, docs)}")