import heapq
import random
"""
1. Sort - O(NlogN)
2. Max Heap - O(N + KlogN) / O(N)
3. Min Heap with length K - O(NlogK)
4. Quick select with random pivot - O(N)
Partition (Lomuto, Hoare)
5. Binary search value - [-2**31, 2*31 - 1] => O(32N)
3 bits -> -4, 3 (8)
Similar question: partition with max sum k

"""
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        for _ in range(k):
            ans = heapq.heappop(nums)
        return -ans    


# k+(n-k)*log(k) time
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])
        
        return heap[0]


# Quick select - O(n)
class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        target_index = len(nums) - k
        while l <= r:
            pivot_index = self.partition(nums, l, r)
            if pivot_index == target_index:
                return nums[target_index]
            elif pivot_index < target_index:
                l = pivot_index + 1
            else:
                r = pivot_index - 1
        return 0
        
    # Lomuto
    def partition(self, nums, left, right):
        pivot = randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot] # put pivot at rightmost position
        i = left
        for j in range(left, right): # left to right-1
            if nums[j] <= nums[right]: 
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[right], nums[i] = nums[i], nums[right] # swap the i and the last element
        return i

    # Hoare - faster but harder to implement
    def partition2(self, nums, lo, hi):
        pivot_index = random.randint(lo, hi)
        pivot = nums[pivot_index]
        nums[lo], nums[pivot_index] = nums[pivot_index], nums[lo]
        i, j = lo + 1, hi
        while True:
            while i <= j and nums[i] <= pivot:
                i += 1
            while i <= j and nums[j] >= pivot:
                j -= 1
            if j <= i:
                nums[lo], nums[j] = nums[j], nums[lo] 
                return j
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return 0


# binary search 
class Solution4:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = min(nums), max(nums) + 1
        while l < r:
            m = r - (r - l) // 2 
            if self.count(nums, m) >= k:
                l = m
            else:
                r = m - 1
        return l
    
    def count(self, nums, threshold):
        return sum(num >= threshold for num in nums)
