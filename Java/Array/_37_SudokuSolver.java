import java.util.HashSet;

public class _37_SudokuSolver {
	
	public void printNums(char[][] board) {
		for (char[] b : board) {
			
			System.out.println(b);
		}
	}
	public void solveSudoku(char[][] board) {
        helper(board);
        printNums(board);
    }

    private boolean helper(char[][] board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    continue;
                }

                for (char k = '1'; k <= '9'; k++) {
                    if (isValid(board, i, j, k)) {
                        board[i][j] = k;
                        if (helper(board)) {
                            return true;
                        }
                        board[i][j] = '.';
                    }
                }
                return false;
            }
        }

        return true; //return true if all cells are checked
    }

    private boolean isValid(char[][] board, int row, int col, char c) {
        for (int i = 0; i < 9; i++) {
            if (board[i][col] != '.' && board[i][col] == c) {
                return false;
            }

            if (board[row][i] != '.' && board[row][i] == c) {
                return false;
            }

            if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] != '.'
                    &&
                    board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == c) {
                return false;
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
		 
		 _37_SudokuSolver vs = new _37_SudokuSolver();
		 
		 vs.solveSudoku(board);
	}
}
