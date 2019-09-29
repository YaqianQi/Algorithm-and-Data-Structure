
public class _285_InorderSuccessorinBST {
	// find the smallest node that greater than p 
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
    	TreeNode res = null;
    	while(root!=null) {
	    	if (root.val <= p.val) {
	    		root = root.right;
	    	}else {
	    		res = root;
	    		root = root.left;
	    	}
    	}

    	return res;
    }
    
    public TreeNode inorderSuccessorRec(TreeNode root, TreeNode p) {
    	if(root == null ) return null;
    	
		if(root.val <= p.val) {
			return inorderSuccessorRec(root.right, p);
		}else {
			TreeNode temp =  inorderSuccessorRec(root.left, p);
			// 如果temp为空，那么返回上一曾
			return (temp !=null)? temp: root;
		}
    	
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode root = new TreeNode(2);
		root.left = new TreeNode(1);
		root.right = new TreeNode(3);
		TreeNode p = new TreeNode(1);
		 _285_InorderSuccessorinBST  is = new  _285_InorderSuccessorinBST();
		 System.out.println(is.inorderSuccessor(root, p).val);
		 System.out.println(is.inorderSuccessorRec(root, p).val);
	}

}
