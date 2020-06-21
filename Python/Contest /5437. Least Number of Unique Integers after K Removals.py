class Solution:
    def findLeastNumOfUniqueInts(self, arr, k):
        import collections 
        cnt = collections.Counter()
        for val in arr:
            cnt[val]+= 1
        #cnt = sorted(cnt,key=lambda x: cnt[x])
        sorted_cnt = sorted((value, key) for (key,value) in cnt.items())
        while k > 0:
            for val, num in sorted_cnt:
                if val - k > 0:
                    cnt[num] -= k
                    k = 0 
                else:
                    cnt[num] = 0 
                    k-= val
        res = []
        for num, val in cnt.items():
            if val != 0:
                res.append(num) 
        return len(res)

            

if __name__ == "__main__":
    sol = Solution()
    arr = [5,5,4]
    k = 1
    res = sol.findLeastNumOfUniqueInts(arr, k)
    print(res)


    sol = Solution()
    arr = [4,3,1,1,3,3,2]
    k = 3
    res = sol.findLeastNumOfUniqueInts(arr, k)
    print(res)

    sol = Solution()
    arr = [2,4,1,8,3,5,1,3]
    k = 3
    res = sol.findLeastNumOfUniqueInts(arr, k)
    print(res)
    
