
class Solution:
    def canArrange(self, arr, k):
        # etl 
        cnt = 0
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                
                if arr[i]!= "x" and arr[j]!= "x":
                    if (arr[i] + arr[j]) % k == 0:
                        arr[j] = "x"
                        cnt += 1
                        break
        return cnt == int(len(arr)//2) 
    def canArrange(self, arr, k):
        return sum(arr)%k==0



if __name__=="__main__":
    # Input: 
    arr = [1,2,3,4,5,10,6,7,8,9]
    k = 5
    # Output: true
    # Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
    sol = Solution()
    print(sol.canArrange(arr, k))

    arr = [1,2,3,4,5,6]
    k = 7
    # 21, 3 * 3 = 9 , 
    # Output: true
    sol = Solution()
    print(sol.canArrange(arr, k))

    #Input: 
    arr = [1,2,3,4,5,6]
    k = 10
    # Output: false
    sol = Solution()
    print(sol.canArrange(arr, k))