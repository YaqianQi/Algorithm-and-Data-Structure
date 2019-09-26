
public class _337_HouseRobberIII {
	// 不能头相邻房间的钱 ， 否则会引起警报
	// o(n)
	/*
	public int rob(TreeNode root) {
		return helper(root);
	}
	int helper(TreeNode root) {
		if (root == null) return 0;
		//int res = 0;
		int val = 0;
		if (root.left != null) {
			val += rob(root.left.left) + rob(root.right.right);
		}
		if (root.right != null) {
			val += rob(root.right.left) + rob(root.right.right);
		}
		return Math.max(val+ root.val, rob(root.left) + rob(root.right));
	}*/
	
	public int rob(TreeNode root) {
		if (root == null) return 0;
		//int res = 0;
		int val = 0;
		if (root.left != null) {
			val += rob(root.left.left) + rob(root.left.right);
		}
		if (root.right != null) {
			val += rob(root.right.left) + rob(root.right.right);
		}
		return Math.max(val+ root.val, rob(root.left) + rob(root.right));
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode t = new TreeNode(3);
		t.left = new TreeNode(2);
		t.left.right = new TreeNode(3);
		t.right = new TreeNode(3);
		t.right.left = new TreeNode(1);
		_337_HouseRobberIII  hr3 = new _337_HouseRobberIII ();
		System.out.println(hr3.rob(t));
		
	}

}
