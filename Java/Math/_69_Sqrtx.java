package math;

/*
 * 1. brute-force
 * 2. binary search 
 * 3. Newtown methods
 * */

public class _69_Sqrtx {
	public static int mySqrt1(int x) {
		for (int i = 1; i < x; i++) {
			if (i*i > x) {
				return i-1;
			}
		}
		return -1;
	}
	public static int mySqrt2(int x) {
		int l = 1; 
		int r = x;
		while(l <= r) {
			int mid = (r-l)/2 + l;
			System.out.println("right " +r);
			if (mid * mid > x) {
				r = mid -1;
			}else {
				l = mid+1;
			}
		}
		return r ;
	}
	public static int mySqrt3(int x) {
		int res = x;
		while (res * res > x) {
			res =  (res + x /res)/2;
			}
		return res;
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x = 4;
		System.out.println(mySqrt1(x));
		System.out.println(mySqrt2(x));
		System.out.println(mySqrt3(x));
	}

}
