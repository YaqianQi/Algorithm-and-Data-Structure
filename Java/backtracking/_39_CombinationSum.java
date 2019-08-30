package backtracking;
import java.util.*;
public class _39_CombinationSum {
	
	public List<List<Integer>> combinationSum(int[] candidates, int target) {
	        List<List<Integer>> res = new ArrayList<>();
	        
	        helper(candidates, target, res, new ArrayList<>(),0);
	        return res;
	    }
	
	public void helper(int[] candidates, int target,List<List<Integer>> res, List<Integer> temp,int start) {
		if(target<0) return ;
		if(target == 0) {
			res.add(new ArrayList<>(temp)) ;
			return ;
		}
		for(int i = start ; i < candidates.length; i ++ ) {
			temp.add(candidates[i]);
			helper(candidates, target- candidates[i], res,temp ,i);
			temp.remove(temp.size()-1);
		}
		
		
	}
	public static void main(String[] args) {
		int[] candidates = new int[] {2,3,6,7};
		int target = 7 ;
		
		_39_CombinationSum cs = new _39_CombinationSum();
		System.out.println(cs.combinationSum(candidates, target));
	}
	
	

}
