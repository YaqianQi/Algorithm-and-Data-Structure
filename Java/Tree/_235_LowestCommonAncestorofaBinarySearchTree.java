
public class _235_LowestCommonAncestorofaBinarySearchTree {
	public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
	        if (root.val > p.val && root.val > q.val) {
	        	return lowestCommonAncestor(root.left, p,  q);
	        }else if (root.val < p.val && root.val < q.val) {
	        	return lowestCommonAncestor(root.right, p,  q);
	        }else {
	        	return root;
	        }
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode root = new TreeNode(6);
		root.left = new TreeNode(2);
		root.right = new TreeNode(8);
		TreeNode p = new TreeNode(2);
		TreeNode q = new TreeNode(8);
		_235_LowestCommonAncestorofaBinarySearchTree lt = new _235_LowestCommonAncestorofaBinarySearchTree();
		System.out.println(lt.lowestCommonAncestor(root, p, q).val);
	}

}
