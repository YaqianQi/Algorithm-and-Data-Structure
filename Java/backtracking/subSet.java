package backtracking;
import java.util.*;
public class subSet {
	public static List<List<Integer>> findSubSet(int[] nums) {
		List<List<Integer>> res = new ArrayList<>();
		if(nums == null || nums.length == 0) {
			return res;
		}
		
		Arrays.parallelSort(nums);
		List<Integer> temp = new ArrayList<>();
		helper(nums, res, temp, 0);
		return res;
	}
	
	public static void helper(int[] nums, List<List<Integer>> res, List<Integer> subset, int startIdx) {
		res.add(new ArrayList<>(subset));
		
		for(int i = startIdx; i < nums.length ; i++) {
			subset.add(nums[i]);
			helper(nums, res,subset,i+1);
			subset.remove(subset.size() - 1);
		}
		
		
	}
	
	
	public static void main(String [] args) {
		int[] nums  = {1,2,3};
		
		List<List<Integer>> res =  findSubSet(nums);
		for(List<Integer> res2 : res) {
			System.out.println(res2);
		}
		
		
 	}
	

}
