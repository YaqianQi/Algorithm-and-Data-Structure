import java.util.*;

public class _377_CombinationSumIV {
	public List<List<Integer>> res = new ArrayList<>();

	public int combinationSum4(int[] nums, int target) {
	    HashMap<Integer, Integer> map = new HashMap<>();
		return helper(nums, target,map) ;
	
	} 
	public int helper(int[] nums, int target,HashMap<Integer, Integer> map) {
		if(target == 0) return 1;
		if (target < 0) return 0;
		int res= 0;
		if(map.containsKey(target)) {
			return map.get(target);
		}
		for(int i = 0; i < nums.length; i++) {
			res+= helper(nums, target - nums[i], map);
		}
		map.put(target, res);
		return res;
		
	}
	public int combinationSum4DP(int[] nums, int target) {
        
        int[] dp = new int[target+1];
        dp[0] = 1;
		for(int i = 1; i < dp.length; i++) {
			for (int num: nums) {
				if(i - num >= 0) {
					dp[i] += dp[i-num];
				}
				
			}
		}
		return dp[target];
	} 
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {1,2,3};
		int target = 4;
		
		_377_CombinationSumIV cs5 = new _377_CombinationSumIV();
		System.out.println(cs5.combinationSum4(nums, target));
		System.out.println(cs5.combinationSum4DP(nums, target));
	}

}
