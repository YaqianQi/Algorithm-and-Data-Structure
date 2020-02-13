
public class _560_SubarraySumEqualsK {
	public int subarraySum(int[] nums, int k) {
        int temp = 0;
        int res = 0 ; 
        for (int i = 0; i < nums.length; i++){
            temp = nums[i];
            if (temp == k){
             res++;
            }
            for (int j = i+1; j< nums.length; j++){
                temp+= nums[j];
                if (temp == k) res++;
            }
        }
        return res;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {1,1,1};
		_560_SubarraySumEqualsK ssek = new _560_SubarraySumEqualsK();
		System.out.println(ssek.subarraySum(nums, 2));
		}
	}


