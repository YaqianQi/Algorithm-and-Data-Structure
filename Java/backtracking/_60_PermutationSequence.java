package backtracking;
import java.util.*;


public class _60_PermutationSequence {
	// time: o(n)
	// space: o(n)
	
	public String permuationSequence(int n, int k){
		List<Integer> res = new ArrayList<>();
		for(int i = 1; i <= n; i++) {
			res.add(i);
		}
		int[] fact = new int[n];
		
		fact[0] = 1;
		for(int i = 1; i< n ;i++) {
			fact[i] =   i * fact[i-1];
		}
		k = k- 1;
		
		
		StringBuilder sb = new StringBuilder();
		for(int i = n; i > 0;i--) {
			int  index = k / fact[i-1];
			k = k % fact[i-1];
			sb.append(res.get(index));
			res.remove(index);
			
		}
		
		return sb.toString();
	}
	
	
	
	
	public static void main(String[] args) {
		int[] nums = new int[]{1,1,3};
		_60_PermutationSequence ps = new _60_PermutationSequence();
		
		System.out.println(ps.permuationSequence(4,17));
	}
}
