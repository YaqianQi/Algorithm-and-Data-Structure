package backtracking;
import java.util.*;
public class _216_CombinationSumIII {
	 public List<List<Integer>> combinationSum3(int k, int n) {
		 List<List<Integer>> res = new ArrayList<>();
		 helper(k, n, new ArrayList<>(), res, 0);
		 return res;
	    }
	
	 public void helper(int k ,  int n , List<Integer> temp, List<List<Integer>> res, int start) {
		 if (n < 0) return ;
		 if(k == 0 && n == 0) {
			 res.add(new ArrayList<>(temp));
			 return ;
		 }
		 
		 for(int i = start ; i <= 9; i++) {
			 temp.add(i);
			 helper(k - 1, n - i, temp, res, i+1);
			 temp.remove(temp.size() - 1);
		 }
		 
	 }
	
	
	
	
	public static void main(String[] args) {
		int k = 3;
		int n = 9;
		_216_CombinationSumIII cs = new _216_CombinationSumIII();
		System.out.println(cs.combinationSum3(k, n));
		
	}

}
