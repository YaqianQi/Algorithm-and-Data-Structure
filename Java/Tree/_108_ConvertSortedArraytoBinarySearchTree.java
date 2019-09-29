
public class _108_ConvertSortedArraytoBinarySearchTree {
	
	public TreeNode sortedArrayToBST(int[] nums) {
		if (nums == null || nums.length == 0) return null;
		return helper(nums, 0, nums.length - 1);
	    }
	
	TreeNode helper(int[] nums, int left, int right) {
		if (right < left) {return null;}
		int mid = (right - left)/2 + left;
		TreeNode res = new TreeNode(nums[mid]);
		res.left = helper(nums, left, mid - 1);
		res.right = helper(nums, right, mid - 1);
		return res;
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {-10, -3,0, 5,9};
		_108_ConvertSortedArraytoBinarySearchTree csab = new _108_ConvertSortedArraytoBinarySearchTree();
		
		System.out.println(csab.sortedArrayToBST(nums).val);
	}

}
