
public class _250_CountUnivalueSubtrees {
	int res;
	// post-traversal 
	// 
	public int countUnivalSubtrees(TreeNode root) {
		res = 0;
		helper(root);
		return res;
	    }
	public boolean helper(TreeNode root) {
		if(root == null) return true;
		boolean left = helper(root.left);
		boolean right = helper(root.right);
		if(left && right) {
			if(root.left!= null && root.val!= root.left.val) {
				return false;
			}
			if(root.right!=null && root.val != root.right.val) {
				return false;
			}
			res++;
			return true;
		}
		return false;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode t = new TreeNode(5);
		t.left = new TreeNode(1);
		t.left.left = new TreeNode(5);
		t.left.right = new TreeNode(5);
		t.right = new TreeNode(5);
		t.right.right  = new TreeNode(5);
		_250_CountUnivalueSubtrees cus = new _250_CountUnivalueSubtrees();
		System.out.println(cus.countUnivalSubtrees(t));
	}

}
