
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        import heapq
        h = set([1])
        heap = [1]
        heapq.heapify(heap)

        while n:
            a = heapq.heappop(heap)
            for i in primes:
                m = a * i
                if not m in h:
                    heapq.heappush(heap, m)
                    h.add(m)
                print(f"a:{a}, m:{m}, heap:{heap}")
            n -= 1
        return a

if __name__ == "__main__":
    """
    a:1, m:2, heap:[2]
    a:1, m:7, heap:[2, 7]
    a:1, m:13, heap:[2, 7, 13]
    a:1, m:19, heap:[2, 7, 13, 19]
    a:2, m:4, heap:[4, 7, 13, 19]
    a:2, m:14, heap:[4, 7, 13, 19, 14]
    a:2, m:26, heap:[4, 7, 13, 19, 14, 26]
    a:2, m:38, heap:[4, 7, 13, 19, 14, 26, 38]
    a:4, m:8, heap:[7, 14, 8, 19, 38, 26, 13]
    a:4, m:28, heap:[7, 14, 8, 19, 38, 26, 13, 28]
    a:4, m:52, heap:[7, 14, 8, 19, 38, 26, 13, 28, 52]
    a:4, m:76, heap:[7, 14, 8, 19, 38, 26, 13, 28, 52, 76]
    """
    n = 12
    primes = [2,7,13,19]
    sol = Solution()
    print(sol.nthSuperUglyNumber(n, primes))