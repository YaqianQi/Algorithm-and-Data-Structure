import java.util.*;
public class _296_BestMeetingPoint {
	 public int minTotalDistance(int[][] grid) {
	        List<Integer> rows = new ArrayList<>();
	        List<Integer> cols = new ArrayList<>();
	        for (int i = 0; i < grid.length; i++){
	            for (int j = 0; j < grid[0].length; j++){
	                if (grid[i][j] == 1){
	                    rows.add(i);
	                    cols.add(j);
	                }
	            }
	        }
	        return count(rows) + count(cols);
	    }
	    public int count(List<Integer> lst){
	        Collections.sort(lst);
	        int i = 0; 
	        int j = lst.size()-1;
	        int res = 0;
	        while(i < j){
	        	
	            res += lst.get(j--) - lst.get(i++);
	        }
	        return res;
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] grid = new int[][]{{1,0,0,0,1},{0,0,0,0,0},{0,0,1,0,0}};
		_296_BestMeetingPoint bmp = new _296_BestMeetingPoint();
		System.out.println(bmp.minTotalDistance(grid));
	}

}
