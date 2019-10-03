
public class _115_DistinctSubsequences {
	/*s->T  S
	 *  	T 	Ø r a b b b i t
			Ø 1 1 1 1 1 1 1 1
			r 0 1 1 1 1 1 1 1
			a 0 0 1 1 1 1 1 1
			b 0 0 0 1 2 3 3 3
			b 0 0 0 0 1 3 3 3
			i 0 0 0 0 0 0 3 3
			t 0 0 0 0 0 0 0 3 
	 * */
	
	public int numDistinct(String s, String t) {
		int m = s.length();
		int n = t.length();
		int[][] dp = new int[n+1][m+1];
		
		for (int j = 0; j <= m; j++) dp[0][j] = 1;
		
		for (int i = 1; i <= n; ++i) {
            		for (int j = 1; j <= m; ++j) {
             
                		dp[i][j] = dp[i][j - 1] + (t.charAt(i-1) == s.charAt(j-1) ? dp[i - 1][j - 1] : 0);
            }
        }
		 return dp[n][m];
		 
	
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "rabbbit", t = "rabbit";
		_115_DistinctSubsequences ds = new _115_DistinctSubsequences();
		System.out.println(ds.numDistinct(s, t));
	}

}
