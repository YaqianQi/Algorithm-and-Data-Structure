
public class reverseLinkedList {
	public static ListNode reverse(ListNode head) {
		
		if(head == null|| head.next == null) return head;
		ListNode prev = null;
		
		while(head.next != null) {
			ListNode temp = head.next;
			head.next = prev;
			prev = head;
			head = temp;
		}
		
		
		return prev;
	}
	
	
	
	
	public static void main(String[] args) {
		ListNode l1 = new ListNode(1);
		l1.next = new ListNode(5);
		l1.next.next  = new ListNode(3);
		l1.next.next.next = new ListNode(2);
		l1.next.next.next.next = new ListNode(3);
		
		ListNode l2 = reverse(l1);
		System.out.println(l2.toString());
		
	}

}
