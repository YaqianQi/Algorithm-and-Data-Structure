class Solution:
    def getFolderNames(self, names):
        from collections import defaultdict
        memo = defaultdict(int)
        res = []
        for n in names:
            if memo[n] > 0:
                while n+'('+ str(memo[n]) +')' in memo.keys():
                    memo[n]+=1
                res.append(n+'('+ str(memo[n]) +')')
                memo[n+'('+ str(memo[n])+')']+=1
            else:
                res.append(n)
            memo[n]+=1
        print(memo)
        return res


if __name__== "__main__":
   
    # Input: 
    names = ["pes","fifa","gta","pes(2019)"]
    # Output: ["pes","fifa","gta","pes(2019)"]    
    sol = Solution()
    print(sol.getFolderNames(names))

    # Input: 
    names = ["gta","gta(1)","gta","avalon"]
    Output: ["gta","gta(1)","gta(2)","avalon"]
    sol = Solution()
    print(sol.getFolderNames(names))

    # Input: 
    names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
    # Output: ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
    sol = Solution()
    print(sol.getFolderNames(names))

    # Input: 
    names = ["wano","wano","wano","wano"]
    # Output: ["wano","wano(1)","wano(2)","wano(3)"]
    sol = Solution()
    print(sol.getFolderNames(names))

    # Input: 
    names = ["kaido","kaido(1)","kaido","kaido(1)"]
    sol = Solution()
    print(sol.getFolderNames(names))