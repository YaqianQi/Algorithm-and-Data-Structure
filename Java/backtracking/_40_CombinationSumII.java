package backtracking;
import java.util.*;
public class _40_CombinationSumII {
	
	public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(candidates);
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
		if (i != start && candidates[i] == candidates[i-1]) continue;
		temp.add(candidates[i]);
		helper(candidates, target- candidates[i], res,temp ,i+1);
		temp.remove(temp.size()-1);
	}
	
	
}
	
	
	public static void main(String[] args) {
		int[] candidates = new int[] {10,1,2,7,6,1,5};
		int target = 8 ;
		
		_40_CombinationSumII cs = new _40_CombinationSumII();
		System.out.println(cs.combinationSum2(candidates, target));
	}
	
}
