from typing import List


def countSort(arr) -> List:
    max_value = max(arr)
    count = [0] * (max_value+1)

    for a in arr:
        count[a] += 1

    result = []
    for idx, freq in enumerate(count):
        result.extend([idx] * freq)

    return result


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 5, 5, 1, 3, 4, 1, 1]
    print(countSort(arr))

# Time complexity :- O(N + K) where K is range and N is number of element in array and works only on integer values
# each number is bucket here
# why O(N + K) not O(N * K) bcz at the end the N values append to the result and K(range)
# It is generally used where the array range is small bcz if the K is large then
# O(N + K) = 10^5 + 10^3 = 10^5
# O(N + K) = 10^5 + 10^5 = 2 * 10^5
# O(N + K) = 10^5 + 10^8 = 10^8
# So it grows on K which is range
