import java.util.*;

public class _102_BinaryTreeLevelOrderTraversal {
	
	public List<List<Integer>> levelOrder(TreeNode root) {
		List<List<Integer>> res = new LinkedList<>();
		if(root == null)
			return res;

		Queue<TreeNode> queue = new LinkedList<>();
		queue.offer(root);

		while(queue.size() > 0){
			int len = queue.size();
			List<Integer> list = new LinkedList<>();
			for(int i=0; i<len; i++){
				TreeNode curr = queue.poll();
				list.add(curr.val); 
				if(curr.left != null) queue.offer(curr.left);
				if(curr.right != null) queue.offer(curr.right);
			}
			res.add(list);
		}
		return res;
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode t = new TreeNode(3);
    	t.left = new TreeNode(9);
    	t.right = new TreeNode(20);
    	t.right.left = new TreeNode(15);
    	t.right.right = new TreeNode(7);
    	
    	_102_BinaryTreeLevelOrderTraversal btlor = new _102_BinaryTreeLevelOrderTraversal();
    	System.out.println(btlor.levelOrder(t));
    	
	}

}
