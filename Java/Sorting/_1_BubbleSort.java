
public class _1_BubbleSort {
	public static void bubbleSort(int[] arr) {
		int n = arr.length; 
        for (int i = 0; i < n-1; i++) 
            for (int j = 0; j < n-i-1; j++) {
            	 System.out.println("j " + j);
                if (arr[j] > arr[j+1]) { 
                    int temp = arr[j]; 
                    arr[j] = arr[j+1]; 
                    arr[j+1] = temp; 
                } 
            }
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {2,3,4,3,2};
		int[] nums2 = new int[] {2,3,4,3,2,99,100,42};
		bubbleSort(nums);
		bubbleSort(nums2);
		//for (int num : nums2)
		//System.out.println(num);
	}

}
