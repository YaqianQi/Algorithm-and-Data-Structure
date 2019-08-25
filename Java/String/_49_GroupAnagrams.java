import java.util.*;

public class _49_GroupAnagrams {
	//o( n * m)
	// ababc
	public List<List<String>> groupAnagrams(String[] strs){
		HashMap<String,List<String>> map = new HashMap<>();
		for(String str: strs) {
			int[] count = new int[26];
			for(Character ch: str.toCharArray()) {
				// 把字符转换成count存起来
				// [a]:2,[b]:2,[c]:1
				count[ch-'a'] ++ ;
			}
			String s= "";
			for(int i = 0 ; i < count.length;i++) {
				if(count[i]!=0) {
					// 把count+ 字母转换回来 
					// 2a2b1c
					s+=String.valueOf(count[i]+ String.valueOf(i+'a'));
				}
			}
			// 如果已经包含了2a2b1c，那么把s对应的anagram str取出来，再把str加入
			if(map.containsKey(s)) {
				List<String> list = map.get(s);
				list.add(str);
			}else {
				// 如果没有出现，那么把这个放入map中间 map<combination, prototype>
				List<String> list = new ArrayList<>();
				list.add(str);
				map.put(s, list);
			}
			
		}
		return new ArrayList<>(map.values());
	}
	
	public static void main(String[] args) {
		_49_GroupAnagrams ga = new _49_GroupAnagrams();
		String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
		System.out.println(ga.groupAnagrams(strs));
	}

}
