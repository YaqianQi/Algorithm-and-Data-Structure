import java.util.*;
public class _347_TopKFrequentElements {
	 public List<Integer> topKFrequent(int[] nums, int k) {
         HashMap<Integer, Integer> map = new HashMap<>();
         for (int num : nums) {
             map.put(num, map.getOrDefault(num, 0) + 1);
         }

         // create a min heap
         PriorityQueue<Map.Entry<Integer, Integer>> queue 
                       = new PriorityQueue<>(Comparator.comparing(e -> e.getValue()));

         //maintain a heap of size k.
         for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
             queue.offer(entry);
             if (queue.size() > k) {
                 queue.poll();
             }
         }

         //get all elements from the heap
         List<Integer> result = new ArrayList<>();
         while (queue.size() > 0) {
             result.add(queue.poll().getKey());
         }

         //reverse the order
         Collections.reverse(result);

         return result;
 }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {1,1,1,2,2,3};
		int k = 2;
		_347_TopKFrequentElements tfe = new _347_TopKFrequentElements();
		System.out.println(tfe.topKFrequent(nums,k));
	}

}
