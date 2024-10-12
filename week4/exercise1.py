import math
import pandas as pd
from collections import defaultdict

# Define the documents
docs = {
    "D1": "wxyyz",
    "D2": "kxvyy",
    "D3": "mwyz",
    "D4": "vwy",
    "D5": "vmxy"
}

# Function to convert documents into a term-document matrix
def create_term_document_matrix(docs):
    # Split each document into a set of unique terms
    term_document_count = defaultdict(set)
    for doc_id, content in docs.items():
        for term in set(content):  # Use set to count each term only once per document
            term_document_count[term].add(doc_id)
    
    # Create a DataFrame for easy manipulation
    terms = list(term_document_count.keys())
    doc_ids = list(docs.keys())
    data = {term: [1 if doc_id in term_document_count[term] else 0 for doc_id in doc_ids] for term in terms}
    return pd.DataFrame(data, index=doc_ids)

# Function to calculate IDF values for each term
def calculate_idf(term_document_matrix, smoothing_numerator=0.5, smoothing_denominator=0.5):
    N = len(term_document_matrix)  # Total number of documents
    idf_scores = {}
    for term in term_document_matrix.columns:
        df = term_document_matrix[term].sum()  # Document frequency of the term
        idf_scores[term] = math.log10((N + smoothing_numerator) / (df + smoothing_denominator))
    return pd.Series(idf_scores, name="IDF")

# Create the term-document matrix and calculate IDF scores
term_document_matrix = create_term_document_matrix(docs)
idf_scores = calculate_idf(term_document_matrix)

print("Term document matrix:\n", term_document_matrix)
print("IDF scores:\n", idf_scores)

# Function to calculate c_t for each term
def calculate_ct(term_document_matrix, smoothing_numerator=0.5, smoothing_denominator=0.5):
    N = len(term_document_matrix)  # Total number of documents
    ct_scores = {}
    for term in term_document_matrix.columns:
        df = term_document_matrix[term].sum()  # Document frequency of the term
        ct_scores[term] = math.log10((N - df + smoothing_numerator) / (df + smoothing_denominator))
    return pd.Series(ct_scores, name="c_t")

# Function to calculate RSV for a given query
def calculate_rsv(query_terms, term_document_matrix, ct_scores):
    rsv_scores = {}
    for doc_id in term_document_matrix.index:
        rsv = sum(ct_scores[term] for term in query_terms if term_document_matrix.at[doc_id, term] == 1)
        rsv_scores[doc_id] = rsv
    return pd.Series(rsv_scores, name="RSV").sort_values(ascending=False)

# Define the query
query_terms = ["m", "v", "y", "k", "w"]

# Calculate c_t scores
ct_scores = calculate_ct(term_document_matrix)

# Calculate RSV for each document based on the query
rsv_scores = calculate_rsv(query_terms, term_document_matrix, ct_scores)

# Display the ordered RSV scores for the documents
print("ct scores:\n", ct_scores)
print("RSV scores (High to Low):\n", rsv_scores)
