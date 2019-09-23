import java.util.*;
// o(n)
public class _145_BinaryTreePostorderTraversal {
	public List<Integer> postorderTraversalRec(TreeNode root) {
	        List<Integer> res = new ArrayList<>();
	        if(root == null) return res;
	        helper(root, res);
	        return res;
	    }
	
	void helper(TreeNode root, List<Integer> res) {
		if (root == null) return ;
		helper(root.left, res);
		helper(root.right,res);
		res.add(root.val);
	}
	
	
	 public List<Integer> postorderTraversalStack(TreeNode root) {
	        LinkedList<Integer> res = new LinkedList<>();
	        Stack<TreeNode>  stack = new Stack<>();
	        stack.push(root);
	        while(!stack.isEmpty()) {
	        	TreeNode cur = stack.pop();
	        	res.addFirst(cur.val);
	        	if (cur.left!= null) stack.push(cur.left);
	        	if (cur.right != null) stack.push(cur.right);
	        }
	        return res;
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode t1 = new TreeNode(1);
		
		t1.right = new TreeNode(2);
		t1.right.left = new TreeNode(3);
		_145_BinaryTreePostorderTraversal btpt = new _145_BinaryTreePostorderTraversal();
		System.out.println(btpt.postorderTraversalRec(t1));
		System.out.println(btpt.postorderTraversalStack(t1));
	}

}
