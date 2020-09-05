class Solution(object):
    def replaceWords(self, roots, sentence):
        root_set = set(roots)
        res = []
        for word in sentence.split():
            prefix = ""
            for i in range(len(word)):
                if word[:i] in root_set:
                    prefix = word[:i]
                    res.append(prefix)
                    break
            if prefix == "":
                res.append(word)
             
        return ' '.join(res) 
