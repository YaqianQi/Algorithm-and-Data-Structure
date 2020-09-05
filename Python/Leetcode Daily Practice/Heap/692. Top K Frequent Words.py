class Solution(object):
    def topKFrequent(self, words, k):
        from collections import Counter
        import heapq
        cnt = Counter(words) # o(n)
        h = [(-freq, key) for key, freq in cnt.items()] # o(n)
        return [heapq.heappop(h)[1] for i in range(k)] # o (k * logn)
print(Solution().topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k = 2))