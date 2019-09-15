import java.util.*;
/*
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
*/
public class _139_WordBreak {
	
	
	public boolean wordBreak(String s, List<String> wordDict) {
	  return helper(s, new HashSet<>(wordDict),0);
			
	}
	
	public boolean helper(String s, HashSet<String> wordDict, int index) {
		if(index == s.length())return true;
		
		for(int i = index + 1; i <= s.length() ; i++) {
			if(wordDict.contains(s.substring(index, i))) {
				if(helper(s,wordDict,i)) {
					return true;
				}
			
			}
		}
		return false;
	}
	
	
	
	public boolean wordBreak2(String s, List<String> wordDict) {
		 boolean[] dp = new boolean[s.length() + 1];
		 dp[0] = true;
		 for(int i = 1; i <= s.length(); i++ ) {
			 for(int j = 0; j < i; j++) {
				 if(dp[j] && wordDict.contains(s.substring(j, i))) {
					 dp[i] = true;
					 break;
				
				 }
			 }
		 }
		// System.out.println(Arrays.toString(dp));
		 return dp[s.length()];
		
	}
	
	public static void main(String[] args) {
		
		String s= "leetcode";
		List<String> wordDict = new ArrayList<String>();
		wordDict.add("leet");
		wordDict.add("code");
		_139_WordBreak wb = new _139_WordBreak();
		System.out.println(wb.wordBreak(s, wordDict));
		System.out.println(wb.wordBreak2(s, wordDict));
	}
}
