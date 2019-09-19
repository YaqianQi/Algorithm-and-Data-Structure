
public class _63_UniquePathsII {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[][] dp = new int[m+1][n+1];
        dp[0][1] = 1;
        for(int i = 1; i <= m; i++) {
        	for(int j = 1; j <= n; j++) {
        		if (obstacleGrid[i-1][j-1] == 1) continue;
        		dp[i][j] = dp[i-1][j] + dp[i][j-1]; 
        	}
        }
        return dp[m][n];
    
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] obstacleGrid = {
							  {0,0,0},
							  {0,1,0},
							  {0,0,0}};
		_63_UniquePathsII up = new _63_UniquePathsII();
		System.out.println(up.uniquePathsWithObstacles(obstacleGrid));
	}

}
