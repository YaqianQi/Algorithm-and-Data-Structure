package math;
import java.util.*;
public class _1346_CheckIfNandItsDoubleExist2 {
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
	
	public static boolean checkIfExist2(int[] arr) {
        HashSet<Integer> set = new HashSet<>();
        int zero = 0;
        for (int a: arr) {
        	if (a == 0) {
        		zero ++;
        	}else {
        		set.add(a);
        		//System.out.println(a+" "+a*2);
        	}
        	
        }
        for (int a:set) {
        	//System.out.println(a+" "+a*2);
        	if (set.contains(a*2)) {
        		//System.out.println(a+""+a*2);
        		return true;
        	}
        }
        if (zero >= 2) {
        	return true;
        }
        return false;
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = new int[] {10,2,5,3};
		System.out.println(checkIfExist2(arr));
	}

}
