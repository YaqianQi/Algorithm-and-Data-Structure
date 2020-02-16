
public class _5340_CountNegativeNumbersinaSortedMatrix {
	public int countNegatives(int[][] grid) {
		int m = grid.length;
		int n = grid[0].length;
		int res = 0;
		for(int i = 0; i < m; i++) {
			for (int j = 0; j < n;j++) {
				if (grid[i][j]<0)res++;
			}
		}
		return res;
    
	}
	public int countNegatives2(int[][] grid) {
        int m = grid.length;
		int n = grid[0].length;
		int res = 0;
		for (int j = n -1, i  = 0 ; j >= 0; j--) {
			while(i + 1 < m && grid[i][j]>=0) {
				i++;
			}
			if(grid[i][j]<0) {
                res += m - i;
            }
		}
		return res;
    }
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] grid = new int[][]{{1,-1},{-1,-1}};
		_5340_CountNegativeNumbersinaSortedMatrix cn = new _5340_CountNegativeNumbersinaSortedMatrix();
		System.out.println(cn.countNegatives2(grid));
	}

}
