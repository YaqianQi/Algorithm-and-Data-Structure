
public class _222_CountCompleteTreeNodes {
	public int countNodes(TreeNode root) {
        int left = leftDept(root);
        int right = rightDept(root);
        if(left == right) {
        	return (1<< left) -1 ;
        }else {
        	return 1 + countNodes(root.left) + countNodes(root.right); 
        }
    }
	 int leftDept(TreeNode root) {
		 int res = 0;
		 while(root!=null) {
			 root = root.left;
			 res++;
		 }
		 return res;
	 }
	 
	 int rightDept(TreeNode root) {
		 int res = 0;
		 while(root!=null) {
			 root = root.right;
			 res++;
		 }
		 return res;
	 }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode root = new TreeNode(1);
		root.left = new TreeNode(2);
		root.right = new TreeNode(3);
		root.left.left = new TreeNode(4);
		root.left.right = new TreeNode(5);
		root.right.left = new TreeNode(6);
		_222_CountCompleteTreeNodes cct = new _222_CountCompleteTreeNodes();
		System.out.println(cct.countNodes(root));
	}

}
