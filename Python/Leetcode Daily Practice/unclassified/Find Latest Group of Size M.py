class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        n = len(arr)
        s = ["0"] * n 
        target = "1" * m
        res = -1
        for i in range(n):
            s[arr[i]-1] = "1"
            t = "".join(s).split("0")
            if target in t:
                res = i + 1
        return res
arr = [3,5,1,2,4]
m = 2      
print(Solution().findLatestStep(arr, m))

arr = [2,1]
m = 2  
print(Solution().findLatestStep(arr, m))
"""
Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "00101", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "11101", groups: ["111", "1"]
Step 5: "11111", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.


Input: arr = [2,1], m = 2
Output: 2
step 0: "00"
step 1: "01"
step 2: "11"
"""