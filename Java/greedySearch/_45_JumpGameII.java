package greedySearch;

public class _45_JumpGameII {
	// time o(n)
	// space o(1)
    public int jump(int[] nums) {
        if(nums == null || nums.length < 2) {
        	return 0;
        }
        int res = 0;
        int  curMaxArea = 0;
        int maxNext = 0;
        for(int i = 0; i < nums.length-1 ;i++) {
        	maxNext = Math.max(maxNext, nums[i] + i);
        	if(i ==  curMaxArea) {
        		res++;
        		 curMaxArea = maxNext;
        	}
        }
        return res;
        	
    }
   
    public int jumpBfs(int[] nums) {
        if(nums == null || nums.length < 2) {
        	return 0;
        }
        int level = 0;
        int  curMaxArea = 0;
        int maxNext = 0;
        int i = 0;
        while(curMaxArea - i + 1 > 0) {
        	level ++ ;
        	for(; i <= curMaxArea; i ++) {
        		maxNext = Math.max(maxNext, nums[i] + i);
        		if(maxNext >= nums.length - 1) {
        			return level;
        		}
        	}
        	curMaxArea = maxNext;
        }

        return 0;
        	
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {2,3,1,1,4};
		_45_JumpGameII jg2 = new _45_JumpGameII();
		System.out.println(jg2.jump(nums));
		System.out.println(jg2.jumpBfs(nums));
	}
}
