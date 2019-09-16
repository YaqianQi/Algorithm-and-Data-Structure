
public class _91_DecodeWays {
	//o(n) 
    public int numDecodings(String s) {
    	if(s == null || s.length() == 0) return 0;
    	int[] dp = new int[s.length()+1]; 
    	dp[0] = 1;
    	dp[1] = s.charAt(0)== '0'? 0:1; 
    			
    	for(int i = 2; i < dp.length;i++) {
    		int first = Integer.valueOf(s.substring(i-1, i));
    		int second = Integer.valueOf(s.substring(i-2, i));
    		if (first<=9 && first>=1) {
    			dp[i] +=dp[i-1];
    		}
    		if(second >= 10 && second <=26) {
    			dp[i] += dp[i-2];
    		}
    	}
    	return dp[s.length()];
        
    }
    
    //o(1)
    /* need review
    public int numDecodings2(String s) {
    	if(s == null || s.length() == 0) return 0;
    	
    	int c1 = 1;
    	int c2 = 2;
    	for(int i = 1; i < s.length(); i++) {
    		if(s.charAt(i) == '0') {
    			c1 = 0;
    		}
    		if(s.charAt(i-1) == '1' || s.charAt(i-1) == '2' && s.charAt(i)<=6) {
    			c1 = c1 + c2;
    			c2 = c1 - c2;
    			System.out.println("c1: "+c1);
    		}else {
    			c2 = c1;
    		}
    	}
    	return c1; 
    	  
    }*/ 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "12";
		String s2 = "226";
		_91_DecodeWays dw = new _91_DecodeWays();
		System.out.println(dw.numDecodings(s));
		//System.out.println(dw.numDecodings2(s));
		System.out.println(dw.numDecodings(s2));
		//System.out.println(dw.numDecodings2(s2));
	}

}
