
public class reOrderList {
	
	
	public void reOrderList(ListNode head) {
		if (head == null || head.next == null ) return;
		ListNode dummy = new ListNode(-1);
		dummy.next = head;
		ListNode temp = null;
		ListNode slow = head;
		ListNode fast = head;
		ListNode l1 = head;
		while(fast!=null && fast.next!= null) {
			temp = slow;
			slow = slow.next;
			fast = fast.next.next;
		}
		
		temp.next = null;
		ListNode l2 = reverse(slow);
		merge(l1,l2);
		
	}
	
	public ListNode reverse(ListNode head) {
		ListNode prev = new ListNode(-1);
		ListNode cur = head;
		while(cur.next != null) {
			ListNode temp = cur.next;
			cur.next = prev;
			prev = cur;
			cur = temp;
		}
		return prev;
	}
	
	public void merge(ListNode l1, ListNode l2) {
		ListNode n1 = l1.next;
		ListNode n2 = l2.next;
		l1.next = l2;
		while(l1.next != null) {
			l1 = n1;
			l2 = n2;
		}
		
	}
	public static void main(String[] args) {
		
		ListNode l1 = new ListNode(1);
		l1.next = new ListNode(5);
		l1.next.next  = new ListNode(3);
		l1.next.next.next = new ListNode(2);
		l1.next.next.next.next = new ListNode(3);
		reOrderList ro = new reOrderList();
		ro.reOrderList(l1);
	}

}
