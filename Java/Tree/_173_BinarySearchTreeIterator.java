import java.util.*;
public class _173_BinarySearchTreeIterator {
	// BSTIterator 
	private TreeNode cur;
	private Stack<TreeNode> stack;
	public _173_BinarySearchTreeIterator(TreeNode root) {
		cur = root;
		stack = new Stack<>();
	        
	    }
	    
	    /** @return the next smallest number */
	    public int next() {
	    	while(cur!=null) {
	    		stack.push(cur);
	    		cur = cur.left;
	    	}
	    	cur = stack.pop();
	    	int val = cur.val;
	    	cur = cur.right;
	    	return val;
	    
	    }
	    
	    /** @return whether we have a next smallest number */
	    public boolean hasNext() {
	    	if(!stack.isEmpty() || cur!=null) return true;
	    	return false;
	        
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 TreeNode t = new TreeNode(3);
		 t.left = new TreeNode(9);
		 t.right = new TreeNode(20);
		 t.right.left = new TreeNode(15);
		 t.right.right = new TreeNode(7);
		_173_BinarySearchTreeIterator bsti = new _173_BinarySearchTreeIterator(t);
		System.out.println(bsti.next());
		System.out.println(bsti.hasNext());
		
	}

}
