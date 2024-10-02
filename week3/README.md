# Week 3 Assignment
## Exercise 1
With the answers done in the same directory, with `exercise1.py`, here is the most important part of the code where calculation is done.

```python
...
def tf_idf(doc: Literal['Doc1', 'Doc2', 'Doc3'], index: Literal['car', 'auto', 'insurance', 'best']) -> float:
    # function implementation
    return df_table1[doc][index] * df_table2['idf'][index]

for doc in ['Doc1', 'Doc2', 'Doc3']:
    for index in ['car', 'auto', 'insurance', 'best']:
        print(f"tf_idf({doc}, {index}) = {tf_idf(doc,index)}")
```

Here is the results for each `td_idf(doc, index)` values.
```
tf_idf("Doc1", "car") = 44.55
tf_idf("Doc1", "auto") = 6.24
tf_idf("Doc1", "insurance") = 0.0
tf_idf("Doc1", "best") = 21.0
tf_idf("Doc2", "car") = 6.6
tf_idf("Doc2", "auto") = 68.64
tf_idf("Doc2", "insurance") = 53.46
tf_idf("Doc2", "best") = 0.0
tf_idf("Doc3", "car") = 39.599999999999994
tf_idf("Doc3", "auto") = 0.0
tf_idf("Doc3", "insurance") = 46.980000000000004
tf_idf("Doc3", "best") = 25.5
```