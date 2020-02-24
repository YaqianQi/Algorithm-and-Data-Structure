
public class _4_ShellSort {
	public static void shellSort(int[] arr) {
		  	int n = arr.length; 
	        // Start with a big gap, then reduce the gap 
	        for (int gap = n/2; gap > 0; gap /= 2) {
	        	for (int i = gap; i < n; i += 1) { 
	                int temp = arr[i]; 
	                int j; 
	                for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
	                    arr[j] = arr[j - gap];
	                }
	                arr[j] = temp; 
	            } 
	        } 
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {2,3,4,3,2};
		int[] nums2 = new int[] {2,3,4,3,2,99,100,42};
		shellSort(nums);
		shellSort(nums2);
		for (int num : nums2)System.out.println(num);
		//System.out.println(5/2);
	}
	
}
