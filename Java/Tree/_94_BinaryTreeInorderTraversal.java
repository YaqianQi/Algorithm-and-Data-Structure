import java.util.*;
public class _94_BinaryTreeInorderTraversal {
	public List<Integer> inorderTraversalRec(TreeNode root) {
		List<Integer> res = new ArrayList<>();
        helper(root, res);
        return res;
	  }
	void helper(TreeNode root, List<Integer> res) {
		if (root == null) return ;
		
		helper(root.left,res);
		res.add(root.val);
		helper(root.right,res);
	}
	// 先把左边放进去， 然后再使用template，在放右边
	 public List<Integer> inorderTraversal(TreeNode root) {
	    List<Integer> res = new ArrayList<>();
	    Stack<TreeNode> stack = new Stack<>();
	    
	    TreeNode p = root;
	    while(p!= null) {
	    	stack.push(p);
	    	p = p.left;
	    }
	    
	    while(!stack.isEmpty()) {
	    	TreeNode t = stack.pop();
	    	res.add(t.val);
	    	t = t.right;
	    	while(t!=null) {
	    		stack.push(t);
	    		t = t.left;
	    	}
	    	
	    }
	    return res;
	 }
	    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// TODO Auto-generated method stub
		TreeNode t1 = new TreeNode(1);
		t1.right = new TreeNode(2);
		t1.right.left = new TreeNode(3);
		
		_94_BinaryTreeInorderTraversal ntit = new _94_BinaryTreeInorderTraversal();
		System.out.println(ntit.inorderTraversalRec(t1));
		System.out.println(ntit.inorderTraversal(t1));
	}

}
