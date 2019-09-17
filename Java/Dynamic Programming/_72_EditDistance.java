
public class _72_EditDistance {
	int[][] memo;
	// dfs 
	public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        memo = new int[m][n];
        return helper(word1, 0, word2, 0, memo);
        //return memo[m-1][n-1];
    }
	public int helper(String word1, int i , String word2, int j, int[][] memo) {
		int res = 0;
		if (word1.length() == i) return word2.length() - j;
		if (word2.length() == j) return word1.length() - i;
		if(memo[i][j]>0) return memo[i][j];
		if (word1.charAt(i) == word2.charAt(j)) {
			return helper(word1, i+1, word2, j+1, memo);
		}else {
			int insertCnt = helper(word1, i, word2, j+1, memo);
			int deleteCnt = helper(word1, i+1, word2, j, memo);
			int replaceCnt = helper(word1, i + 1, word2, j+1,memo);
			res = Math.min(insertCnt , Math.min(replaceCnt,deleteCnt))+1;
		}
		return memo[i][j] = res;
	}
	
	//DP
	public int minDistance2(String word1, String word2) {
		int m = word1.length(), n = word2.length();
		int[][] dp = new int[m+1][n+1];
		
		for (int i = 0; i <= m; ++i) dp[i][0] = i;
        for (int i = 0; i <= n; ++i) dp[0][i] = i;
		
		for(int i = 1; i <= m; ++i) {
			for(int j = 1; j <= n; ++j) {
				if(word1.charAt(i-1) == word2.charAt(j-1)) {
					dp[i][j] = dp[i-1][j-1];
				}else {
					dp[i][j] = Math.min(dp[i-1][j-1], Math.min(dp[i-1][j], dp[i][j-1]))+1;
				}
			}
		}
		return dp[m][n];
		
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String word1 = "horse", word2 = "ros";
		_72_EditDistance ed = new _72_EditDistance();
		System.out.println(ed.minDistance(word1, word2));
		System.out.println(ed.minDistance2(word1, word2));
	}

}
