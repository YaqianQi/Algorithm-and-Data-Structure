package backtracking;
import java.util.*;
public class _90_SubsetsII {
	// return all possible subset without duplicates 
	public List<List<Integer>> subset(int[] nums){
		
		List<List<Integer>> res = new ArrayList<>();
		Arrays.sort(nums);
		helper(nums, new ArrayList<>(), 0, res);
		return res;
		
	}
	
	public void helper(int[] nums, List<Integer> temp, int start, List<List<Integer>> res) {
		res.add(new ArrayList<>(temp));
		for(int i = start; i < nums.length;i++) {
			if( i > start && nums[i-1]== nums[i]) {
				continue;
			}
			temp.add(nums[i]);
			helper(nums, temp, i+1, res);
			temp.remove(temp.size()-1);
			
			
		}
	}
	
	
	
	public static void main(String[] args) {
		int[] nums = new int[] {1,1,2};
		_90_SubsetsII sb = new _90_SubsetsII();
		System.out.println(sb.subset(nums));
	}

}
