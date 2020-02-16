import java.util.*;
public class _560_SubarraySumEqualsK {
	
	public static int subarraySum(int[] nums, int k) {
		// O(N^2)
		int res = 0;
		for(int i = 0; i < nums.length; i++) {
			int temp = nums[i];
		
			if (temp == k) {
				res ++;
			}
			for(int j = i+1; j< nums.length; j++) {
				temp += nums[j];
				//System.out.println(nums[i] +" "+j+" " +temp);
				if (temp == k) {
					res ++;
				}
			}
		}
		return res;
	
	}
	public static int subarraySum2(int[] nums, int k) {
		// TIME: O(N), SPACE: O(N)
		int res = 0;
		HashMap<Integer, Integer> map = new HashMap<>();
		map.put(0, 1);
		int sum = 0;
		for (int i = 0; i < nums.length; i++) {
			sum += nums[i];
			if (map.containsKey(sum - k)) {
				res += map.get(sum - k); 
			}
			map.put(sum, map.getOrDefault(sum, 0)+1);
		}
		return res;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums1 = new int[] {1,1,1};
		int k1 = 2;
		int[] nums2 = new int[] {28,54,7,-70,22,65,-6};
		int k2 = 100;
		System.out.println(subarraySum(nums1,k1));
		System.out.println(subarraySum2(nums2,k2));
	}

}
