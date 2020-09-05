"""
Given an array nums sorted in ascending order, return true if and only if you can split it into 1 or more subsequences 
such that each subsequence consists of consecutive integers and has length at least 3.

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5

Input: [1,2,3,3,4,4,5,5]
                    i
{3: 0, 4: 1, 5: 1, 1: 0, 2: 0}
next = {4:0,5:0, 6:2}
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5

{3: 2, 4: 2, 5: 2, 1: 1, 2: 1}
"""
class Solution(object):
    def isPossible(self, nums):
        from collections import Counter, defaultdict
        freq = Counter(nums)
        next_val_dict = defaultdict(int)
        for num in nums:
            print(num, freq, next_val_dict)
            if freq[num] == 0:
                continue
            elif next_val_dict[num]> 0:
                next_val_dict[num] -= 1
                next_val_dict[num + 1] += 1 
            elif freq[num + 1] > 0 and freq[num+2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                next_val_dict[num+3] += 1
            else:
                return False
            freq[num] -= 1
        return True

nums = [1,2,3,3,4,4,5,5]
print(Solution().isPossible(nums))
        