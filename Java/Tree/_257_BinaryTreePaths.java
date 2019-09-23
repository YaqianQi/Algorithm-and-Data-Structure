import java.util.*;
public class _257_BinaryTreePaths {
	public List<String> binaryTreePaths(TreeNode root) {
		List<String> res = new ArrayList<>();
	    if (root == null) return res; 
	    helper(root, res, "");
	    return res;
	}
	void helper(TreeNode root,List<String> res,String path) {
		if(root.left == null && root.right == null) {
			res.add(path+root.val);
		} ;
		if (root.left != null) {
			helper(root.left, res, path+ root.val+ "->");
		}
		if(root.right != null) {
			helper(root.right, res, path+root.val + "->");
		}
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode root = new TreeNode(1);
		root.left = new TreeNode(2);
		root.left.right = new TreeNode(5);
		root.right = new TreeNode(3);
		_257_BinaryTreePaths btp = new _257_BinaryTreePaths();
		System.out.println(btp.binaryTreePaths(root));
	}

}
