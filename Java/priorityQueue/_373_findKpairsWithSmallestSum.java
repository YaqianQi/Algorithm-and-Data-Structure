package priorityQueue;
import java.util.*;

public class _373_findKpairsWithSmallestSum {
	
	//o(n)
	
	public List<int[]> kSmallestPairs(int[] nums1,int[] nums2,int k){
		List<int[]> res= new ArrayList<>();
		if(nums1.length ==0 || nums2.length == 0 || k == 0) {
			return res;
		}
		
		PriorityQueue<int[]> priorityQueue = new PriorityQueue<>((a,b)->(a[0]+a[1]-b[0]-b[1]));
		for(int i = 0; i < k && i < nums1.length;i++) {
			priorityQueue.offer(new int[] {nums1[i],nums2[0],0});
		}
		
		while(!priorityQueue.isEmpty() && k-->0) {
			int[] cur = priorityQueue.poll();
			
			res.add(new int[] {cur[0],cur[1]});
			//System.out.println("cur1 " + cur[1]);
			if(cur[2] == nums2.length - 1) continue;
			//System.out.println("cur0 " + cur[0]);
			//System.out.println(nums2[cur[2]+1]);
			priorityQueue.offer(new int[] {cur[0], nums2[cur[2]+1],cur[2]+1});
		}
		return res;
	}
	
	
	public static void main(String[] args) {
		int[] num1 = new int[] {1,2,3};
		int[] num2 = new int[] {2,3,4};
		int k = 3;
		_373_findKpairsWithSmallestSum fk = new _373_findKpairsWithSmallestSum();
		
		List<int[]> res = fk.kSmallestPairs(num1, num2,k);
		
		res.stream().forEach(System.out::println);
		
		/*
		 * print list 
		List<String> features = Arrays.asList("Lambdas", "Default Method", "Stream API", "Date and Time API");
	        (features).forEach(System.out::println);
		
		*/
		
	}

}
