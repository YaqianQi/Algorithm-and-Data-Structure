
import java.util.*;
public class _344_ReverseString {
/*	
	public String reverseString(String s) {
		if(s == null || s.length() == 0) return "";
		
		int left = 0 , right = s.length()-1;
		char[] cs = s.toCharArray();
		
		
		while(left < right) {
			swap(cs, left, right);
			right -- ;
			left ++ ;
		}
		return new String(cs);
		
	}
	
	*/
	
	public char[] reverseString(char[] s) {
		if(s == null || s.length == 0) return s;
		
		int left = 0 , right = s.length-1;
		
		
		while(left < right) {
			swap(s, left, right);
			right -- ;
			left ++ ;
		}
		return s;
		
	}
	
	public void swap(char[]cs, int i, int j) {
		char temp = cs[i]; 
		cs[i] = cs[j];
		cs[j] = temp;
	}
	
	public static void main(String[] args) {
		
		String s = "hello";
		char[] cs = s.toCharArray();
		_344_ReverseString rs = new _344_ReverseString();
		
		System.out.println(rs.reverseString(cs));
		
	}

}
