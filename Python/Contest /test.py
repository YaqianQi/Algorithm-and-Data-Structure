import bisect 

lst = [(1,'a'),(2,'b'),(3,'c'),(3,'d')]
l = bisect.bisect(lst, (3,chr(0)))
#print(l,lst2[l],  r, lst2[r])
print(l)