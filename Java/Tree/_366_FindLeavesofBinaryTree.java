import java.util.*;
public class _366_FindLeavesofBinaryTree {
	List<List<Integer>> res;
	public List<List<Integer>> findLeaves(TreeNode root) {
        res = new ArrayList<>();
		helper(root);
        return res;
    }
	public int helper(TreeNode root) {
		if(root == null) return -1;
		int left = helper(root.left);
		int right =helper(root.right);
		int level = Math.max(left, right) + 1;
		if (res.size() == level) {
			res.add(new ArrayList<>());
		}
		res.get(level).add(root.val);
		root.left = null;
		root.right = null;
		return level;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode t = new TreeNode(1);
		t.left = new TreeNode(2);
		t.left.left = new TreeNode(4);
		t.left.right = new TreeNode(5);
		t.right = new TreeNode(3);
		_366_FindLeavesofBinaryTree flobt = new _366_FindLeavesofBinaryTree();
		System.out.println(flobt.findLeaves(t));
		
	}

}
