"""
Design your implementation of the circular double-lasted queue (deque).

Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not. 
isFull(): Checks whether Deque is full or not.


MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be 3
circularDeque.insertLast(1);			// return true
circularDeque.insertLast(2);			// return true
circularDeque.insertFront(3);			// return true
circularDeque.insertFront(4);			// return false, the queue is full
circularDeque.getRear();  			// return 2
circularDeque.isFull();				// return true
circularDeque.deleteLast();			// return true
circularDeque.insertFront(4);			// return true
circularDeque.getFront();			// return 4
2, 1, 3, 4
last     front 

4,3,1, 2
front      last 
"""
class MyCircularDeque:
    
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.len_val = 0 
        self.deque = [0] * k
        self.front = 0
        self.last = -1 
        self.k = k
        

    def insertFront(self, value):
        """
        # Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if not self.isFull():
            # two cases: in the middle: front - 1; in the begging, the insert wiil be in the end. 
            self.front = self.k - 1 if self.front == 0 else self.front - 1
        else:
            self.front = 0 
            self.last = 0 
        self.deque[self.front] = value 
        self.len_val += 1
        return True 

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        # two cases two. use mode to solve. 
        self.last = (self.last + 1) % self.k
        self.deque[self.last] = value 
        self.len_val += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.len_val -= 1
        return True
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """ 
        if self.isEmpty():
            return False
        self.last = self.k - 1 if self.last == 0 else self.last - 1
        self.len_val -= 1
        return True 

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if not self.isEmpty():
            return self.deque[self.last]
        return -1 
        
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.len_val == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.len_val == len(self.deque)

circularDeque = MyCircularDeque(3)
circularDeque.insertLast(1)
circularDeque.insertLast(2)
circularDeque.insertFront(3)
circularDeque.insertFront(4)
print(circularDeque.getRear())