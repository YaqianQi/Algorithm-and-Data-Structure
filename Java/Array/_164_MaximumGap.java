import java.util.Arrays;

public class _164_MaximumGap {
	// quick sort: o(nlogn)
	public int maximumGap(int[] nums) {
	    int res = Integer.MIN_VALUE; 
	    if(nums == null || nums.length < 2) return 0;
	    Arrays.sort(nums);
		for(int i = 1; i < nums.length; i++) {
	    	int cur = nums[i] - nums[i-1];
	    	res = Math.max(cur, res);
	    }
		return res;
	}
	// bucket sort: o(n)
	
	class Bucket{
	    int low;
	    int high;
	    public Bucket(){
	        low = -1;
	        high = -1; 
	    }
	    }
	public int maximumGap2(int[] num) {
		if(num == null || num.length < 2){return 0; }
		 
	    int max = num[0];
	    int min = num[0];
	    for(int i=1; i<num.length; i++){
	        max = Math.max(max, num[i]);
	        min = Math.min(min, num[i]);
	    }
	 
	    // initialize an array of buckets
	    Bucket[] buckets = new Bucket[num.length+1]; //project to (0 - n)
	    for(int i=0; i<buckets.length; i++){
	        buckets[i] = new Bucket();
	    }
	 
	    double interval = (double) num.length / (max - min);
	    //distribute every number to a bucket array
	    for(int i=0; i<num.length; i++){
	        int index = (int) ((num[i] - min) * interval);
	 
	        if(buckets[index].low == -1){
	            buckets[index].low = num[i];
	            buckets[index].high = num[i];
	        }else{
	            buckets[index].low = Math.min(buckets[index].low, num[i]);
	            buckets[index].high = Math.max(buckets[index].high, num[i]);
	        }
	    }
	 
	    //scan buckets to find maximum gap
	    int result = 0;
	    int prev = buckets[0].high;
	    for(int i=1; i<buckets.length; i++){
	        if(buckets[i].low != -1){
	            result = Math.max(result, buckets[i].low-prev);
	            prev = buckets[i].high;
	        }
	 
	    }
	 
	    return result;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {3,6,9,1};
		_164_MaximumGap mg = new _164_MaximumGap();
		System.out.println(mg.maximumGap(nums));
		System.out.println(mg.maximumGap2(nums));
	}

}
