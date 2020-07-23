class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def dfs(t):
            if t == None:
                return ""
            if t.left == None and t.right == None:
                return str(t.val) + ""
            if t.right == None:
                return str(t.val) + "(" + dfs(t.left)+")"
            
            return str(t.val) + "("+dfs(t.left) + ")" + "("+ dfs(t.right) + ")"
            
        return dfs(t)


if __name__ == "__main__":
    """
    case 1: missing right , dont care 
    Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     
   

    Output: "1(2(4))(3)"

    Explanation: Originallay it needs to be "1(2(4)())(3()())", 
    but you need to omit all the unnecessary empty parenthesis pairs. 
    And it will be "1(2(4))(3)".

    # missing left  create empty parenthese for them 
    Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

    Output: "1(2()(4))(3)"

    Explanation: Almost the same as the first example, 
    except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output."""