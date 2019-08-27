package priorityQueue;
import java.util.*;

public class _215_findKthLargest {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(); 
        for(int num : nums) {
        	priorityQueue.offer(num);
        	if(priorityQueue.size()>k) {
        		priorityQueue.poll();
        	}
        }
        return priorityQueue.poll();
    
    }
    
    public static void main(String[] args) {
    	int[] nums = {1,2,3,4,5};
    	int k = 1;
    	_215_findKthLargest fk = new _215_findKthLargest();
    	System.out.println(fk.findKthLargest(nums, k));
    }
}
