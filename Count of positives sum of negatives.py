def count_positives_sum_negatives(arr):
    if not arr:
        return []
    neg, pos = [], []
    [neg.append(i) if i<0 else pos.append(i) for i in arr if i]
    return [len(pos), sum(neg)]
