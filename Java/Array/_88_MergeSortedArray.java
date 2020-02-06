
public class _88_MergeSortedArray {
	 public void merge(int[] nums1, int m, int[] nums2, int n) {
	     int p1 = m-1 ;
	     int p2 = n-1;
	     int p3 = m+n - 1;
	     
	     while(p1 >= 0 && p2>= 0) {
	    	 if (nums1[p1] > nums2[p2]) {
	    		 nums1[p3--] = nums1[p1--];
	    	 }else {
	    		 nums1[p3--] = nums2[p2--];
	    	 }
	     }
	     while(p2 >= 0) {
	    	 nums1[p3--] = nums2[p2--];
	     }
	     while(p1 >= 0) {
	    	 nums1[p3--] = nums1[p1--];
	     }
	     for (int num: nums1) {
	    	 System.out.print(num+" ");
	     }
	     
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums1 = new int[] {1,2,3,0,0,0};
		int m = 3;
		int[] nums2 = new int[] {2,5,6};
		int n = 3;
		// should return [1,2,2,3,5,6]
		 _88_MergeSortedArray msa = new  _88_MergeSortedArray();
		 msa.merge( nums1,  m, nums2, n);
	}

}
