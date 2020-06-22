from collections import Counter
cnt = Counter()
lst = [1,1,2,3,4]
for rain in lst:
    cnt[rain] += 1
cnt = sorted(cnt.items(),key=lambda x: (x[1],x[0]))
#cnt.sort(key=lambda x:x[])

print(cnt.pop(0))