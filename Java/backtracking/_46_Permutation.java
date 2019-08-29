package backtracking;
import java.util.*;


public class _46_Permutation {
	public List<List<Integer>> res = new ArrayList<>();
	
	public List<List<Integer>> permutate(int[] nums) {
		
		helper(nums, new ArrayList<>(), res);
		return res;
	}
	
	
	public void helper(int[] nums, List<Integer> temp, List<List<Integer>> res ) {
		if(temp.size() == nums.length) {
			res.add(new ArrayList<>(temp));
		}
		for(int i = 0; i < nums.length; i++) {
			if(temp.contains(nums[i])) continue;
			temp.add(nums[i]);
			helper(nums, temp, res);
			temp.remove(temp.size()-1);
		}
		
	}
	
	public static void main(String[] args) {
		int[] nums = new int[]{1,2,3};
		_46_Permutation pm = new _46_Permutation();
		//pm.permutate(nums);
		System.out.println(pm.permutate(nums));
	}
}
