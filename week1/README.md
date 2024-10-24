# Question 0
## 0.1

Query processing order:
- `tangerine OR trees` &rarr; `46653 + 316812 = 363465`
- `marmalade OR skies` &rarr; `107913 + 271658 = 379571`
- `kaleidoscope OR eyes` &rarr; `87009 + 2113312 = 300321`

We begin with the smallest value:
`(kaleidoscope OR eyes) AND (tangerine OR trees) AND (marmalade OR skies)`

## 0.2
We should process `kaleidoscope OR eyes` first since it has the smallest worst case after `OR` operation.

# Question 1
## 1.1

Code to make the matrix.

```python
...
docs = {
    1: "breakthrough drug for schizophrenia",
    2: "new schizophrenia drug",
    3: "new approach for treatment of schizophrenia",
    4: "new hopes for schizophrenia patients"
}

incidence_matrix = defaultdict(lambda: [0,0,0,0])

for doc, content in docs.items():
    for word in content.split():
        # doc is 1-indexed
        incidence_matrix[word][doc-1] = 1
...
```


Incidence matrix looks like this.

```bash
{'breakthrough': [1, 0, 0, 0], 'drug': [1, 1, 0, 0], 'for': [1, 0, 1, 1], 'schizophrenia': [1, 1, 1, 1], 'new': [0, 1, 1, 1], 'approach': [0, 0, 1, 0], 'treatment': [0, 0, 1, 0], 'of': [0, 0, 1, 0], 'hopes': [0, 0, 0, 1], 'patients': [0, 0, 0, 1]}
```

## 1.2 (a)

Based on the query `schizophrenia AND drug` &rarr; `Doc1 and Doc2` has the answer

## 1.2 (b)

Based on the query `for AND NOT(drug OR approach)` &rarr; `[1 0 1 1] AND NOT[1 1 1 0]` &rarr; `[0 0 0 1]` &rarr; which means its `Doc4`

## 1.3
```python
...
inverted_idx = defaultdict(list)
for key,val in docs.items():
    words = val. split(" ")
    # print (words)
    for word in words:
        inverted_idx[word].append(key)
    # print (inverted_idx)

for key, val in sorted(inverted_idx.items()):
    print (f"{key} -> {val}")
...
```

```bash
approach -> [3]
breakthrough -> [1]
drug -> [1, 2]
for -> [1, 3, 4]
hopes -> [4]
new -> [2, 3, 4]
of -> [3]
patients -> [4]
schizophrenia -> [1, 2, 3, 4]
treatment -> [3]
```