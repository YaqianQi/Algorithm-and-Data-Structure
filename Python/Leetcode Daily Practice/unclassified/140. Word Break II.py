class Solution:

    def wordBreak(self, s, wordDict):
        self.memo = {}
        l = len(s)
        def dfs(cur):
            if cur>= l:
                return []
            if cur in self.memo:
                return self.memo[cur]
            res = []
            substring = s[cur:]
            for word in wordDict:
                if substring.startswith(word):
                    if len(word) == len(substring):
                        res.append(word)
                    else:
                        word_rest = dfs(cur + len(word))
                        for wr in word_rest:
                            res.append(word + " "+wr)
            self.memo[cur] = res
            return res
        return dfs(0)
            
#Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
#Output: ["cats and dog","cat sand dog"]
sol = Solution()
print(sol.wordBreak(s, wordDict))