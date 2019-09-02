
public class _303_RangeSumQueryImmutable {
	private int[] sum;
	 public _303_RangeSumQueryImmutable(int[] nums) {
	        sum = new int[nums.length + 1];
	        for(int i = 0; i < nums.length; i++) {
	        	sum[i+1] = sum[i] + nums[i];
	        }
	    }
	    
    public int sumRange(int i, int j) {
    	return sum[j+1] - sum[i];
        
    }

	public static void main(String[] args) {
		int[] nums = new int[] {-2,0,3,-5,2,-1};
		_303_RangeSumQueryImmutable rsqi = new _303_RangeSumQueryImmutable(nums);
		System.out.println(rsqi.sumRange(1,3));
	}
}
