class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # time: o(m+n), space: o(m)
        from collections import defaultdict
        d = defaultdict()
        for i, p in enumerate(list1):
            d[p] = i
        min_val, res = float("inf"), []
        for i, p in enumerate(list2):
            if p in d:
                if d[p] + i <= min_val:
                    # challenge part 
                    if (d[p] + i < min_val):
                        res = []
                        min_val = d[p] + i
                    res.append(p)
        return res


if __name__ == "__main__":
    # Input:
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    # Output: ["Shogun"]
    # Explanation: The only restaurant they both like is "Shogun".
    sol = Solution()
    print(sol.findRestaurant(list1, list2))