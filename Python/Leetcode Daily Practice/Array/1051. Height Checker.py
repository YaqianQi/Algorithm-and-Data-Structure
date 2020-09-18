"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students to be standing 
in non-decreasing order of height.

Notice that when a group of students is selected they can reorder in any possible way between 
themselves and the non selected students remain on their seats.

 

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.

*********************************** counting sort *******************************************

Take input [1,1,4,2,1,3] as an example:

The heightToFreq will be [0,3,1,1,1] (the index of this array are the height values). This array is another format of a sorted array (ignore 0) [1,1,1,2,3,4].

The second for loop does the following things:

Find a valid height value (as an index) in the sorted heights array [0,3,1,1,1].
If the valid height value is not equal to heights[i], it means there is a wrong position. Hence increment result by 1.
Regardlessly, we have compared this person's height, hence decrement the value by 1.
"""

class Solution(object):
    def heightChecker_bruteforce(self, heights):
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        height_freq = [0] * 101
        for height in heights:
            height_freq[height] += 1
        
        res = 0 
        cur = 0 

        for i in range(len(heights)):
            while height_freq[cur] == 0:
                cur += 1
            if cur != height[i]:
                res += 1
            height_freq[cur] -= 1
        return res