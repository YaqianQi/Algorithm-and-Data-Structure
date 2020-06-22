# time o(nlogn)
class Solution:
    def avoidFlood(self, rains):
        import heapq
        from collections import defaultdict
        h = []
        res = []
        heapq.heapify(h)
        dic = defaultdict(list)
        to_empty = []
        heapq.heapify(to_empty)
        res = [-1] * len(rains)

        for idx, rain in enumerate(rains):
            dic[rain].append(idx)

        for i , rain in enumerate(rains):
            if rain != 0:
                if dic[rain] and dic[rain][0] < i: # full
                    return []
                if dic[rain] and len(dic[rain]) > 1: # can put into waiting list 
                    next_rain = dic[rain][1]
                    heapq.heappush(to_empty, next_rain)
            else: # needs to pop 
                if to_empty: # can pop
                    res[i] = rains[heapq.heappop(to_empty)]
                    dic[res[i]].pop(0)
                else: # nothing to pop 
                    res[i] = 1
        return res

if __name__ == "__main__":
    rains = [1,2,0,2,3,0,1]
    output = [-1,-1,2,-1,-1,1,-1]
    sol = Solution()
    print(sol.avoidFlood(rains))

    # Input: 
    rains = [1,2,3,4]
    #Output: [-1,-1,-1,-1]
    sol = Solution()
    #print(sol.avoidFlood(rains))

    # Input: 
    rains = [1,2,0,0,2,1]
    # Output: [-1,-1,2,1,-1,-1]
    sol = Solution()
    #print(sol.avoidFlood(rains))

    # Input: 
    rains = [1,2,0,1,2]
    # Output: []
    sol = Solution()
    #print(sol.avoidFlood(rains))

    # Input: 
    rains = [69,0,0,0,69]
    # Output: [-1,69,1,1,-1]
    sol = Solution()
    #print(sol.avoidFlood(rains))

    # Input: 
    rains = [10,20,20]
    # Output: []
    sol = Solution()
    #print(sol.avoidFlood(rains))
