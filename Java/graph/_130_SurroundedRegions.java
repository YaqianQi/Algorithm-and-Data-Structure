package graph;

import java.util.Arrays;

public class _130_SurroundedRegions {
	
	// check boundary first and then change the O inside 
	// bfs,dfs can both work 
	public char[][] solve(char[][] board) {
		
		int n = board.length-1; 
		int m = board[0].length-1;
		// for 1st row and last row 
		for(int i = 0 ; i <= n ; i ++) {
			if (board[0][i] == 'O') {
				dfs(board, 0 , i);
			}
			if (board[m][i] == 'O') {
				dfs(board, m , i);
			}
		}
		// for 1st col and last col 
		for(int i = 0 ; i <= m ; i ++) {
			if (board[i][0] == 'O') {
				dfs(board, i , 0);
			}
			if (board[i][n] == 'O') {
				dfs(board, i , n);
			}
		}
		
		
		for(int i = 0; i <= m; i++) {
			for(int j = 0; j <= n ; j++) {
				if (board[i][j] == 'O') {
					board[i][j] = 'X';
				}else if (board[i][j] == '1') {
					board[i][j] = 'O'; 
				}
			}
		}
		return board;
		
	}
	
	public void dfs(char[][] board, int i , int j) {
		if ( i < 0|| j < 0 || i >= board.length || j >= board[0].length|| board[i][j] != 'O' ) return ;
		
		board[i][j] = '1';
		dfs(board, i, j-1);
		dfs(board, i , j+1);
		dfs(board, i-1 , j);
		dfs(board, i+1 , j);
	}
	
	public static void main(String[] args) {
		char[][] board = {
						{'X' ,'X', 'X' ,'X'},
						{'X' ,'O', 'O' ,'X'},
						{'X' ,'X', 'X' ,'X'},
						{'X' ,'O', 'X' ,'X'}
						}; 
		
		_130_SurroundedRegions sr = new _130_SurroundedRegions();
		sr.solve(board);		
		System.out.println(Arrays.deepToString(sr.solve(board)));
		
	}

}
