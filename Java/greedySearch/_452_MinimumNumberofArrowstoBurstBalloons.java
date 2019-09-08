package greedySearch;

import java.util.Arrays;

public class _452_MinimumNumberofArrowstoBurstBalloons {
	public int findMinArrowShots(int[][] points) {
		if(points == null || points.length == 0) return 0;
	        Arrays.sort(points,(a,b)->(a[1]- b[1]));
	        int end = points[0][1];
	        int res = 1;
	        for(int i = 1; i < points.length; i++) {
	        	if (points[i][0]<= end) {
	        		continue;
	        	}
	        	res++;
        		end =points[i][1];
	        	}
	        return res;
	    }
	public int findMinArrowShots2(int[][] points) {
		if(points == null || points.length == 0) return 0;
	        Arrays.sort(points,(a,b)->(a[0]- b[0]));
	        int end = points[0][1];
	        int res = 1;
	        for(int i = 1; i < points.length; i++) {
	        	if (points[i][0] > end) {
		        	res++;
	        		end =points[i][1];
	        	}else {
	        		end = Math.min(end, points[i][1]);
	        	}
	        	}
	        return res;
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] points = {{10,16}, {2,8}, 
		                      {1,6}, {7,12}};
		_452_MinimumNumberofArrowstoBurstBalloons abb = new _452_MinimumNumberofArrowstoBurstBalloons();
		System.out.print(abb.findMinArrowShots(points));
		System.out.print(abb.findMinArrowShots2(points));
	}

}
