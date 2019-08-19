
public class reverseInteger {
	
	public static int  reverse(int n ) {
		int res = 0 ;
		while (n != 0) {
			int cur = res;
			res = res * 10 +  n % 10;
			n /= 10;
			if (res/10!=cur) {
				return 0;
			}
		}
		
		return res; 
	}
	
	
	public static void main(String[] args) {
		System.out.println(reverse(30220001));
		
	}

}
