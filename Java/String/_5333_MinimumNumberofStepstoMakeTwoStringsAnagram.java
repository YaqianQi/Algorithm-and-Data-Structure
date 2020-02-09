package graph;

public class _5333_MinimumNumberofStepstoMakeTwoStringsAnagram {

	public int minSteps(String s, String t){
		int res = 0;
		int[] count = new int[26];
		if (s.length()!= t.length())return -1;
		for (int i = 0; i< s.length();i++) {
			count[s.charAt(i)-'a']++;
			count[t.charAt(i)-'a']--;
		}
		for(int i = 0; i < count.length; i++) {
			if (count[i]<= 0) {
				res += 0-count[i];
			};
		}
		return res;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		_5333_MinimumNumberofStepstoMakeTwoStringsAnagram  ma = new _5333_MinimumNumberofStepstoMakeTwoStringsAnagram ();
		String s = "anagram";
		String t = "mangaar";
		System.out.println(ma.minSteps(s, t));
	}

}
