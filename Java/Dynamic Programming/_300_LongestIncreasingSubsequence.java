import java.util.Arrays;

public class _300_LongestIncreasingSubsequence {
	 public int lengthOfLIS(int[] nums) {
		 if (nums == null || nums.length == 0) {
	            return 0;
	        }
		 
		 int[] dp = new int[nums.length];
		 Arrays.fill(dp, 1);
		 
		 for(int i = 0; i < nums.length; i++) {
			 for(int j = 0; j < i; j++) {
				 if (nums[i]>nums[j]) {
					 dp[i] = Math.max(dp[i], dp[j] + 1);
				 } 
			 }
		 }
		 int res = dp[0];
		 for(int i = 1; i < dp.length ; i++) {
			 res = Math.max(res, dp[i]);
		 }
		 return res;

	  }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {10,9,2,5,3,7,101,18};
		_300_LongestIncreasingSubsequence lis = new _300_LongestIncreasingSubsequence();
		System.out.println(lis.lengthOfLIS(nums));
	}

}
