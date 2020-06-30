class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # brute-force o(n^2)
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    idx = j + 1
                    while idx < len(nums2):
                        if nums2[idx]>nums1[i]:
                            res[i] = nums2[idx]
                            break
                        idx+= 1
        return res

    def nextGreaterElement(self, nums1, nums2):
        # stack o(n) 
        res = [-1] * len(nums1)
        from collections import defaultdict
        d = defaultdict()
        stack = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                d[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            res[i] = d.get(nums1[i], -1)
        return res


if __name__ == "__main__":
    # Input 
    nums1 = [1,3,5,2,4]
    nums2 = [6,5,4,3,2,1,7]
    stack = [6, 5, 4, 3, 2, 1]
    # output 
    #Input: [7,7,7,7,7]

    sol = Solution()
    print(sol.nextGreaterElement(nums1, nums2))

    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    # stack = [1] < 3 , d = {1:3}
    # stack = [3] < 4, d +={3:4}
    # stack = [4] 
    # -> d = {1:3, 3:4}
    # res = [-1, 3, -1] 
    # Output: [-1,3,-1]
    # Explanation:
    # For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    # For number 1 in the first array, the next greater number for it in the second array is 3.
    # For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

    sol = Solution()
    # print(sol.nextGreaterElement(nums1, nums2))


    # Input: 
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    # Output: [3,-1]

    sol = Solution()
    #print(sol.nextGreaterElement(nums1, nums2))