import bisect 

lst = [(1,'a'),(2,'b'),(4,'c'),(4,'d')]
l = bisect.bisect(lst, (3,chr(0)))
#print(l,lst2[l],  r, lst2[r])

s = "abc(1)(2)"
#print(len(s) -s[::-1].index(")"))


def helper(s):
    cnt = 0 
    for i in range(len(s)):
        if s[i] == "(":
            cnt+= 1
    return cnt
print(helper(s))


import re
s1 =  re.split('[()]', name)
lst = [x for x in s1 if x!= "" ]
print(lst)

