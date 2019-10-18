import java.util.*;
public class _295_FindMedianfromDataStream {
	PriorityQueue<Integer> minHeap = new PriorityQueue<>();
	PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
	public _295_FindMedianfromDataStream() {
	        
	    }
	    
	    public void addNum(int num) {
	        minHeap.offer(num);
	        maxHeap.offer(minHeap.poll());
	        if (maxHeap.size() > minHeap.size()) {
	        	minHeap.offer(maxHeap.poll());
	        }
	    }
	    
	    public double findMedian() {
	        if(minHeap.size()>maxHeap.size()) {
	        	return minHeap.peek();
	        }else {
	        	return 1/2 * (minHeap.peek()+ maxHeap.peek());
	        }
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		_295_FindMedianfromDataStream fm = new _295_FindMedianfromDataStream ();
		fm.addNum(3);
		fm.addNum(4);
		fm.addNum(5);
		System.out.println(fm.findMedian());

	}

}
