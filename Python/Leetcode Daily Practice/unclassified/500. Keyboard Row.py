class Solution(object):
    def findWords(self, words):
        # I have used set to check the word.I firstly make every line a set of letter.
        # Then I check every word if this word set is the subset if any line set.
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        ret = []
        for word in words:
            w = set(word.lower())
            if w <= line1 or w <= line2 or w <= line3:
                ret.append(word)
        return ret
word = set("qwera")
word_set = set("qwertyuiop")
print(word <= word_set)