
public class _333_LargestBSTSubtree {
    //所谓二分搜索树就是满足左<根<右的二分树
	// binary tree, left < root < right 
	//1. postorder
	//2. BST
	//3. decide 
    public int largestBSTSubtree(TreeNode root) {
    	if (root == null) return 0;
        if (isValid(root, Integer.MIN_VALUE, Integer.MAX_VALUE)) return count(root);
        return Math.max(largestBSTSubtree(root.left), largestBSTSubtree(root.right));
    }
    boolean isValid(TreeNode root, int mn, int mx) {
        if (root == null) return true;
        if (root.val <= mn || root.val >= mx) return false;
        return isValid(root.left, mn, root.val) && isValid(root.right, root.val, mx);
    }
    public int count(TreeNode root) {
    	if (root == null) return 0;
        return count(root.left) + count(root.right) + 1;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode root = new TreeNode(10);
		root.left = new TreeNode(5);
		root.left.left = new TreeNode(1);
		root.left.right = new TreeNode(8);
		root.right = new TreeNode(15);
		root.right.right = new TreeNode(7);
		_333_LargestBSTSubtree lbs = new _333_LargestBSTSubtree();
		System.out.println(lbs.largestBSTSubtree(root));
	}

}
