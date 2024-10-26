import numpy as np

def precision_at_k(r, k):
    """Score is precision @ k (This we solve for you!)
    Relevance is binary (nonzero is relevant).
    >>> r = [0, 0, 1]
    >>> precision_at_k(r, 1)
    0.0
    >>> precision_at_k(r, 2)
    0.0
    >>> precision_at_k(r, 3)
    0.33333333333333331
    >>> precision_at_k(r, 4)
    Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    ValueError: Relevance score length < k
    Args:
    r: Relevance scores (list or numpy) in rank order
    (first element is the first item)
    Returns:
    Precision @ k
    Raises:
    ValueError: len(r) must be >= k
    """
    assert k >= 1
    r = np.asarray(r)[:k] != 0
    if r.size != k:
        raise ValueError('Relevance score length < k')
    return np.mean(r)

def average_precision(r):
    """Score is average precision (area under PR curve)
    Relevance is binary (nonzero is relevant).
    >>> r = [1, 1, 0, 1, 0, 1, 0, 0, 0, 1]
    >>> delta_r = 1. / sum(r)
    >>> sum([sum(r[:x + 1]) / (x + 1.) * delta_r for x, y in
    enumerate(r) if y])
    0.7833333333333333
    >>> average_precision(r)
    0.78333333333333333
    Args:
    r: Relevance scores (list or numpy) in rank order
    (first element is the first item)
    Returns:
    Average precision
    """
    #write your code here
    r = np.asarray(r)
    precisions = [precision_at_k(r, k + 1) for k in range(len(r)) if r[k]]
    if not precisions:
        return 0.0
    return np.mean(precisions)

def mean_average_precision(rs):
    """Score is mean average precision
    Relevance is binary (nonzero is relevant).
    >>> rs = [[1, 1, 0, 1, 0, 1, 0, 0, 0, 1]]
    >>> mean_average_precision(rs)
    0.78333333333333333
    >>> rs = [[1, 1, 0, 1, 0, 1, 0, 0, 0, 1], [0]]
    >>> mean_average_precision(rs)
    0.39166666666666666
    Args:
    rs: Iterator of relevance scores (list or numpy) in rank order
    (first element is the first item)
    Returns:
    Mean average precision
    """
    #write your code here
    return np.mean([average_precision(r) for r in rs])


def dcg_at_k(r, k, method=0):
    """Score is discounted cumulative gain (dcg)
    Relevance is positive real values.  Can use binary
    as the previous methods.
    >>> dcg_at_k([3, 2, 3, 0, 1, 2], 1)
    3.0
    >>> dcg_at_k([3, 2, 3, 0, 1, 2], 2)
    5.0
    >>> dcg_at_k([3, 2, 3, 0, 1, 2], 6)
    9.6051177391888114
    >>> dcg_at_k([3, 2, 3, 0, 1, 2], 6, method=1)
    8.7407469159740733
    Args:
    r: Relevance scores (list or numpy) in rank order
    (first element is the first item)
    k: Number of results to consider
    method: If 0 then weights are [1.0, 1.0, 0.6309, 0.5, 0.4307,
    ...]
    If 1 then weights are [1.0, 0.6309, 0.5, 0.4307, ...]
    Returns:
    Discounted cumulative gain
    """
    r = np.asfarray(r)[:k]
    if r.size:
        if method == 0:
            return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 2)))
        elif method == 1:
            return np.sum(r / np.log2(np.arange(2, r.size + 2)))
    return 0.

def ndcg_at_k(r, k, method=0):
    """Score is normalized discounted cumulative gain (ndcg)
    Relevance is positive real values. Can use binary
    as the previous methods.
    Example from
    http://www.stanford.edu/class/cs276/handouts/EvaluationNew-handout-6-per
    .pdf
    >>> r = [3, 2, 3, 0, 0, 1, 2, 2, 3, 0]
    >>> ndcg_at_k(r, 1)
    1.0
    >>> r = [2, 1, 2, 0]
    >>> ndcg_at_k(r, 4)
    0.9203032077642922
    >>> ndcg_at_k(r, 4, method=1)
    0.96519546960144276
    >>> ndcg_at_k([0], 1)
    0.0
    >>> ndcg_at_k([1], 2)
    1.0
    Args:
    r: Relevance scores (list or numpy) in rank order
    (first element is the first item)
    k: Number of results to consider
    method: If 0 then weights are [1.0, 1.0, 0.6309, 0.5, 0.4307,
    ...]
    If 1 then weights are [1.0, 0.6309, 0.5, 0.4307, ...]
    Returns:
    Normalized discounted cumulative gain
    """
    #write your code here (return appropriate value)
    return 0.

if __name__ == "__main__":
    print(precision_at_k([0, 0, 1],1))
    print(precision_at_k([0, 0, 1],2))
    print(precision_at_k([0, 0, 1],3))
    # print(precision_at_k([0, 0, 1],4))


    print(average_precision([1, 1, 0, 1, 0, 1, 0, 0, 0, 1]))
    print(average_precision([0,1,0,0,1,0,1,0,0,0]))
    print(average_precision([1,0,1,0,0,1,0,0,1,1]))
    print(mean_average_precision([[1,0,1,0,0,1,0,0,1,1],[0,1,0,0,1,0,1,0,0,0]]))
    print(dcg_at_k([1.0,0.6,0.0,0.8,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.2,0.0],3))
    print(ndcg_at_k([1.0,0.6,0.0,0.8,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.2,0.0],3))