
public class _2_SelectionSort {
	public static void selectionSort(int[] arr) {
		int n = arr.length; 
		for(int i = 0; i < n-1; i++) {
			int minIndex = i;
			for (int j = i+1; j < n; j++) {
				if (arr[j] < arr[minIndex]) {
					minIndex = j;
				}
			}
			int temp = arr[i];
			arr[i] = arr[minIndex];
			arr[minIndex] = temp;
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {2,3,4,3,2};
		int[] nums2 = new int[] {2,3,4,3,2,99,100,42};
		selectionSort(nums);
		selectionSort(nums2);
		for (int num : nums2)System.out.println(num);
	}

}
