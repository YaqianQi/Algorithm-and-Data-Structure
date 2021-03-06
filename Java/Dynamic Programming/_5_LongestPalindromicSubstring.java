
public class _5_LongestPalindromicSubstring {
	//o(n)
	public String longestPalindrome(String s) {
		if(s == null || s.length() == 0) return s;
		boolean[][] dp = new boolean[s.length()][s.length()];
		String res = "";
		int max = 0;
		
		for(int j = 0; j < s.length(); j++) {
			for(int i = 0; i <= j; i++) {
				// 从外向里，如果只有两位就不用往里看了
				dp[i][j] = s.charAt(i) == s.charAt(j) && ((j-i<=2) || dp[i+1][j-1]);
				if(dp[i][j]) {
					if((j-i+1)> max){
						max = j-i+1; 
						res= s.substring(i,j+1);
					}
					
				}
				
			}
		}
		return res; 
	}
	public String res = "";
	public String longestPalindromeDFS(String s) {
		if (s == null || s.length() == 0) return s;
		for(int i = 0; i < s.length();i++) {
			helper(s,i,i);
			helper(s,i,i+1);
		}
		
		return res;
	}
	// o(n^2)
	public void helper(String s, int left, int right) {
		while(left >= 0 && right< s.length() && s.charAt(left) == s.charAt(right)) {
			left--;
			right++;
		}
		String cur = s.substring(left + 1,right);
		if(cur.length() >res.length()) {
			res = cur;
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "babad";
		
		 _5_LongestPalindromicSubstring lps = new _5_LongestPalindromicSubstring();
		 System.out.println(lps.longestPalindrome(s));
		 System.out.println(lps.longestPalindromeDFS(s));
	}

}
