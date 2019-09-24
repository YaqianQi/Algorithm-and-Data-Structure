
public class _111_MinimumDepthofBinaryTree {
	public int minDepth(TreeNode root) {
	        if (root == null) return 0;
	        if (root.left != null) return 1+minDepth(root.left);
	        if (root.right != null) return 1+minDepth(root.right);
	        return 1 + Math.min(minDepth(root.left), minDepth(root.right));
	    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode t  = new TreeNode(3);
		t.right = new TreeNode(20);
		t.left = new TreeNode(9);
		t.right.left = new TreeNode(15);
		t.right.right = new TreeNode(7);
		_111_MinimumDepthofBinaryTree mdbt = new _111_MinimumDepthofBinaryTree();
		System.out.println(mdbt.minDepth(t));
	}

}
