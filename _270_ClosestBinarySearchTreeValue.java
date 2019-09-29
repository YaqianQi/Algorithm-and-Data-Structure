
public class _270_ClosestBinarySearchTreeValue {
	
	 public int closestValue(TreeNode root, double target) {
		 int res = root.val;
		 while(root!=null) {
			 if(Math.abs(res - target )> Math.abs(root.val - target)) {
				 res = root.val;
			 }
			 root = root.val > target? root.left : root.right;
		 }
		return res;
		 
	 }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode root = new TreeNode(4);
		root.left = new TreeNode(2);
		root.right = new TreeNode(5);
		root.left.right = new TreeNode(3);
		double target = 3.444;
		_270_ClosestBinarySearchTreeValue cbst = new _270_ClosestBinarySearchTreeValue();
		System.out.println(cbst.closestValue(root, target));
	}

}
