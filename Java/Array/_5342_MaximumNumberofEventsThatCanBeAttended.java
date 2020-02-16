import java.util.*;

public class _5342_MaximumNumberofEventsThatCanBeAttended {
	public static int maxEvents(int[][] A) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        Arrays.sort(A, (a, b) -> Integer.compare(a[0], b[0]));
        int i = 0, res = 0, n = A.length;
        for (int d = 1; d <= 100000; ++d) {
            while (i < n && A[i][0] == d)
                pq.offer(A[i++][1]);
            while (pq.size() > 0 && pq.peek() < d){
                pq.poll();
            }
            if (pq.size() > 0) {
                pq.poll();
                ++res;
            }
        }
        return res;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] events2 = {{1,1},{1,2},{1,3},{1,4},{1,5},{1,6},{1,7}};
		System.out.println(maxEvents(events2));
	}

}
