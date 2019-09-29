
// convert sorted liste to binary search tree
public class _109_ConvertSortedListtoBinarySearchTree {
	 public TreeNode sortedListToBST(ListNode head) {
		 if (head == null) return null;
		 return helper(head, null);
	 } 
	 
	 public TreeNode helper(ListNode head, ListNode tail) {
		 if(head == tail) return null;
		 ListNode fast = head;
		 ListNode slow = head;
		 while (fast!= tail && fast.next!=tail) {
			 fast = fast.next.next;
			 slow = slow.next;
		 }
		 TreeNode root = new TreeNode(slow.val);
		 root.left = helper(head,slow);
		 root.right = helper(slow.next,tail);
		 return root;
		 
	 }
	
	 public static void main(String[] args) {
		// TODO Auto-generated method stub
		 ListNode head = new ListNode(-10);
		 head.next = new ListNode(-3);
		 head.next.next = new ListNode(0);
		 head.next.next.next = new ListNode(5);
		 head.next.next.next.next = new ListNode(9);
		 _109_ConvertSortedListtoBinarySearchTree cslbst = new _109_ConvertSortedListtoBinarySearchTree();
		 System.out.println(cslbst.sortedListToBST(head).val);
	}

}
