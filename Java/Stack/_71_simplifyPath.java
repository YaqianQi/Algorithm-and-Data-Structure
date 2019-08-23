import java.util.*;
public class _71_simplifyPath {
	
	public String simplifyPathMethod(String path) {
		Stack<String> stack = new Stack<>();
		
		String[] paths = path.split("/+");
		for(String s: paths) {
			if(s.equals("..")){
				if(!stack.isEmpty()) {
					stack.pop();
				}
			}else if(!s.equals(".") && !s.equals("")) {
				stack.push(s);
			}
		}
		
		String res = "";
		while(!stack.isEmpty()) {
			res = '/' + stack.pop() + res;
		}
		
		if(res.length() == 0) {
			return "/";
		}
		return res;
		
		}
	
	public static void main(String[] args) {
		String path = "/home/123";
		
		simplifyPath  sm  = new simplifyPath();
		System.out.println(sm.simplifyPathMethod(path));
	}

}
