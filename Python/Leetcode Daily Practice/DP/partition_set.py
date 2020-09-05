"""
Given a set of positive numbers, 
find if we can partition it into two subsets such that the sum of elements in both 
the subsets is equal.
"""
def can_partition(num):
    # TODO: Write your code here
    from collections import defaultdict
    d = defaultdict(list)
    def dfs(num, idx, t):
        if idx > len(num) or len(t) > len(num):
            return
        for i in range(idx, len(num)):
            if int(num[i]) in list(t):
                continue
            else:
                sum_val = sum(t) + num[i]
                d[sum_val].append(t+[num[i]])
                dfs(num, i+1, t+[num[i]])
                
    half_sum = sum(num)//2
    dfs(num, 0, [])
    return len(d[half_sum])>=2
print(can_partition([1,2,3,4]))