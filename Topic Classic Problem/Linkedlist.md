## Topic 

- Traversal the linkedlist 
  - Merge Two Sorted List
- Reverse the linkedlist 
- find the middle point of the linkedlist 

### 21. Merge Two Sorted Lists

```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        node = dummy 
        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2 
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        if l1:
            node.next = l1
            
        if l2:
            node.next = l2
        return dummy.next 
```



### 143. Reorder List

```python
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        1->2->3->4->5
           s  
                    f 
                   
      p<-c-> t 
          p  c
        """
        # 1. find middle point 
        # 2. reverse 2nd part 
        # 3. connect two list one by one 
        # 1->2->3
        #     n
        # 5->4
        
        def reverse_node(head):
            prev = None
            nxt = None 
            while head:
                nxt = head.next 
                head.next = prev 
                prev = head
                head = nxt 
            return prev 
        if not head or not head.next or not head.next.next:
            return 
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next 
    
        second = slow.next
        slow.next = None # rememebr to break the connection 
        second = reverse_node(second)
        first = head 
        """
           n
        1 2->3
        |/  
        5->4
           i
        1->5->2
        """
        while second:
            nxt = first.next 
            first.next = second 
            second = second.next 
            first = first.next
            first.next = nxt
            first = first.next
    
```

### 138. Copy List with Random Pointer

- graph 
- traversal 

```python 
class Solution(object):
    def copyRandomList(self, head):
        """
        
        1 -> 2 -> 3 -> 4
        cur = 1, cur.next = 2
        map_lst[cur] = new_1
        map_lst[cur.next] = new_2
        new_1 -> new_2
        
        1 1 
        2 2
        3 3 
        4 4
        o(n)
        """
        if not head:
            return None 
        from collections import defaultdict
        map_lst = defaultdict(Node)
        cur = head
        while cur:
            map_lst[cur] = Node(cur.val)
            cur = cur.next 
        
        cur = head 
        while cur:
            if cur.next:
                map_lst[cur].next = map_lst[cur.next]
            if cur.random:
                map_lst[cur].random = map_lst[cur.random]
            cur = cur.next 
        return map_lst[head]
```



