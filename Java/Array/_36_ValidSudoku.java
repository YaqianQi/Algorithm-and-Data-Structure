import java.util.*;
public class _36_ValidSudoku {
	
	public boolean isValidSudoku(char[][] board) {
		for (int i = 0; i < 9; i++) {
			HashSet<Character> rows = new HashSet<>();
			HashSet<Character> cols = new HashSet<>();
			HashSet<Character> squares = new HashSet<>();
			for (int j = 0; j < 9; j++) {
				if (board[i][j] != '.' && !rows.add(board[i][j])) {
					return false;
				}
				if (board[j][i] != '.' && !cols.add(board[j][i])) {
					return false;
				}
				int rowIndex = 3 * (i / 3) + j / 3;
				int colIndex = 3 * (i % 3) + j % 3;
				if (board[rowIndex][colIndex]!= '.' && !squares.add(board[rowIndex][colIndex])) {
					return false;
				}	
			}
			
		}
		return true;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		char[][] board = new char[][]{
		 {'5','3','.','.','7','.','.','.','.'},
		 {'6','.','.','1','9','5','.','.','.'},
		 {'.','9','8','.','.','.','.','6','.'},
		 {'8','.','.','.','6','.','.','.','3'},
		 {'4','.','.','8','.','3','.','.','1'},
		 {'7','.','.','.','2','.','.','.','6'},
		 {'.','6','.','.','.','.','2','8','.'},
		 {'.','.','.','4','1','9','.','.','5'},
		 {'.','.','.','.','8','.','.','7','9'}};
		 
		 _36_ValidSudoku vs = new _36_ValidSudoku();
		 System.out.println(vs.isValidSudoku(board));
	}

}
