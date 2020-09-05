def find_target_subsets_brute_force(num, s):
    res = []
    def dfs(num, sum_val, idx, t):
        if idx >= len(num): 
            return 
        if idx == len(num) - 1:
            if sum_val == num[idx]:
                res.append(t+f"+{num[idx]}")
                return
            elif sum_val == -num[idx]:
                res.append(t+f"-{num[idx]}")
                return

        dfs(num, sum_val - num[idx], idx + 1, t + f"+{num[idx]}")
        dfs(num, sum_val + num[idx], idx + 1, t + f"-{num[idx]}")
    dfs(num, s, 0, "")
    return len(res)

def find_target_subsets_top_down(num, s):
    res = []
    from collections import defaultdict
    dp = defaultdict(int)
    def dfs(num, sum_val, idx):
        if idx >= len(num): 
            return 0
        if idx == len(num) - 1:
            if sum_val == num[idx]:
                return 1 
            elif sum_val == -num[idx]:
                return 1
        num1 = dfs(num, sum_val - num[idx], idx + 1)
        num2 = dfs(num, sum_val + num[idx], idx + 1)
        return num1 + num2

    return dfs(num, s, 0)


# print(find_target_subsets_brute_force([1,1,2,3], s=1))  
print(find_target_subsets_top_down([1,1,2,3], s=1))