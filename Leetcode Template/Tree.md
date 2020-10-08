# Main Frame 

1. Tree traversal recursive 

   - Pre-order 

   - In-order 
   - post-order

2. Iterative Traversal 

------------------------------

# Question Classification

## Pre order traversal

### Basic Template

#### Basic recursive 

```python
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        def dfs(root):
            if not root:
                return
            self.res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res
```

#### Iteration

- Time complexity : we visit each node exactly once, thus the time complexity is O(*N*), where N is the number of nodes, *i.e.* the size of tree.
- Space complexity : depending on the tree structure, we could keep up to the entire tree, therefore, the space complexity is O(*N*).

```python 
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque 
        if root is None:
            return []
        stack = deque()
        stack.append(root)
        output = []
        
        while stack:
            root = stack.pop()
        
            output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        
        return output
```

### Question Classification

#### Binary Tree Features 

##### 669. Trim a Binary Search Tree

```python
class Solution(object):
    def trimBST(self, root, L, R):
        def dfs(root):
            if not root:
                return 
            if root.val < L: #the left side is discarded
                return dfs(root.right)
            if root.val > R: # the right side is discarded 
                return dfs(root.left)
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            return root
        return dfs(root)
```

##### 404. Sum of Left Leaves

- Find the sum of all left leaves in a given binary tree.

```python
class Solution(object):
    # iterative 
    def sumOfLeftLeaves(self, root):
        """

        Example:

            3
           / \
          9  20
            /  \
           15   7

        There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
        """
        def dfs(root):
            if not root:
                return 0
            res = 0 
            if root.left:
                if not root.left.left and not root.left.right:
                    res += root.left.val
                else:
                    res += dfs(root.left)
            res += dfs(root.right)
            return res
        return dfs(root)

    def sumOfLeftLeaves_bfs(self, root):
        from collections import deque 
        q = deque()
        q.append(root)
        res = 0
        if not root:
            return 0 
        while q:
            cur = q.popleft()
            if cur and cur.left:
                if not cur.left.left and not cur.left.right:
                    res += cur.left.val 
                else:
                    q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return res
    # recursive dfs like dp     
    def sumOfLeftLeaves_recursive(self, root):
        def dfs(root, is_left):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val if is_left else 0
            return dfs(root.left, True) + dfs(root.right, False) 
        
        return dfs(root, False)
```

#### Traversal + pre-order features

##### 572. Subtree of Another Tree

```python
class Solution(object):
    def isSubtree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
```

similar question: 

- 100.same tree
- 101.Symmetric Tree

##### 297. Serialize and Deserialize Binary Tree

- Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

```python
class Codec:
    def serialize(self, root):
        """ 
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        
        You may serialize the following tree:

            1
           / \
          2   3
             / \
            4   5

        as "[1,2,3,null,null,4,5]"
        """
        def rserialize(root, string):
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
```

- Time complexity : in both serialization and deserialization functions, we visit each node exactly once, thus the time complexity is *O*(*N*), where N*N* is the number of nodes, *i.e.* the size of tree.
- Space complexity : in both serialization and deserialization functions, we keep the entire tree, either at the beginning or at the end, therefore, the space complexity is *O*(*N*).

## In Order Traversal

-  `Left -> Node -> Right`

### Basic Template

#### Recursive 

```python
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []
```

####  Iterating method using Stack

```java
public class Solution {
    public List < Integer > inorderTraversal(TreeNode root) {
        List < Integer > res = new ArrayList < > ();
        Stack < TreeNode > stack = new Stack < > ();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }
}
```

- Successor = "after node", i.e. the next node, or the smallest node *after* the current one.

```python
def successor(root):
    root = root.right
    while root.left:
        root = root.left
    return root
```

Predecessor = "before node", i.e. the previous node, or the largest node *before* the current one.

```python
def predecessor(root):
    root = root.left
    while root.right:
        root = root.right
    return root
```

![precessor and succesor](/Users/aliciaqi/Documents/Leetcode Template/pics/precessor and succesor.png)



### Question Classification

#### 450. Delete Node in a BST![find successor](/Users/aliciaqi/Documents/Leetcode Template/pics/find successor.png)



```python 
class Solution(object):
    def deleteNode(self, root, key):

        def find_min(root): # successor 
            while root.left: 
                root = root.left 
            return root

        if not root:
            return 
        if root.val > key: 
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right 
            elif not root.right:
                return root.left 
            else:
                min_val = find_min(root.right)
                root.val = min_val.val
                root.right = self.deleteNode(root.right, root.val) 
        return root
```



- Time complexity : O(log*N*). During the algorithm execution we go down the tree all the time - on the left or on the right, first to search the node to delete and then to actually delete it. *H*1 is a tree height from the root to the node to delete. Delete process takes O(*H*2) time, where *H*2 is a tree height from the root to delete to the leafs. That in total results in O(*H*1+*H*2)=O(*H*) time complexity, where *H* is a tree height, equal to log*N* in the case of the balanced tree.

- Space complexity : O(*H*) to keep the recursion stack, where H*H* is a tree height. H = log*N* for the balanced tree.

  



## Post order traversal

### Basic Template

#### Basic Template 1: recursive 

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
```

#### Basic Template 2: iteration	

```python
class Solution(object):
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
                
        return output[::-1]
```

#### Basic Template 3：iteration 不好记

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, output = [], []
        while root or stack:
            # push nodes: right -> node -> left 
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            # if the right subtree is not yet processed
            if stack and root.right == stack[-1]:
                stack[-1] = root
                root = root.right
            # if we're on the leftmost leaf
            else:
                output.append(root.val)
                root = None
                
        return output
```

- Complexity Analysis 
  - Time complexity: O(*N*), where *N* is the number of nodes. We visit each node exactly once, thus the time complexity is O(*N*).
  - Space complexity: up to O(*H*) to keep the recursion stack, where *H* is a tree height.

### Question Classification

#### post order + memo table

##### 663. Equal Tree Partition

```python
class Solution(object):
    def checkEqualTree(self, root):
        
        def sum_node(root):# normal template 
            if not root:
                return 0
            cur = root.val + sum_node(root.left) + sum_node(root.right)
            self.map[cur] += 1
            return cur
          
        from collections import defaultdict
        self.map = defaultdict(int)
        sum_val = sum_node(root)
        if sum_val == 0:
            return self.map[sum_val] > 1
        return sum_val % 2 == 0 and sum_val//2 in self.map
```

- Time Complexity: O(N) where N is the number of nodes in the input tree. We traverse every node.
- Space Complexity: O(N), the size of [map] and the implicit call stack in our DFS.

#### post order + tree features 

##### 671. Second Minimum Node In a Binary Tree

```python
Class Solution(object):
    def findSecondMinimumValue(self, root):
        def dfs(root, min_val):
            if not root:
                return -1 
            if root.val > min_val:
                return root.val 
            left = dfs(root.left, min_val)
            right = dfs(root.right, min_val)
            if left == -1 or right == -1:
                return max(left, right)
            else:
                return min(left, right)
        if not root:
            return -1
        return dfs(root, root.val)
```

- Time Complexity: *O*(*N*), where N*N* is the total number of nodes in the given tree. We visit each node at most once.
- Space Complexity: *O*(*N*). The depth-first search may store up to *O*(*h*)=*O*(*N*) information in the call stack, where h*h* is the height of the tree.

## Level Order Traversal 

### Basic Template

#### Recursion

- Time complexity : O(*N*) since each node is processed exactly once.
- Space complexity : O(*N*) to keep the output structure which contains `N` node values.

```python
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels
```

#### Iteration

- Time complexity : O(*N*) since each node is processed exactly once.
- Space complexity : O(*N*) to keep the output structure which contains `N` node values.

```python
from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels
```



### Question classification 

#### Level Order + Memo Table 

##### 662. Maximum Width of Binary Tree

```python
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import defaultdict 
        d = defaultdict(int)
        res = 0
        if not root:
            return res
        
        level = 0
        queue = deque([root,])
        while queue:
            # number of elements in the current level 
            level_length = len(queue)
            start = 0 
            end = -1 
            for i in range(level_length):
                node = queue.popleft()
                if i == 0:
                    start = d[node]
                if i == level_length - 1:
                    end = d[node]
                
                if node.left:
                    d[node.left] = d[node] * 2
                    queue.append(node.left)
                if node.right:
                    d[node.right] = d[node] * 2 + 1
                    queue.append(node.right)
            
            # go to next level
            res = max(res, end - start + 1)
        
        return res
```

- **Complexity Analysis**

  Let *N* be the total number of nodes in the input tree.

  - Time Complexity: O(*N*)
    - We visit each node once and only once. And at each visit, it takes a constant time to process.
  - Space Complexity:O(*N*)
    - We used a queue to maintain the nodes along with its indices, which is the main memory consumption of the algorithm.
    - Due to the nature of BFS, at any given moment, the queue holds no more than *two levels* of nodes. In the worst case, a level in a full binary tree contains at most half of the total nodes (2*N*), *i.e.* this is also the level where the leaf nodes reside.
    - Hence, the overall space complexity of the algorithm is O(*N*).

