package priorityQueue;
import java.util.*;

public class _253_meetingRoomsII {
	
	 class Interval{
	        int start; 
	        int end; 
	        int room;
	        public Interval(int start, int end){
	            this.start = start; 
	            this.end = end;
	            this.room = -1;
	        }
	    }
	    
	    
	    public int minMeetingRooms(int[][] intervals) {
	        if(intervals.length == 0) return 0;
	        List<Interval> a = new ArrayList<>();
	        for (int[] interval :
	                intervals) {
	            a.add(new Interval(interval[0], interval[1]));
	        }
	        Collections.sort(a, new Comparator<Interval>() {
	            @Override
	            public int compare(Interval o1, Interval o2) {
	                return o1.start - o2.start;
	            }
	        });

	        Queue<Interval> q = new PriorityQueue<>(new Comparator<Interval>() {
	            @Override
	            public int compare(Interval o1, Interval o2) {
	                return o1.end - o2.end;
	            }
	        });
	        
	        
	        
	        
	        for(Interval interval: a){
	            if(q.size() == 0){
	                q.add(interval);
	            }else{
	                int end = q.peek().end;
	                if(interval.start >= end){
	                    q.poll();
	                    q.add(interval);
	                }else{
	                    q.add(interval);
	                }
	            }
	        }
	        return q.size();
	      
	    }
	
	
	public int minMeetingRooms(int[][] intervals) {
	    Arrays.sort(intervals, Comparator.comparing((int[] itv) -> itv[0]));

	    PriorityQueue<Integer> heap = new PriorityQueue<>();
	    int count = 0;
	    for (int[] itv : intervals) {
		if (heap.isEmpty()) {
		    count++;
		    heap.offer(itv[1]);
		} else {
		    if (itv[0] >= heap.peek()) {
			heap.poll();
		    } else {
			count++;
		    }

		    heap.offer(itv[1]);
		}
	    }

	    return count;
	}
}
