class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        if len(arr)==1:
            return True
        delta = arr[1] - arr[0]
        t = arr[0] 
        for i in range(1, len(arr)):
            t += delta 
            if arr[i]!= t:
                return False
        return True

if __name__=="__main__":
    # Input: 
    arr = [3,5,1]
    # Output: true
    # Explanation: We can reorder the elements as [1,3,5] or 
    # [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
    sol = Solution()
    print(sol.canMakeArithmeticProgression(arr))

    # Input: 
    arr = [1,2,4]
    # Output: false
    # Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
    sol = Solution()
    print(sol.canMakeArithmeticProgression(arr))