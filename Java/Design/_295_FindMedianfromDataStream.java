package design;
import java.util.*;
public class _295_FindMedianfromDataStream {
		private PriorityQueue<Integer> maxQueue;
		private PriorityQueue<Integer> minQueue;
		public _295_FindMedianfromDataStream() {
	        maxQueue = new PriorityQueue<>(Collections.reverseOrder());
	        minQueue = new PriorityQueue<>();
	    }
	    
	    public void addNum(int num) {
	    	minQueue.offer(num);
	    	maxQueue.offer(minQueue.poll());
	    	if(minQueue.size() < maxQueue.size()) {
	    		minQueue.offer(maxQueue.poll());
	    	}
	        
	    }
	    
	 public double findMedian() {
	            
	            if(minQueue.size() > maxQueue.size()){
	            return minQueue.peek();
	        }else {
	            return (minQueue.peek()+maxQueue.peek())/2.0;}
	        }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		_295_FindMedianfromDataStream fmd = new _295_FindMedianfromDataStream();
		fmd.addNum(3);
		fmd.addNum(4);
		fmd.addNum(5);
		fmd.addNum(6);
		fmd.addNum(7);
		System.out.println(fmd.findMedian());
	}

}
