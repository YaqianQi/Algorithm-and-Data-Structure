
public class _53_MaximumSubarray {
	
	 public int maxSubArray(int[] nums) {
		 int temp = nums[0];
		 int res = nums[0];

		 for(int i = 1; i < nums.length ;i++) {
			 temp = Math.max(nums[i]+temp, nums[i]);
			 res = Math.max(temp, res);	 
		 }
		 return res;
	       
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
		_53_MaximumSubarray ms = new _53_MaximumSubarray();
		System.out.println(ms.maxSubArray(nums));
	}

}
