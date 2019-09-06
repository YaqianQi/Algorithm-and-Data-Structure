
public class _230_KthSmallestElementinBST {
	int count; 
	int res;
	public int kthSmallest(TreeNode root, int k) {
		count = k;
		res = 0;
	       
	     helper(root);
	        
	     return res;
	    }
	
	public void helper(TreeNode root) {
		if (root == null) return ;
		helper(root.left);
		count -- ;
		if(count == 0) res = root.val;
		helper(root.right);
	}
	
	public static void printTreeNode(TreeNode root) {
		if (root == null) return ;
		printTreeNode(root.left);
		System.out.println(root.val);
		printTreeNode(root.right);
	}	
	public static void main(String[] args) {
		TreeNode t1 = new TreeNode(3);
		t1.left = new TreeNode(1);
		t1.right = new TreeNode(4);
		t1.left.right = new TreeNode(2);
		//printTreeNode(t1);
		_230_KthSmallestElementinBST kse = new _230_KthSmallestElementinBST();
		System.out.println(kse.kthSmallest(t1, 1));
	}

}
