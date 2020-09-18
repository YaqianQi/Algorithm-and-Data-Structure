class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        left, right = 0, len(A) - 1
        res = []
        while left <= right:
            if abs(A[left]) < abs(A[right]):
                # print(left, right, A[left], A[right])
                res.append(A[right]**2)
                right -= 1
            elif abs(A[right]) < abs(A[left]):
                res.append(A[left] ** 2)
                left += 1
            else:
                res.append(A[right] ** 2)
                if right != left:
                    res.append(A[left] ** 2)
                left += 1
                right -= 1
        return res[::-1]

A = [-4, -1, 0, 3, 10]
print(Solution().sortedSquares(A))