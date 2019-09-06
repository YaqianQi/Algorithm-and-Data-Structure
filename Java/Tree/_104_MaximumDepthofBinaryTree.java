
public class _104_MaximumDepthofBinaryTree {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        int left = maxDepth(root.left) + 1;
        int right = maxDepth(root.right) + 1;
        return Math.max(left, right);
    }
    public static void main(String[] args) {
    	TreeNode t = new TreeNode(2);
    	t.left = new TreeNode(1);
    	t.right = new TreeNode(3);
    	t.right.left = new TreeNode(1);
    	t.right.right = new TreeNode(4);
    	_104_MaximumDepthofBinaryTree mdb = new _104_MaximumDepthofBinaryTree();
    	System.out.println(mdb.maxDepth(t));
    }
}
