package backtracking;

import java.util.*;
public class _47_PermutationsII {
	// no duplicate for this one  
	// -> Arrays.sort()
	
	public List<List<Integer>> permutation(int[] nums){
		List<List<Integer>> res = new ArrayList<>();	
		Arrays.sort(nums);
		helper(nums, new ArrayList<>(), res, new boolean[nums.length]);
		
		return res;
		
	
	}
	public void helper(int[] nums, List<Integer> temp, List<List<Integer>> res,boolean[] used ) {
		if(temp.size() == nums.length) {
			res.add(new ArrayList<>(temp));
		}
		for(int i = 0; i < nums.length; i++) {
			
			if(used[i] || i > 0 && nums[i-1] == nums[i] && !used[i-1]) {
				continue;
			}
			
			used[i] = true;
			temp.add(nums[i]);
			helper(nums, temp, res,used);
			used[i] = false;
			temp.remove(temp.size()-1);
		}
		
	}
	
	
	
	public static void main(String[] args) {
		int[] nums = new int[]{1,1,3};
		_47_PermutationsII pm = new _47_PermutationsII();
		
		System.out.println(pm.permutation(nums));
	}
}
