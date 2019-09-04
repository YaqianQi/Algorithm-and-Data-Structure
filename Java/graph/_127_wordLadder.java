package graph;
import java.util.*;
public class _127_wordLadder {
	// 这时一道bfs的题，开始突然反应不过来。 可以想象成一棵树，根节点是start字符串，第二层是所有的和它相差一个字母的字符串（之前出现过的，
	// 之后就没有必要出现了，因为出现的话，也是abc变成bbc又变回abs，没有意义），用一个hashmap来保存每一个节点的所处的层数，
	// 还需要一个队列来实现广度优先搜索，因为是从顶层到底层来遍历的，所以发现等于end的时候的层数值就是最小的，返回即可。
	public int ladderLength(String beginWord, String endWord, List<String> wordList) {
	        if(beginWord == null || endWord == null || beginWord.length() == 0 || beginWord.length() != endWord.length()) {
	        	return 0;
	        };
	        
	        // set 里面放的是词性变化
	        Set<String> set = new HashSet<String>(wordList);
	        if(set.contains(beginWord)) {
	        	set.remove(beginWord);
	        }
	        Queue<String> wordQueue = new LinkedList<String>();
	        int level = 1; // start level, 
	        int curnum = 1; //candidate on current level
	        int nextnum = 0; // counter for next level 
	        
	        wordQueue.add(beginWord);
	        
	        while(!wordQueue.isEmpty()) {
	        	String word = wordQueue.poll();
	        	curnum -- ;
	        	for(int i = 0; i < word.length();i++) {
	        		char[] wordunit = word.toCharArray();
	        		for(char j = 'a'; j<='z'; j++) {
	        			wordunit[i] = j;
	        			String temp = new String(wordunit);
	        			if(set.contains(temp)){
	        				if(temp.equals(endWord)) {
	        					return level + 1;
	        				}
	        				nextnum++;
	        				wordQueue.add(temp);
	        				set.remove(temp);
	        			}
	        		}
	        	}
        		if(curnum == 0) {
        			curnum = nextnum;
        			nextnum = 0;
        			level ++ ;
        		}
	        }
	        return 0;
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
		_127_wordLadder wl = new _127_wordLadder();
		System.out.println(wl.ladderLength(beginWord, endWord, wordList));
	}
}
