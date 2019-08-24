
import java.util.*;
public class _388_LongestAbsolutePath {
	
	public int LengthLongestPath(String input) {
		Stack<Integer> stack = new Stack<>();
        stack.push(0);
        int res = 0;
        
        for(String s: input.split("\n")){
            int level = s.lastIndexOf("\t") + 1;
            while(level + 1 < stack.size()){
                stack.pop();
            }
            
            int len = stack.peek() + s.length() - level + 1;
            stack.push(len);
            if(s.contains(".")){
                res = Math.max(res,len-1);
            }
        }
        return res;
		
	}
	
	
	
	public static void main(String[] args) {
		String input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext";
		_388_LongestAbsolutePath lap = new _388_LongestAbsolutePath();
		System.out.println( lap.LengthLongestPath(input));
	}
}
