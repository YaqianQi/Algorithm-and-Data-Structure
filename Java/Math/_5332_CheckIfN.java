package math;
import java.util.*;
public class _5332_CheckIfN {
	public boolean checkIfExist(int[] arr) {
        Arrays.sort(arr);
        for (int i = 1; i < arr.length; i++){
            for (int j = 0; j < i; j++){
                if (arr[i] == 0 && arr[j] == 0) return true;
                if ( arr[j] == 0) continue;
                System.out.println(arr[i]+" "+ arr[j]);
                if (arr[i]>0 && arr[j]>0) {
                	if (arr[i]/arr[j] == 2 && arr[i] % arr[j] == 0 ){
                        return true;
                    }
                }else if (arr[i]<0 && arr[j]<0){
                	if (arr[j]/arr[i] == 2 && arr[j] % arr[i] == 0 ){
                        return true;
                }
               }
                
            }
        }
        return false;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {-10,12,-20,-8,15};
		_5332_CheckIfN ci = new _5332_CheckIfN();
		System.out.println(ci.checkIfExist(nums));
	}

}
