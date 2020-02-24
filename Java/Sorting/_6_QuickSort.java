
public class _6_QuickSort {
	public static int[] quickSort(int[] arr, int left , int right) {
		  if (left < right) {
		       int mid = merge(arr, left, right);       
		       arr = quickSort(arr, left, mid - 1);
		       arr = quickSort(arr, mid + 1, right);
			 }
		return arr;
	}
	
	public static int merge(int[] arr, int left , int right) {
		  //选取中轴元素
	        int pivot = arr[left];
	        int i = left + 1;
	        int j = right;
	        // System.out.println("i start " + i + " j start " + j);
	        while (true) {
	            // pivot 的元素位置
	            while (i <= j && arr[i] <= pivot) i++;
	            // pivot 的元素位置
	            while(i <= j && arr[j] >= pivot ) j--;
	           // System.out.println("j in loop " + j );
	            if(i >= j)
	                break;
	            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
	       }
	       arr[left] = arr[j];
	       arr[j] = pivot;
	       return j;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {2,3,4,3,2};
		int[] nums2 = new int[] {2,3,4,3,2,99,100,42};
		nums =  quickSort(nums, 0, nums.length - 1 );
		nums2 = quickSort(nums2, 0, nums2.length - 1);
		for (int num : nums2)System.out.println(num);
	}
}
