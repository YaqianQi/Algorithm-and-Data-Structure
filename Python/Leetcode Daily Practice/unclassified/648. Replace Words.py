class Solution(object):
    def replaceWords(self, roots, sentence):
        root_set = set(root)
        res = []
        for word in sentence.split():
            prefix = ""
            for i in range(len(word)):
                if word[:i] in root_set:
                    prefix = word[:i]
                    break
            if prefix == "":
                res.append(word) 
        return ' '.join(res) 
