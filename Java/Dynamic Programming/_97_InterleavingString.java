
public class _97_InterleavingString {
	// Left and right is true then continue 
	 public boolean isInterleave(String s1, String s2, String s3) {
	        int n = s1.length();
	        int m = s2.length();
	        int k = s3.length();
	        if (m + n!=k ) return false;
	        boolean[][] dp = new boolean[m+1][n+1];
	        dp[0][0] = true;
	        
	        if ((n == 0 && m!=k) || (m == 0 && n!=k)) return false;
	        for(int i = 1; i  <= m; i++) {
	        	dp[i][0] = dp[i-1][0] && s1.charAt(i-1) == s3.charAt(i-1); 
	        }
	        for(int j = 1; j  <= n; j++) {
	        	dp[0][j] = dp[0][j-1] && s2.charAt(j-1) == s3.charAt(j-1); 
	        }
	        
	        
	        for(int i = 1; i <= m; i++) {
	        	for(int j = 1; j <= n; j++) {
	        		dp[i][j] = (dp[i-1][j] && s1.charAt(i-1) == s3.charAt(i+j-1)) || (dp[i][j-1] && s2.charAt(j-1) == s3.charAt(i+j-1));
	        	}
	        }
	        return dp[m][n];
	    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac";
		_97_InterleavingString ils = new _97_InterleavingString();
		System.out.println(ils.isInterleave(s1, s2, s3));
	}

}
