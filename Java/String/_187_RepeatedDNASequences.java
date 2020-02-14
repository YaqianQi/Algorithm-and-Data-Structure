import java.util.*;
public class _187_RepeatedDNASequences {
	// find substrings that appear twice 
	// o(n) 
	// hashset to set 
	public static List<String> findRepeatedDnaSequences(String s) {
		List<String> res = new ArrayList<String>();
        Set<String> resset = new HashSet<String>();
        if(s == null || s.length() <= 10){
            return res;
        }
        Set<String> set = new HashSet<String>();
        int len = s.length();
        for(int i = 0; i <= len - 10; i++){
            String sub = s.substring(i, i + 10);
            System.out.println(sub);
            if(!set.add(sub)){
                resset.add(sub);
                System.out.println(" This can not be added: "+sub);
            }
        }
        res.addAll(resset);
        return res;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"; 	
		System.out.println(findRepeatedDnaSequences(s));
	}

}
