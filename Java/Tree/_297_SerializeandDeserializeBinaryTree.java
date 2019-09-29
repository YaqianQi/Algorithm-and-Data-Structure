import java.util.*;
public class _297_SerializeandDeserializeBinaryTree {
	// lavel order ?
	// Encodes a tree to a single string.
	
	// as "[1,2,3,null,null,4,5]"
	
	// Encodes a tree to a single string.
	public String serialize(TreeNode root) {
	    ArrayList<String> list = new ArrayList<>();
	    LinkedList<TreeNode> q = new LinkedList<>();
	    q.offer(root);
	 
	    while (!q.isEmpty()) {
	        TreeNode h = q.poll();
	        if (h == null) {
	            list.add("#");
	        } else {
	            list.add("" + h.val);
	            q.offer(h.left);
	            q.offer(h.right);
	        }
	    }
	 
	    return String.join(",", list);
	}
	 
	// Decodes your encoded data to tree.
	public TreeNode deserialize(String data) {
	    String[] arr = data.split(",");
	    if (arr[0].equals("#")) {
	        return null;
	    }
	 
	    TreeNode root = new TreeNode(Integer.parseInt(arr[0]));
	    LinkedList<TreeNode> q = new LinkedList<>();
	    q.offer(root);
	 
	    int i = 1;
	 
	    while (!q.isEmpty()) {
	        TreeNode h = q.poll();
	        if (h != null) {
	            TreeNode left = null;
	            if (!arr[i].equals("#")) {
	                left = new TreeNode(Integer.parseInt(arr[i]));
	            }
	            h.left = left;
	            q.offer(left);
	            i++;
	 
	            TreeNode right = null;
	            if (!arr[i].equals("#")) {
	                right = new TreeNode(Integer.parseInt(arr[i]));
	            }
	            h.right = right;
	            q.offer(right);
	            i++;
	        }
	    }
	 
	    return root;
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeNode t = new TreeNode(1);
		t.left = new TreeNode(2);
		t.right = new TreeNode(3);
		t.right.left = new TreeNode(4);
		t.right.right = new TreeNode(5);
		_297_SerializeandDeserializeBinaryTree sdb = new _297_SerializeandDeserializeBinaryTree();
		String data = "1,2,3,#,#,4,5,#,#,#,#";
		System.out.println(sdb.serialize(t));
		System.out.println(sdb.deserialize(data));

	}

}
