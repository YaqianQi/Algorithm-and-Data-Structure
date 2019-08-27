package priorityQueue;
import java.util.*;

public class _56_mergeIntervals {
	
	public int[][] merge(int[][] intervals){
		
		
		if(intervals == null || intervals.length == 0) {
			return new int[][] {};
		}
		
		Arrays.sort(intervals,(a,b)->(a[0]-b[0]));
		List<int[]> res = new ArrayList<>();
		int start = intervals[0][0];
		int end = intervals[0][1];
		
		for(int[] interval: intervals) {
			if(interval[0]<= end) {
				end = Math.max(end, interval[1]);
			}else {
				res.add(new int[]{start, end });
				start = interval[0];
				end = interval[1];
			}
		}
		res.add(new int[] {start, end});
		return res.toArray(new int[][]{});
		
	}
	
	// arrays.sort() 
	
	public static void main(String[] args) {
		
		int[][] intervals = new int[][] {{1,5},{4,3}};
		_56_mergeIntervals mi = new _56_mergeIntervals();
		System.out.println(mi.merge(intervals));
		
	}
}
