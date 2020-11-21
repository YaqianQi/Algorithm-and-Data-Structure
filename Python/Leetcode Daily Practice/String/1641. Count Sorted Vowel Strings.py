class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        Input: n = 2
        Output: 15
        Explanation: The 15 sorted strings that consist of vowels only are
        ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
        Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
        """
        lst = ["a","e","i","o","u"]
        token_dict = {val: idx for idx, val in enumerate(lst)}
        if n == 1:
            return len(lst) 
        res =[]
        def dfs(idx, t, prev):
            if len(t) == n:
                res.append(t)
                return 
            for i in range(idx, len(lst)):
                if not prev:
                    dfs(idx, t + lst[i], lst[i])
                else:
                    prev_pos = token_dict[prev]
                    if token_dict[lst[i]] >= prev_pos:
                        dfs(idx, t + lst[i], lst[i])
        dfs(0, "", "")
        return len(res)
print(Solution().countVowelStrings(2))