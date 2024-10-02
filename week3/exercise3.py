from typing import List
import math

vectors = {
    'a' : [0.5, 1.5],
    'b' : [4, 4],
    'c' : [8, 6]
}
x = [2, 2]

# Cosine similarity
def cosine_similarity(vector1: List[float], vector2: List[float]) -> float:
    dot_product = sum(a * b for a, b in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(a * a for a in vector1))
    magnitude2 = math.sqrt(sum(b * b for b in vector2))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0
    return dot_product / (magnitude1 * magnitude2)

# Euclidean distance
def euclidean_distance(vector1: List[float], vector2: List[float]) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(vector1, vector2)))

for vector_key in vectors.keys():
    print(f"cosine_similarity(x, {vector_key}) = {cosine_similarity(x, vectors[vector_key])}")
    print(f"euclidean_distance(x, {vector_key}) = {euclidean_distance(x, vectors[vector_key])}")