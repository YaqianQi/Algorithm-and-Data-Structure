
public class _307_RangeSumQueryMutable {
	int[] btree;
	int[] arr;
	 public _307_RangeSumQueryMutable(int[] nums) {
	        btree = new int[nums.length + 1];
	        arr = nums;
	        for(int i = 0; i < nums.length ; i++) {
	        	add(i+1,nums[i]);
	        }
	    }
	 public void add(int i , int val) {
		 for(int j = i; j < btree.length;j= j + (j&(-j))) {
			 btree[j] += val;
		 }
	 }
	    
    public void update(int i, int val) {
    	add(i+1,val - arr[i]);
    	arr[i] = val;
        
    }
	    
    public int sumRange(int i, int j) {
    		return sumHelper(j+1) - sumHelper(i);
    }
    
    public int sumHelper(int i) {
    	int sum = 0;
        for(int j = i; j >= 1; j = j-(j&(-j))) {
        	sum+= btree[j];
        }
        return sum;
    }
    
    public static void main(String[] args) {
    	int[] nums = new int[] {1,3,5};
    	_307_RangeSumQueryMutable rsm = new _307_RangeSumQueryMutable(nums);
    	System.out.println(rsm.sumRange(0, 2));
    	rsm.update(1, 2);
    	System.out.println(rsm.sumRange(0, 2));
    	
    }
}
