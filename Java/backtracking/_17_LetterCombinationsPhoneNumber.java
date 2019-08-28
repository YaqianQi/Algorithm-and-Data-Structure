package backtracking;
import java.util.*;

public class _17_LetterCombinationsPhoneNumber {
	
	// time O(3^n)
    private String[] mapping = new String[]{"0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
	public List<String> letterCombinations(String digits) {
        List<String> res=  new ArrayList<>();
        if(digits == null || digits.length() == 0) {
        	return res;
        }
        
        helper(res, "", digits, 0);
        return res;
    }
    
    public void helper(List<String> res, String s , String digits, int index ) {
    	if (s.length() == digits.length()) {
    		res.add(s);
    		//return ;
    	}
    	String Letters = mapping[digits.charAt(index) - '0'];
    	for(int i = 0; i < Letters.length(); i++) {
    		helper(res, digits, s + Letters.charAt(i),index+ 1);
    	}
    	
    }
	
	
	
	public static void main(String[] args) {
		
		_17_LetterCombinationsPhoneNumber lcpn = new _17_LetterCombinationsPhoneNumber();
		List<String> res = lcpn.letterCombinations("23");
		System.out.println(res);
		
	}

}
