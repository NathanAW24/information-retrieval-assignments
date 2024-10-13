from collections import defaultdict
import math

relevant_docs = {
    "D1": "wxyyz",
    "D2": "kxvyy"
}

non_relevant_docs = {
    "D3": "mwyz",
    "D4": "vwy",
    "D5": "vmxy"
}

additional_docs = {
    "D6": "wxxk",
    "D7": "vzy",
    "D8": "mvy"
}


word_frequency = { # df_t
    "x": 15,
    "y": 12,
    "z": 14,
    "w": 16,
    "v": 18,
    "k": 10,
    "m": 8
}

N = 30

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

def ct(letter_target, N, relevant_docs, word_frequency, smoothing=0.5):
    count_exist = 0 # s
    relevant_doc_size = 0 # S

    for letters in relevant_docs.values():
        if letter_target in letters:
            count_exist += 1
        relevant_doc_size += 1
    
    numerator = (count_exist+smoothing) / (relevant_doc_size-count_exist+smoothing)
    denominator = (word_frequency[letter_target]-count_exist+smoothing) / (N-word_frequency[letter_target]-relevant_doc_size+count_exist+smoothing)

    return math.log10(numerator/denominator)


ct_scores = defaultdict(int)
for letter_target in ['x', 'y', 'z', 'w', 'v', 'k', 'm']:
    print(f"ct({letter_target}, ...) = {ct(letter_target, N, relevant_docs, word_frequency)}")
    ct_scores[letter_target] = ct(letter_target, N, relevant_docs, word_frequency)


def rsv(query, doc_values, ct_scores):
    score = 0
    for letter in query:
        if letter in doc_values:
            score += ct_scores[letter]

    return score

query = "mvykw"
for doc, doc_values in additional_docs.items():
    print(f"rsv({query}, {doc}, ...) = {rsv(query, doc_values, ct_scores)}")