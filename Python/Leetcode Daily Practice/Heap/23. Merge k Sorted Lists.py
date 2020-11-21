import heapq
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = heapq([])
        for l in lists:
            if l:
                heapq.heappush((l.val, l))
        while not q.empty():
            val, node = heapq.heappop(q)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush((node.val, node))
        return head.next

Solution().mergeKLists()