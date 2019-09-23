import java.util.*;
public class _144_BinaryTreePreorderTraversal {
	// recursive 
	public List<Integer> preorderTraversalRec(TreeNode root) {
	        List<Integer> res = new ArrayList<>();
	        helper(root, res);
	        return res;
	  }
	void helper(TreeNode root, List<Integer> res) {
		if (root == null) return ;
		res.add(root.val);
		helper(root.left,res);
		helper(root.right,res);
	}
	
	public List<Integer> preorderTraversal(TreeNode root) {
		List<Integer> res = new ArrayList<>();
		Stack<TreeNode> stack = new Stack<>();
		stack.push(root);
		while (!stack.isEmpty()) {
			TreeNode t = stack.pop();
			res.add(t.val);
			if (t.right != null) stack.push(t.right);
			if (t.left != null) stack.push(t.left);
		}
		return res;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode t1 = new TreeNode(1);
		t1.right = new TreeNode(2);
		t1.right.left = new TreeNode(3);
		_144_BinaryTreePreorderTraversal brpt = new _144_BinaryTreePreorderTraversal();
		System.out.println(brpt.preorderTraversalRec(t1));
		System.out.println(brpt.preorderTraversal(t1));
	}

}
