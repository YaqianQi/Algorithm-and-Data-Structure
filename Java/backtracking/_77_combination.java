package backtracking;
import java.util.*;

public class _77_combination {
	//List<List<Integer>> res;
	public List<List<Integer>> combination(int n , int k){
		
		List<List<Integer>> res = new ArrayList<>();
		
		helper(res, new ArrayList<>(), n, k, 1);
		
		return res;
	}

	public void helper(List<List<Integer>> res, List<Integer> list, int n, int k , int start) {
		if (k == 0) {
			res.add(new ArrayList<>(list));
		}
		for(int i = start; i <= n ;i++) {
			list.add(i);
			helper(res, list, n , k- 1, i+1);
			list.remove(list.size()-1);
		}
	}
	
	
	
	
	public static void main(String[] args) {
		
		_77_combination cb = new _77_combination();
		System.out.println(cb.combination(4, 2));
		
	}

}
