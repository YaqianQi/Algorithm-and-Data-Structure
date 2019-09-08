package greedySearch;

import java.util.Arrays;

public class _253_MeetingRoomsII {
	
	public int minMeetingRooms(int[][] intervals) {
		int[] starts = new int[intervals.length];
        int[] ends = new int[intervals.length];
        for(int i=0; i<intervals.length; i++) {
            starts[i] = intervals[i][0];
            ends[i] = intervals[i][1];
        }
        Arrays.sort(starts);
       // System.out.println(Arrays.toString(starts));
        Arrays.sort(ends);
        //System.out.println(Arrays.toString(ends));
        int rooms = 0;
        int endsItr = 0;
        //the diff is "how many meeting running together at this moment?"
        //=> how many meeting rooms we need.
        for(int i=0; i<starts.length; i++) {
            if(starts[i]<ends[endsItr])
                rooms++;
            else
                endsItr++;
        }
        return rooms;
    }
	    
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] intervals = {{7,10}, {2,4}};
		int[][] intervals2 = {{0,30}, {5,10},{15,20}};
		 _253_MeetingRoomsII mr2 =  new _253_MeetingRoomsII ();
		 System.out.println(mr2.minMeetingRooms(intervals));
		 System.out.println(mr2.minMeetingRooms(intervals2));
	}

}
