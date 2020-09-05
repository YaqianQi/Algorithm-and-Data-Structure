"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Input: "USA"
Output: True
"""
import string
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cnt = [0] * 2 
        init = False
        for i, w in enumerate(word):
            if w.isupper():
                cnt[0] += 1
                if i == 0:
                    init = True 
            elif w.islower():
                cnt[1] += 1
        if (cnt[0] == 1 and init) or cnt[1] == len(word) or cnt[0] == len(word):
            return True
        return False
print(Solution().detectCapitalUse("USA"))
