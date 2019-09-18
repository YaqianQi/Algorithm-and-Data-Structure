
public class _221_MaximalSquare {
	// 
	public int maximalSquare(char[][] matrix) {
		int m = matrix.length;
		int n = matrix[0].length;
		int[][] dp = new int[m][n];
		int res = 0;
		
		for(int i = 0; i < m; i++) {
			for(int j = 0; j < n; j++) {
				if (i ==0 || j == 0 ) dp[i][j] = matrix[i][j] -'0';
				else if (matrix[i][j] == '1') {
					dp[i][j] = Math.min(dp[i-1][j-1],Math.min(dp[i-1][j], dp[i][j-1]))+1;
					
				}
				res =  Math. max(res, dp[i][j]); 
			}
		}
		return res*res;
	}
  
    	
    
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		char[][] matrix = {{'1', '0' ,'1' ,'0' ,'0'},
						{'1' , '0' ,'1' ,'1' ,'1'},
						{'1' ,'1', '1', '1', '1'},
						{'1', '0' ,'0' ,'1' ,'0'}};
		
		_221_MaximalSquare ms = new _221_MaximalSquare();
		System.out.println(ms.maximalSquare(matrix));
	}

}
