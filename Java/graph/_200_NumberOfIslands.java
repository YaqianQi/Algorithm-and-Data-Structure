package graph;

public class _200_NumberOfIslands {
	  
	private int rows;
	private int cols;
	public int numIslands(char[][] grid) {
		if (null ==grid || grid.length<=0 ||grid[0].length <=0) return 0;
        rows = grid.length;
        cols = grid[0].length;
        int count = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] =='1'){
                    count++;
                    dfsSearch(grid,i,j);
                }
            }
        }
        return count;
    }
	  
	  public void dfsSearch(char[][] grid, int i , int j) {
		  if(i < 0 || j < 0 || i >= rows|| j >= cols|| grid[i][j] == '0') return;
		  grid[i][j] ='0';
		  dfsSearch(grid, i+1, j);
		  dfsSearch(grid,i-1,j);
		  dfsSearch(grid, i, j+ 1);
		  dfsSearch(grid,i,j-1);	  
	  }
	
	
	
	
	
	public static void main(String[] args) {
		
		char [][] grid = {
                {'1','1','1','1','0' },
                {'1','1','0','1','0'},
                {'1','1','0','0','0'},
                {'0','0','0','0','0'}
        };
		_200_NumberOfIslands nfi= new _200_NumberOfIslands();
		System.out.println(nfi.numIslands(grid));
	}
}
