
public class _129_SumRoottoLeafNumbers {
	 public int sumNumbers(TreeNode root) {
	        return helper(root, 0);
	    }
	 int helper(TreeNode root, int sum) {
		 if (root == null) return 0;
		 sum = sum * 10 + root.val;
		 if (root.left == null && root.right == null) return sum;
		 return helper(root.left, sum) + helper(root.right, sum);
	 }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode t = new TreeNode(1);
		t.left = new TreeNode(2);
		t.right = new TreeNode(3);
		_129_SumRoottoLeafNumbers sln = new _129_SumRoottoLeafNumbers();
		System.out.println(sln.sumNumbers(t));
	}

}
