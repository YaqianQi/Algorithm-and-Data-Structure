package graph;
import java.util.*;
public class _126_wordLadderII {
	// time: o(v+e) ; space: o(n)
	// this time you should return the transformation process 
	public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
		 HashSet<String> set = new HashSet<>(wordList);
	        Queue<List<String>> queue = new ArrayDeque<>();
	        List<String> list = new ArrayList<>();
	        list.add(beginWord);
	        queue.offer(list);
	        //boolean found = false;
	        while (!queue.isEmpty()) {
	            int size = queue.size();
	            HashSet<String> removed = new HashSet<>();
	            for (int i = 0; i < size; i++) {
	                List<String> cur = queue.poll();
	                String lastWord = cur.get(cur.size() - 1);
	                for (int j = 0; j < lastWord.length(); j++) {
	                    char[] array = lastWord.toCharArray();
	                    for (char ch = 'a'; ch <= 'z'; ch++) {
	                        array[j] = ch;
	                        String next = new String(array);
	                        if (set.contains(next)) {
	                            removed.add(next);
	                            cur.add(next);
	                            queue.offer(new ArrayList<>(cur));
	                            cur.remove(cur.size() - 1);
	                        }
	                    }
	                }
	            }
	            if (removed.contains(endWord)) {
	                break;
	            }
	            for (String s : removed) {
	                set.remove(s);
	            }
	        }
	        List<List<String>> result = new ArrayList<>();
	        while (!queue.isEmpty()) {
	            list = queue.poll();
	            String last = list.get(list.size() - 1);
	            if (last.equals(endWord)) {
	                result.add(list);
	            }
	        }
	        return result;
    }
    
	public static void main(String[] args) {
		//{"hot","dot","dog","lot","log","cog"
		String beginWord = "hit";
		String endWord = "cog";
		List<String> wordList = new ArrayList<>();
		wordList.add("hot");
		wordList.add("dot");
		wordList.add("dog");
		wordList.add("lot");
		wordList.add("log");
		wordList.add("cog");
		_126_wordLadderII wl = new _126_wordLadderII();
		System.out.println(wl.findLadders(beginWord, endWord, wordList));
	}
}
