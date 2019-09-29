
public class _236_LowestCommonAncestorofaBinaryTree {
	// cant pass leetcode  
	public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
	        if (root == null || root == q|| root == p) return root;
	        TreeNode left = lowestCommonAncestor(root.left, p,q);
	        TreeNode right = lowestCommonAncestor(root.right, p,q);
	        
	        if (root.left!= null && root.right != null) return root;
	        
	        return left == null? right: left;
	        
	    }
	    
	 // cant path in ide    
	public TreeNode lowestCommonAncestor2(TreeNode root, TreeNode p, TreeNode q) {
		 if (root == null || root == q|| root == p) return root;
	    TreeNode l = lowestCommonAncestor2(root.left, p, q);
	    TreeNode r = lowestCommonAncestor2(root.right, p, q);
	 
	    if(l!=null && r!=null){
	        return root;
	    }else if(l==null && r==null){
	        return null;
	    }else{
	        return l==null?r:l;
	    }
	}
	
	public static void main(String[] args) {
		TreeNode t = new TreeNode(3);
		t.left = new TreeNode(5);
		t.left.right = new TreeNode(2);
		t.left.left = new TreeNode(6);
		t.right = new TreeNode(1);
		t.right.left = new TreeNode(0);
		t.right.right = new TreeNode(8);
		TreeNode p = new TreeNode(5);
		TreeNode q = new TreeNode(1);
		_236_LowestCommonAncestorofaBinaryTree lcab = new _236_LowestCommonAncestorofaBinaryTree();
		//System.out.println(lcab.lowestCommonAncestor2(t, p, q).val);
		 System.out.println(lcab.lowestCommonAncestor(t, p, q).val);
		
	}
}
