package backtracking;

import java.util.ArrayList;
import java.util.List;

public class _78_Subsets {
	List<List<Integer>> res= new ArrayList<>();
	public List<List<Integer>> subsets(int[] nums) {
		List<Integer> temp = new ArrayList<>();
		helper(nums, 0, temp);
	return res;
	}
	
	public void helper(int[] nums, int start, List<Integer> temp) {
		res.add(new ArrayList<>(temp));
		for(int i = start; i < nums.length; i++) {
			temp.add(nums[i]);
			helper(nums, i+1, temp);
			temp.remove(temp.size()-1);
		}
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {1,2,3};
		
		 _78_Subsets sb = new  _78_Subsets();
		 System.out.println(sb.subsets(nums));
	}

}
