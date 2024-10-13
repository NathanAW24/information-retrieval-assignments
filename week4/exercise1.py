# Define the documents
from collections import defaultdict
import math


docs = {
    "D1": "wxyyz",
    "D2": "kxvyy",
    "D3": "mwyz",
    "D4": "vwy",
    "D5": "vmxy"
}

def df(letters, docs):
    _df = defaultdict(int)
    
    # populate dft
    for letter_target in letters:
        for doc_values in docs.values():
            if letter_target in doc_values:
                _df[letter_target] += 1

    return dict(_df)


def idf(letters, docs, smoothing=0):
    N = len(docs)

    _df = df(letters, docs)

    # calculate idf
    _idf = defaultdict(int)
    for letter_target in letters:
        _idf[letter_target] = math.log10((N + smoothing) / (_df[letter_target] + smoothing))

    return dict(_idf)

# with smoothing
for smoothing in [0, 0.5]:
    print(f"IDF score, With smoothing = {smoothing} \n idf={idf(['x', 'y', 'z', 'w', 'v', 'k', 'm'], docs, smoothing)}")

def c(letters, docs, smoothing=0):
    N = len(docs)

    _df = df(letters, docs)

    _c = defaultdict(int)
    for letter_target in letters:
        _c[letter_target] = math.log10( (N - _df[letter_target] + smoothing) / (_df[letter_target] + smoothing) )

    return dict(_c)

_c = c(['x', 'y', 'z', 'w', 'v', 'k', 'm'], docs, smoothing)

for smoothing in [0.5]:
    print(f"C Score, With smoothing = {smoothing} \n C={_c}")

def rsv(c, query, docs):
    _rsv = defaultdict(int)

    for letter in query:
        for doc, doc_values in docs.items():
            if letter in doc_values:
                _rsv[doc] += c.get(letter, 0)

    return dict(_rsv)


query = "mvykw"
_rsv = rsv(_c, query, docs)
print(f"RSV with given c = {_rsv}")

print(f"Sorting Based on RSV (descending), {sorted(_rsv, key = _rsv.get, reverse=True)}")