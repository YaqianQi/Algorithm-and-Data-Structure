// space is larger than binary index tree

class TreeNode{
	int start; 
	int end; 
	int sum; 
	TreeNode leftChild; 
	TreeNode rightChild;
	
	//构建一个树 
	public TreeNode(int left, int right, int sum) {
		this.start = left;
		this.end = right;
		this.sum = sum;
	}
	public TreeNode(int left, int right) {
		this.start = left;
		this.end = right;
		this.sum = 0;
	}
}



public class _307_RangeSumQueryMutableSegmentTree {
	TreeNode root = null;
    // 构造函数，nums, start, end
	public _307_RangeSumQueryMutableSegmentTree(int[] nums) {
		if(nums==null || nums.length==0)
            return;
 
        this.root = buildTree(nums, 0, nums.length-1);  
		
	}
	// ipdate 函数， 在i的位置updateval
	void update(int i , int val) {
		updateHelper(root, i, val);
	}
	void updateHelper(TreeNode root, int i , int val) {
		if(root==null)
            return;
        int mid = root.start + (root.end-root.start)/2;
        if(i<=mid){
            updateHelper(root.leftChild, i, val);
        }else{
            updateHelper(root.rightChild, i, val);
        }
        // to the end 
        if(root.start==root.end&& root.start==i){
            root.sum=val;
            return;
        }
 
        root.sum=root.leftChild.sum+root.rightChild.sum;
	}
	public int sumRange(int i, int j) {
		return sumRangeHelper(root, i, j);
	}
	public int sumRangeHelper(TreeNode root, int i , int j) {
	      if(root==null || j<root.start || i > root.end ||i>j )
	            return 0;
	 
	        if(i<=root.start && j>=root.end){
	            return root.sum;
	        }    
	        int mid = root.start + (root.end-root.start)/2;
	        int result = sumRangeHelper(root.leftChild, i, Math.min(mid, j))
	                    +sumRangeHelper(root.rightChild, Math.max(mid+1, i), j);
	 
	        return result;
	}
	
	public TreeNode buildTree(int[] nums, int i , int j) {
		if(nums==null || nums.length==0|| i>j)
            return null;
 
        if(i==j){
            return new TreeNode(i, j, nums[i]);
        }
 
        TreeNode current = new TreeNode(i, j);
 
        int mid = i + (j-i)/2;
 
        current.leftChild = buildTree(nums, i, mid);
        current.rightChild = buildTree(nums, mid+1, j);
 
        current.sum = current.leftChild.sum+current.rightChild.sum;
 
        return current;
		
	}
	
	
	
	
	public static void main(String[] args) {
	   	int[] nums = new int[] {1,3,5};
	   	_307_RangeSumQueryMutableSegmentTree rsm = new _307_RangeSumQueryMutableSegmentTree(nums);
    	System.out.println(rsm.sumRange(0, 2));
    	rsm.update(1, 2);
    	System.out.println(rsm.sumRange(0, 2));
	}
}
