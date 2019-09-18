
public class _132_PalindromePartitioningII {
	public int minCut(String s) {
	    int n = s.length();    
		boolean[][] p = new boolean[n][n] ; 
		int[] dp = new int[n];
		for (int i = 0; i < n; i++) {
            dp[i] = i;
            for (int j = 0; j <= i; j++) {
                if (s.charAt(i) == s.charAt(j) && (i - j < 2 || p[j + 1][i - 1])) {
                    p[j][i] = true;
                    dp[i] = (j == 0) ? 0 : Math.min(dp[i], dp[j - 1] + 1);
                }
            }
        }
        return dp[n - 1];
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s= "abbab";
		_132_PalindromePartitioningII pp = new _132_PalindromePartitioningII();
		System.out.println(pp.minCut(s));
	}

}
