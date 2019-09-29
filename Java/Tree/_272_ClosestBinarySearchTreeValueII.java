import java.util.*;
public class _272_ClosestBinarySearchTreeValueII  {
    // find k value that close to target in BST
	// dfs
	// in-order 
	//List<Integer> res ;
	public List<Integer> closestKValues(TreeNode root, double target, int k) {
		LinkedList<Integer> res = new LinkedList<>();
		helper(res, root, target, k);
		return res;
        
    }
	void helper(LinkedList<Integer> res, TreeNode root, double target, int k) {
		if (root == null) return ;
		helper(res ,root.left, target, k);
		if (k == res.size()) {
			if (Math.abs(root.val - target) < Math.abs(target - res.peekFirst())) {
				res.removeFirst();
			}else return ;
		}
		res.add(root.val);
		helper(res,root.right, target, k);
		
		
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		TreeNode root = new TreeNode(4);
		root.left = new TreeNode(2);
		root.right = new TreeNode(5);
		root.left.left = new TreeNode(1);
		root.left.right = new TreeNode(3);
		
		_272_ClosestBinarySearchTreeValueII cbst = new _272_ClosestBinarySearchTreeValueII();
		System.out.println(cbst.closestKValues(root, 3.7,2));
	}

}
