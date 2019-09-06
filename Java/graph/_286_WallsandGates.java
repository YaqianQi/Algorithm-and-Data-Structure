package graph;

import java.util.Arrays;

public class _286_WallsandGates {
	public int[][] wallsAndGates(int[][] rooms) {
	        if(rooms == null || rooms.length == 0|| rooms[0].length == 0) return rooms;
	        
	        int m = rooms.length;
	        int n = rooms[0].length;
	        
	        for(int i = 0; i < m; i++) {
	        	for(int j = 0; j < n; j++) {
	        		if(rooms[i][j] == 0) {
	        			fill(rooms,i,j,0);
	        		}
	        	}
	        } 
	        return rooms;
	    }
	
	
	public void fill(int[][] rooms, int i , int j, int distance) {
		
		int m = rooms.length; 
		int n = rooms.length;
		if(i < 0 || j < 0 || i >= m|| j >= n || rooms[i][j] < distance) {
			return ;
		}
		rooms[i][j] = distance;
		fill(rooms, i , j - 1, distance + 1);
		fill(rooms, i , j + 1 , distance + 1);
		fill(rooms, i - 1 , j , distance + 1);
		fill(rooms, i + 1 , j , distance + 1);
	} 
	
	
	public static void main(String[] args) {
		
		int[][] rooms = {
				{1000 ,-1, 0 ,1000},
				{1000 ,1000, 1000 ,-1},
				{1000 ,-1, 1000 ,-1},
				{0 ,-1, 1000 ,1000}
				}; 
		
		_286_WallsandGates wg = new _286_WallsandGates();
		int[][] res = wg.wallsAndGates(rooms);
		
		for(int[] re : res) {
			System.out.println(Arrays.toString(re));
		}
	}

}
