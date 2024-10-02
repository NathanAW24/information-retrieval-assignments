def jaccard_similarity(doc1: str, doc2: str) -> float:
    # Tokenize the documents into sets of words
    set1 = set(doc1.split())
    set2 = set(doc2.split())
    
    # Compute the intersection and union of the sets
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    
    # Calculate the Jaccard similarity
    return len(intersection) / len(union)

# Example usage
doc1 = "we love information retrieval course"
doc2 = "information retrieval is a course offered in sutd"

similarity = jaccard_similarity(doc1, doc2)
print(f"Jaccard Similarity: {similarity}")