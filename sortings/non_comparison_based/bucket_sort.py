from typing import List


def bucketSort(arr) -> List:
    n = len(arr)
    if n <= 1:
        return arr

    # Step 1: Find the min and max
    min_val = min(arr)
    max_val = max(arr)

    # If all the elements are same, already sorted and this is edge case also
    if max_val == min_val:
        return arr

    # Step 2: Create n empty buckets
    buckets = [[] for _ in range(n)]

    # Step 3: Normalize and distribute elements into buckets
    range_val = max_val - min_val
    for num in arr:
        normalized = (num - min_val) / range_val
        index = int(normalized * n)
        if index == n:
            index -= 1

        buckets[index].append(num)

    # Step 4: Sort each bucket and merge
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))

    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 5, 5, 1, 3, 4, 1, 1]
    print(bucketSort(arr))

# Time complexity:- Avg Case O(N), suppose the each bucket contains only one element means uniformly distributed
# then sorting only one element is O(1) (Fast if data is uniform)
# Time complexity:- Worst Case O(N logN)
# Works for integer + floating values
