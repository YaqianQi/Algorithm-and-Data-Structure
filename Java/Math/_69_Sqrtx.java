package math;

/*
 * 1. brute-force o(n)
 * 2. binary search : O(logN).
 * 3. Newtown methods : O(logN)
 * */

public class _69_Sqrtx {
	public static int mySqrt1(int x) {
		if (x <= 1) return x;
	    for (long s = 1; s <= x; ++s)
	    	if (s * s > x) return (int)s - 1;
	    return -1;
	}
	public static int mySqrt2(int x) {
		int l = 1;
        int r = x;
        while (l <= r) {
          int m = l + (r - l) / 2;
          if (m > x / m) {
            r = m - 1;
          } else {
            l = m + 1;
          }
        }
        return r;
	}
	public static int mySqrt3(int x) {
		if (x < 2) return x;

        double x0 = x;
        double x1 = (x0 + x / x0) / 2.0;
        while (Math.abs(x0 - x1) >= 1) {
          x0 = x1;
          x1 = (x0 + x / x0) / 2.0;
        }

        return (int)x1;
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x = 4;
		System.out.println(mySqrt1(x));
		System.out.println(mySqrt2(x));
		System.out.println(mySqrt3(x));
	}

}
