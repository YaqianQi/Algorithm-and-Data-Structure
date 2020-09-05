"""
Given an array of non-negative integers numbers and a non-negative integer k, your task is to return the number of distinct pairs (a, b), where a ≤ b, both a and b are in numbers, they have different indices in numbers, and b - a = k.

Two pairs of integers (a, b) and (c, d) are considered distinct if at least one element of (a, b) is not in (c, d). For example, a pair (1, 2) is distinct from (1, 3) and (2, 3), but not from (1, 2).

Example

For numbers = [1, 1, 2, 2, 3, 3] and k = 1, the output should be countPairsWithDifference2(numbers, k) = 2.

There are 2 distinct pairs in numbers that have a difference of k = 1:

(1, 2)
(2, 3)
Note that each of the pairs are only counted once.

For numbers = [6, 5, 4, 3, 2, 1] and k = 2, the output should be countPairsWithDifference2(numbers, k) = 4.

There are 4 distinct pairs in numbers that have a difference of k = 2:

(1, 3)
(2, 4)
(3, 5)
(4, 6)
For numbers = [1, 2, 5, 6, 9, 10] and k = 2, the output should be countPairsWithDifference2(numbers, k) = 0.

There are no pairs in numbers that have a difference of k = 2.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer numbers

An array of non-negative integers.

Guaranteed constraints:
2 ≤ numbers.length ≤ 2 · 105,
0 ≤ numbers[i] ≤ 109.

[input] integer k

A non-negative integer - the expected difference for the pairs.

Guaranteed constraints:
0 ≤ k ≤ 109.

[output] integer

The number of distinct pairs in numbers with a difference equal to k.
"""


def countPairsWithDifference2(numbers, k):
    from collections import Counter
    cnt = Counter(numbers)
    keys = sorted(cnt)
    res = set()
    for key in keys:
        if k > 0:
            if cnt[key] > 0 and cnt[key + k] > 0:
                pair = (key, key+k)
                res.add(pair)
        elif k == 0:
            if cnt[key]>=2:
                pair = (key, key)
                res.add(pair)
    return len(res) 


numbers = [1, 1, 2, 2, 3, 3]
k = 1
# 2
print(countPairsWithDifference2(numbers, k))

numbers = [6, 5, 4, 3, 2, 1]
k = 2
# 4
print(countPairsWithDifference2(numbers, k))

numbers = [1, 2, 5, 6, 9, 10]
k = 2
# 0
print(countPairsWithDifference2(numbers, k))
numbers= [324004395, 656604343, 635823980, 133767248, 620638222, 734241484, 897179656, 428592089, 159152016, 949541531, 431599440, 225521120, 203479921, 155413784, 559221552, 336139546, 668337900, 560162163, 280339150, 270068090, 226261831, 947456643, 438425635, 591889177, 220598028]
k= 0
# 0
print(countPairsWithDifference2(numbers, k))