
public class _110_BalancedBinaryTree {
	// o(n)
	public boolean isBalanced(TreeNode root) {
		if (root == null) return true;
	       return helper(root) != -1;
	    }
	
	int helper(TreeNode root){
		if (root == null) return 0;
		int l = helper(root.left);
		int r = helper(root.right);
		if(l == -1 || r == -1|| Math.abs(l-r) > 1) {
			return -1;
		}
		return Math.max(l, r)+1;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 TreeNode t = new TreeNode(3);
		 t.left = new TreeNode(9);
		 t.right = new TreeNode(20);
		 t.right.left = new TreeNode(15);
		 t.right.right = new TreeNode(7);
		 
		 TreeNode t2 = new TreeNode(1);
		 t2.left = new TreeNode(2);
		 t2.left.left = new TreeNode(3);
		 t2.left.right = new TreeNode(3);
		 t2.left.right.left = new TreeNode(4);
		 t2.left.right.right = new TreeNode(4);
		 t2.right = new TreeNode(2);
		 _110_BalancedBinaryTree bbt = new _110_BalancedBinaryTree();
		 System.out.println(bbt.isBalanced(t));
		 System.out.println(bbt.isBalanced(t2));
	}

}
