
public class _3_InsertionSort {
	public static void insertSort(int[] arr) {
		int n = arr.length;
		for (int i = 1; i < n; i++) {
			int temp = arr[i];
			int k = i-1;
			while(k >= 0 && arr[k]> arr[i]) {
				k --;
			}
			//k+1 is the insert position 
			for(int j = i; j > k+1; j--) {
			arr[j] = arr[j-1];
			}
			arr[k+1] = temp;
		}	
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {2,3,4,3,2};
		int[] nums2 = new int[] {2,3,4,3,2,99,100,42};
		insertSort(nums);
		insertSort(nums2);
		for (int num : nums2)System.out.println(num);
	}

}
