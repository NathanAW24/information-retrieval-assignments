from collections import defaultdict
import pandas as pd

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

print(dict(incidence_matrix))

inverted_idx = defaultdict(list)
for key,val in docs.items():
    words = val. split(" ")
    # print (words)
    for word in words:
        inverted_idx[word].append(key)
    # print (inverted_idx)

for key, val in sorted(inverted_idx.items()):
    print (f"{key} -> {val}")