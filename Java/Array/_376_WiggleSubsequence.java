import java.util.Arrays;

public class _376_WiggleSubsequence {
	
	public int wiggleMaxLength(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
		int n = nums.length;
		int[] up = new int[n];
		int[] down = new int[n];
		Arrays.fill(up,1);
		Arrays.fill(down, 1);
		for(int i = 1; i < n; i++) {
			if (nums[i] > nums[i-1]) {
				up[i] = Math.max(down[i-1]+1, up[i]);
				down[i] = down[i-1];
			}else if(nums[i]< nums[i-1]){
				down[i] = Math.max(up[i-1]+1,down[i]);
				up[i] = up[i-1];
			}else{
                down[i] = down[i-1];
                up[i] = up[i-1];
            }
		}
		return Math.max(up[n-1], down[n-1]); 
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {1,7,4,9,2,5};
		_376_WiggleSubsequence ws = new _376_WiggleSubsequence();
		System.out.println(ws.wiggleMaxLength(nums));
	}

}
