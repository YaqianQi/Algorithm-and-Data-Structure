
public class _5_MergeSort {
	
	public static void mergeSort(int[] arr, int left, int right) {
		       
		         if (left < right) {
		        	 
		            int mid = (left + right) / 2;
		            System.out.println("left "+left+ " right "+right+" mid " + mid);
		            mergeSort(arr, left, mid);
		            mergeSort(arr, mid + 1, right);
		            merge(arr, left, mid, right);
		        }
		   
		    }
		
		    private static void merge(int[] arr, int left, int mid, int right) {
		        int[] a = new int[right - left + 1];
		        int i = left;
		        int j = mid + 1;
		        int k = 0;
		        while (i <= mid && j <= right) {
		            if (arr[i] < arr[j]) {
		                a[k++] = arr[i++];
		            } else {
		                a[k++] = arr[j++];
		            }
		        }
		        while(i <= mid) a[k++] = arr[i++];
		        while(j <= right) a[k++] = arr[j++];
		        
		        for (i = 0; i < k; i++) {
		            arr[left++] = a[i];
		        }
		    }
	public static void main(String[] args) {	
		int[] nums2 = new int[] {2,3,4,3,2,99,100,42};
		mergeSort(nums2,0,nums2.length - 1);
		for (int num : nums2)System.out.println(num);
		
	}
}
