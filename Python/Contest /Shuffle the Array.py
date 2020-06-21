class Solution:
    def shuffle(self, nums, n):
        part1 = nums[:n]
        part2 = nums[n:]
        res = []
        for x, y in zip(part1, part2):
            res.append(x)
            res.append(y)
        return res

if __name__ =="__main__":
    nums = [2,5,1,3,4,7]
    n = 3
    sol = Solution()
    print(sol.shuffle(nums, n))

    nums = [1,2,3,4,4,3,2,1]
    n = 4
    print(sol.shuffle(nums, n))

    nums = [1,1,2,2]
    n = 2
    print(sol.shuffle(nums, n))