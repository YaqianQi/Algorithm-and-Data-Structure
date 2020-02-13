package binarySearch;

public class _1300_SumofMutatedArrayClosesttoTarget {
	
	
	// O(nlogM)
	// n : arr.length ; M: the largest value 
	public static int findBestValue(int[] arr, int target) {
		int left = 0; 
		int right = target;
		
		while(left < right) {
			int mid = (right - left)/2 + left;
			int sum = sumValue(arr, mid);
			if (sum > target ) {
				right = mid;
			}else {
				left  = mid +1;
			}
		}
		if (Math.abs(target - (left-1)) > Math.abs(target - left)){
			return left;
		} else {
			return left - 1 ;
		}
    }
	public static int sumValue(int[] arr, int value) {
		int sum = 0;
		for(int i = 0; i < arr.length; i++) {
			if (arr[i] > value) {
				sum += value;
			}else {
				sum += arr[i];
			}
		}
		return sum;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = new int[] {4,9,3};
		int target = 10;
		int res = findBestValue(arr, target); 
		System.out.println(res);
	}

}
