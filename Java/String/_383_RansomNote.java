
public class _383_RansomNote {
	//为啥叫勒索信？原因：匪徒想再杂志上找可以用来写信的字母，所以，只能用一次
	// 最快的方式 bit manipulation
	public boolean canConstruct(String ransomNote, String magazine) {
		int[] arr = new int[26];
		for(int i = 0; i< magazine.length();i++) {
			arr[magazine.charAt(i)-'a']++;
		}
		for(int i = 0; i < ransomNote.length();i++) {
			if(--arr[ransomNote.charAt(i)-'a']<0) {
				return false;
			}
		}
		return true;
	}
	
	public static void main(String[] args) {
		_383_RansomNote rn = new  _383_RansomNote();
		String ransomNote = "cmbspool";
		String magazine  =  "cmbspoolishuge";
		System.out.println(rn.canConstruct(ransomNote, magazine));
		
		String aa = "aa";
		String bb = "bb";
		System.out.println(rn.canConstruct(aa, bb));
	
	}
	
}
