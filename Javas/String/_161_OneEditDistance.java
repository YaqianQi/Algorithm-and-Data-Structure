
public class _161_OneEditDistance {
	
	// time complexity O(N)
	
	public static boolean isOneEditDistance(String s, String t) {
		for(int i = 0; i < Math.min(s.length(),t.length());i++){
			if(s.charAt(i)!=t.charAt(i)) {
				if(s.length() == t.length()) {
					// 如果现在的字母不同那么只需要比较后面的字母就可以了
					return s.substring(i+1).equals(t.substring(i+1));
				}else if (s.length() > t.length()) {
					// 如果其中的一个string比另外一个要长，那么比较长的string后的substring
					return s.substring(i+1).equals(t.substring(i));
				}else {
					return t.substring(i+1).equals(s.substring(i));
				}
			}
		}
		return Math.abs(s.length() - t.length()) == 1;
	}
	
	public static void main(String[] args) {
		
		String s= "abcdef";
		String t = "abc";
		System.out.println(isOneEditDistance(s,t));
		
		
		String s1= "abcd";
		String t1 = "abc";
		System.out.println(isOneEditDistance(s1,t1));
	}

}
