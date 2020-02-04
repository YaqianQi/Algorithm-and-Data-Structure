package graph;
import java.util.*;
public class _505_TheMazeII {
	public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        int m = maze.length;
        int n = maze[0].length;
        int[][] dist = new int[m][n];
        for (int[] d:dist){
            Arrays.fill(d,Integer.MAX_VALUE);
        }
        dist[start[0]][start[1]] = 0;
        helper(maze, start[0], start[1], destination,dist);
        int res = dist[destination[0]][destination[1]];
        return (res == Integer.MAX_VALUE) ? -1 : res;
    }
    
    public void helper(int[][] maze, int row, int col, int[] destination,int[][] dist){
        //if (row < 0 || row > maze.length || col < 0 ||col > maze[0].length|| visited[row][col]) return ;
        if (row == destination[0] && col == destination[1]) return ;
        int[][] dirs = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
        
        for (int[] dir: dirs){
            int x = row , y = col;
            int dis = dist[x][y];
            while(x >=0 && x < maze.length && y >=0 && y< maze[0].length && maze[x][y]==0 ){
                x += dir[0];
                y += dir[1];
                ++dis;
            }
            x -= dir[0];
            y -= dir[1];
            --dis;
            if (dis < dist[x][y]){
                dist[x][y] = dis;
                helper(maze, x, y, destination,dist);
            }
           
        }
    
    } 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] maze = new int[][]
			{{0,0,1,0,0},{0,0,0,0,0},{0,0,0,1,0},{1,1,0,1,1},{0,0,0,0,0}}
		;
		int[] start = new int[] {0,4};
		int[] destination = new int[] {4,4};
		_505_TheMazeII tm = new _505_TheMazeII();
		int res = tm.shortestDistance(maze, start, destination);
		System.out.println(res);
	}
}
