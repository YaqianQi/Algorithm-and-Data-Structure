import java.util.Arrays;

public class _64_MinimumPathSum {
	
	 public int minPathSum(int[][] grid) {
	        int m = grid.length;
	        int n = grid[0].length;
	        int[][] dp = new int[m+1][n+1];
	        dp[0][0] = grid[0][0];
	        for(int i = 1; i < m; i++) {
	        	dp[i][0] = grid[i][0] + dp[i-1][0];
	        }
	        for(int j = 1; j < n; j++) {
	        	dp[0][j] = grid[0][j] + dp[0][j-1];
	        }
	        for(int i = 1; i < m; i++) {
	        	for(int j = 1; j < n; j++) {
	        		dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
	        	}
	        }
	        return dp[m-1][n-1];
	 }
	 
	 public int minPathSumOpt(int[][] grid) {
	        int m = grid.length;
	        int n = grid[0].length;
	        int[] dp = new int[n+1];
	        Arrays.fill(dp, Integer.MAX_VALUE);
	        dp[0] = 0;
	        
	        for(int i = 0; i < m; i++) {
	        	for(int j = 0; j < n; j++) {
	        		if (j == 0) dp[j] += grid[i][j]; 
	        		else dp[j] = Math.min(dp[j-1], dp[j]) + grid[i][j];
	        	}
	        }
	        return dp[n-1];
	 }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] grid = {{1,3,1},
						{1,5,1},
						{4,2,1}
						};
		
		_64_MinimumPathSum mps = new _64_MinimumPathSum();
		System.out.println(mps.minPathSum(grid));
		System.out.println(mps.minPathSumOpt(grid));
	}

}
