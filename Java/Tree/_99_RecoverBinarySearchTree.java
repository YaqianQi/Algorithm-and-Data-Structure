import java.util.*;
public class _99_RecoverBinarySearchTree {
	// time o(n)
	// space o(n)
	TreeNode first = null;
	TreeNode second = null;
	TreeNode prev = null;
	// inorder traversal 
	public void recoverTree(TreeNode root) {
	        if(root == null) return ;
	        helper(root);
	        int temp = first.val;
	        first.val = second.val;
	        second.val = temp;
	    }
	public void helper(TreeNode root) {
		if(root == null) return;
		helper(root.left);
		if (prev!=null && prev.val >= root.val) {
			if(first == null) first = prev;
			second = root; 
		}
		prev = root;
		helper(root.right);
	}
	
	public void recoverTreeRec(TreeNode root) {
        if(root == null) return ;
        TreeNode first = null;
    	TreeNode second = null;
    	TreeNode prev = null;
    	
    	TreeNode cur = root;
    	Stack<TreeNode> stack = new Stack<>();
    	while(!stack.isEmpty()|| cur!=null) {
    		if(cur!=null) {
    			stack.push(cur);
    			cur = cur.left;
    		}else {
    			cur = stack.pop();
    			if(prev != null && cur.val <= prev.val) {
    				if(first == null) first = prev;
    				second = cur;
    			}
    			prev = cur;
    			cur = cur.right;
    		}
    	}
    	int temp = first.val;
        first.val = second.val;
        second.val = temp;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode root = new TreeNode(1);
		root.left = new TreeNode(3);
		root.left.right = new TreeNode(2);
		
		_99_RecoverBinarySearchTree rbs = new _99_RecoverBinarySearchTree();
		rbs.recoverTree(root);
	}

}
