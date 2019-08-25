
public class _151_ReverseWordsInAString {
	// time complexity : o(n)
	// space o(n) 
	public String reverseWords(String s){
		StringBuilder sb = new StringBuilder();
		String[] word = s.trim().split("\\s+"); // \\s: 换行回撤，+多个
		for(int i = word.length - 1; i >=0 ; i--) {
			sb.append(word[i] + " ");
			//System.out.println(word[i]);
		}
		
		
		return sb.toString().trim();
	}
	
	
	public static void main(String[] args) {
		_151_ReverseWordsInAString  rw = new _151_ReverseWordsInAString();
		String s = "Dont want to work everyday";
		
		System.out.println(rw.reverseWords(s));
	}

}
