
public class _509_FibonacciNumber {
	//0, 1, 1, 2, 3, 5, 8, 13, 21, 34
	// recursive 
	 public int fib0(int N) {
		 int a = 0;
		 int b = 1;
		 if (N<=1) return N;
		 int temp = 0;
		 while (N >=2) {
			 temp = a + b;
			 a = b;
			 b = temp;
			 N--;
		 }
		 return temp;
	 }
	 public int fib1(int N) {
	        if(N<=1) return N;
	        return fib1(N-1) + fib1(N-2);
	        
	 }
	 
	 // memorization 
	 int[] memorization = new int[12345];
	 public int fib2(int N) {
		 if(N <= 1) {
			 return N;
		 }
		 if(memorization[N] == 0) {
			 memorization[N] = fib2(N-1) + fib2(N-2);
		 }
		 return memorization[N];
	 }
	 
	 // dynamic programming 
	 public int fib3(int N) {
		 if(N<=1) {
			 return N;
		 }
		 int[] dp = new int[N+1];
		 dp[1] = 1;
		 for(int i = 2; i <= N;i++) {
			 dp[i] = dp[i-1] + dp[i-2];
		 }
		 return dp[N];
	 }
	 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		_509_FibonacciNumber fn = new _509_FibonacciNumber();
		System.out.println(fn.fib0(4));
		System.out.println(fn.fib1(4));
		System.out.println(fn.fib2(4));
		System.out.println(fn.fib3(4));
	}

}
