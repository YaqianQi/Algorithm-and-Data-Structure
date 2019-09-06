
public class _124_BinaryTreeMaximumPathSum {
	// find max value for a tree
	int res;
	public int maxPathSum(TreeNode root) {
		if (root == null) return 0;
		res = Integer.MIN_VALUE;
		
		helper(root);
		return res;
	}
	
	public int helper(TreeNode root) {
		if(root == null) return 0;
		int left = Math.max(0, helper(root.left));
		int right = Math.max(0, helper(root.right));
		res = Math.max(res,  left + right + root.val);
		return Math.max(left,  right) + root.val;
		
	}
	public static void main(String[] args) {
		TreeNode t = new TreeNode(1);
		t.left = new TreeNode(2);
		t.right = new TreeNode(3);
		_124_BinaryTreeMaximumPathSum btmps = new _124_BinaryTreeMaximumPathSum();
		System.out.println(btmps.maxPathSum(t));
		
	}

}
