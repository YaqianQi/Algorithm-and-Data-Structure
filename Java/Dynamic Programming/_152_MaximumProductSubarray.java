
public class _152_MaximumProductSubarray {
	public int maxProduct(int[] nums) { 
		int[] max = new int [nums.length]; 
		int[] min = new int [nums.length];
		max[0] = nums[0];
		min[0] = nums[0];
		int res = nums[0];
		for (int i = 1; i < nums.length; i++) {
			if(nums[i] > 0) {
				max[i] = Math.max(max[i-1] * nums[i], nums[i]);
				min[i] = Math.min(min[i-1] * nums[i], nums[i]);
			}else {
				max[i] = Math.max(min[i-1] * nums[i], nums[i]);
				min[i] = Math.min(max[i-1] * nums[i], nums[i]);
			}
			res = Math.max(res, max[i]);
			
		}
		return res;
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {2,3,-2,4};
		_152_MaximumProductSubarray mps = new _152_MaximumProductSubarray();
		System.out.println(mps.maxProduct(nums));
	}

}
