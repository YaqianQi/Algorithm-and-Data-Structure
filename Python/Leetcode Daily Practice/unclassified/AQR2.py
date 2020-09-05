"""

Given an array of integers a and an integer m, your task is to find the maximum value among the minimum values of each contiguous subarray of size m in array a.

Example

For a = [1, 2, 3, 1, 2] and m = 1, the output should be maxMinInSubarrays(a, m) = 3.

The subarrays of size m = 1 are [1], [2], [3], [1], and [2]. Since each array contains only one element, each value is the minimal element of the subarray it is in. The maximum of these values is 3.

For a = [1, 1, 1] and m = 2, the output should be maxMinInSubarrays(a, m) = 1.

The subarrays of size m = 2 are [1, 1] and [1, 1]. The minimum value for both arrays is 1. The maximum of these values is 1.

For a = [2, 5, 4, 6, 8] and m = 3, the output should be maxMinInSubarrays(a, m) = 4.

The subarrays of size m = 3 are [2, 5, 4], [5, 4, 6], and [4, 6, 8]. The respective minimum values for these subarrays are 2, 4, and 4, so the maximum of these values is 4.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

An array of integers in which subarrays should be considered.

Guaranteed constraints:
1 ≤ a.length ≤ 106,
1 ≤ a[i] ≤ 109.

[input] integer m

An integer representing the size of the subarrays to consider.

Guaranteed constraints:
1 ≤ m ≤ 105,
m ≤ a.length.

[output] integer

The maximum value among the minimum values of all subarrays of size m.
"""


def maxMinInSubarrays(a, m):
    import collections
    ans, inc = a[0], collections.deque()
    for i, num in enumerate(a):
        # maintain mono non-decreasing deque
        # [1,2,3,4]
        while inc and a[inc[-1]] > num:
            inc.pop()
        inc.append(i)
        # lazy deletion
        if inc[0] <= i - m:
            inc.popleft()
        # update ans if we find a larger min
        if i >= m - 1:
            ans = max(ans, a[inc[0]])
    return ans

        
a = [2, 5, 4, 6, 8] 
m = 3
# 4
print(maxMinInSubarrays(a, m))

a = [1, 2, 3, 1, 2] 
m = 1
print(maxMinInSubarrays(a, m))