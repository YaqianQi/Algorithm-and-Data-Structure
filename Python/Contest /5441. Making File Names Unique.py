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


    # Input: 
    names = ["gta","gta(1)","gta","avalon"]
    Output: ["gta","gta(1)","gta(2)","avalon"]


    # Input: 
    names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
    # Output: ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
    sol = Solution()
    # print(sol.getFolderNames(names))

    # Input: 
    names = ["wano","wano","wano","wano"]
    # Output: ["wano","wano(1)","wano(2)","wano(3)"]
    sol = Solution()
    #print(sol.getFolderNames(names))

    # Input: 
    names = ["kaido","kaido(1)","kaido","kaido(1)"]
    
    # Output: ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
    # {kaido: {0 : 2},{1: 2}}
    # name = kaido,  prex = kaido 
    # p_cnt = 0 , freq = 0, suffix = "" 
    # final_name = name + suffix 
    # name kaido(1), prex = kaido 
    # p_cnt = 1, freq = 0, suffix = (p_cnt) * (freq)
    # final_name = kaido(1)
    # name = kaidp , prex = kaido 
    # p_cnt = 0 ,freq = 1, suffix = (1)
    # fanme 
    sol = Solution()
    #print(sol.getFolderNames(names))