# Exercise 2
Code is in `exercise2.py`.

To find `pt`, this is the function
```python
def pt(letter_target, relevant_docs):
    # <number-of-term-exist-in-relevant-docs> / <total-relevant-docs>
    count_exist = 0 # s
    relevant_doc_size = 0 # S

    for letters in relevant_docs.values():
        if letter_target in letters:
            count_exist += 1
        relevant_doc_size += 1

    return count_exist / relevant_doc_size

for letter_target in ['x', 'y', 'z', 'w', 'v', 'k', 'm']:
    print(f"pt({letter_target}, ...) = {pt(letter_target, relevant_docs)}")
```

Here's the result
```bash
pt(x, ...) = 1.0
pt(y, ...) = 1.0
pt(z, ...) = 0.5
pt(w, ...) = 0.5
pt(v, ...) = 0.5
pt(k, ...) = 0.5
pt(m, ...) = 0.0
```

TP find `ut`, this is the function
```python
def ut(letter_target, N, relevant_docs, word_frequency):
    # <number-of-term-exist-in-non-relevant-docs> / (N - <total-relevant-docs>)
    count_exist = 0
    relevant_doc_size = 0

    for letters in relevant_docs.values():
        if letter_target in letters:
            count_exist += 1
        relevant_doc_size += 1

    return (word_frequency[letter_target] - count_exist) / (N - relevant_doc_size)        

for letter_target in ['x', 'y', 'z', 'w', 'v', 'k', 'm']:
    print(f"ut({letter_target}, ...) = {ut(letter_target, N, relevant_docs, word_frequency)}")
```

This is the result
```bash
ut(x, ...) = 0.4642857142857143
ut(y, ...) = 0.35714285714285715
ut(z, ...) = 0.4642857142857143
ut(w, ...) = 0.5357142857142857
ut(v, ...) = 0.6071428571428571
ut(k, ...) = 0.32142857142857145
ut(m, ...) = 0.2857142857142857
```

To find `ct` this is the function
```python
def ct(letter_target, N, relevant_docs, word_frequency, smoothing=0.5):
    count_exist = 0 # s
    relevant_doc_size = 0 # S

    for letters in relevant_docs.values():
        if letter_target in letters:
            count_exist += 1
        relevant_doc_size += 1
    
    numerator = (count_exist+smoothing) / (relevant_doc_size-count_exist+smoothing)
    denominator = (word_frequency[letter_target]-count_exist+smoothing) / (N-word_frequency[letter_target]-relevant_doc_size+count_exist+smoothing)

    return numerator/denominator


ct_scores = defaultdict(int)
for letter_target in ['x', 'y', 'z', 'w', 'v', 'k', 'm']:
    print(f"ct({letter_target}, ...) = {ct(letter_target, N, relevant_docs, word_frequency)}")
    ct_scores[letter_target] = ct(letter_target, N, relevant_docs, word_frequency)
```

This is the result.
```bash
ct(x, ...) = 0.7589679340113041
ct(y, ...) = 0.9449524336690945
ct(z, ...) = 0.05999792967528537
ct(w, ...) = -0.05999792967528537
ct(v, ...) = -0.18234020833268275
ct(k, ...) = 0.3123110060736703
ct(m, ...) = -0.3166350689945572
```

For `rsv` for each `additional_docs`.
```python
def rsv(query, doc_values, ct_scores):
    score = 0
    for letter in query:
        if letter in doc_values:
            score += ct_scores[letter]

    return score

query = "mvykw"
for doc, doc_values in additional_docs.items():
    print(f"rsv({query}, {doc}, ...) = {rsv(query, doc_values, ct_scores)}")
```

This is the result.
```bash
rsv(mvykw, D6, ...) = 0.2523130763983849
rsv(mvykw, D7, ...) = 0.7626122253364118
rsv(mvykw, D8, ...) = 0.44597715634185464
```