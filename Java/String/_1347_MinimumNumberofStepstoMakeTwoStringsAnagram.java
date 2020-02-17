package math;

public class _1347_MinimumNumberofStepstoMakeTwoStringsAnagram {
	public static int minSteps(String s, String t) {
	 int[] v1 = new int[26];
	 int[] v2 = new int[26];
	 int res = 0;
	 for (int i = 0; i < s.length(); i++) {
		 v1[s.charAt(i) - 'a'] ++ ;
	 }
	 for (int i = 0; i < t.length(); i++) {
		 v2[t.charAt(i) - 'a'] ++ ;
	 }
	 for(int i = 0; i < 26;i ++) {
		 res += Math.abs(v1[i] - v2[i]);
	 }
	 return res / 2 ;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "leetcode", t = "practice";
		System.out.println(minSteps(s,t));
	}

}
