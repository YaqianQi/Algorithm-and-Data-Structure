package graph;

public class _490_TheMaze {
	public boolean hasPath(int[][] maze, int[] start, int[] destination) {
		int m = maze.length;
		int n = maze[0].length;
		boolean[][] visited =  new boolean[m][n];
		return dfs(maze, visited, start, destination);
	}
	
	private boolean dfs(int[][] maze, boolean[][] visited,int[] start, int[] destination) {
		int row = start[0], col = start[1];
		if(row < 0|| row >= maze.length || col < 0 || col >= maze[0].length || visited[row][col]) {
			return false;
		}
		visited[row][col] = true;
		if(row == destination[0] && col == destination[1]) {
			return true;
		}
		
		int[][] dirs = new int[][] {{1,0},{-1,0},{0,1},{0,-1}};
		for(int i = 0 ; i < 4 ;i++) {
			int x = row, y = col;
			while(x >= 0 && x<maze.length && y >= 0 && y < maze[0].length && maze[x][y] !=1) {
				x += dirs[i][0];
				y += dirs[i][1];
			}
			x -= dirs[i][0];
			y -= dirs[i][1];
			if(dfs(maze,visited, new int[]{x,y}, destination)) return true;
		}
		
		
		return false;
	}
	
	
	public static void main(String[] args) {
        String mazeStr = "0 0 1 0 0\n" +
                "0 0 0 0 0\n" +
                "0 0 0 1 0\n" +
                "1 1 0 1 1\n" +
                "0 0 0 0 0";

        int[][] maze = MazeUtils.readMaze(mazeStr, 5, 5);
        //ArrayUtils.printArray(maze);

        _490_TheMaze mz = new _490_TheMaze();
        boolean b = mz.hasPath(maze, new int[]{0, 4}, new int[]{3, 2});
        System.out.println(b);
    }
}
