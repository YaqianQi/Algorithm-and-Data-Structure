package greedySearch;

public class _55_Jump_Game {
    public boolean canJump(int[] nums) {
        int max = 0;
        for(int i = 0; i < nums.length; i++){
            
            if(max < i) return false;
            max = Math.max(max, nums[i]+i);
        }
        return true;
    }
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = {2,3,1,1,4};
		_55_Jump_Game jg = new _55_Jump_Game();
		System.out.println(jg.canJump(nums));
	}

}
