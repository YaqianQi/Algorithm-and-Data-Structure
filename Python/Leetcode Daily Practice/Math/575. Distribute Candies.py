

class Solution(object):
    def distributeCandies2(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        from collections import Counter
        n = len(candies)/2
        cnt = Counter()
        for c in candies:
            cnt[c]+= 1
        cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        res = []
        idx = 0 
        while idx < len(cnt) and n > 0:
            res.append(cnt[idx][0])
            n -= 1
            idx += 1
            #print(res)
        return len(res)

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        from collections import Counter
        n = len(candies)/2
        kind = len(set(candies))
        return min(kind, n)


if __name__ == "__main__":
    """distribute these candies equally in number to brother and sister. 
    Return the maximum number of kinds of candies the sister could gain.


    Input: candies = [1,1,2,2,3,3]
    Output: 3
    Explanation:
    There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
    Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
    The sister has three different kinds of candies. """    


    candies = [1,1,2,2,3,3]
    print(Solution().distributeCandies(candies))