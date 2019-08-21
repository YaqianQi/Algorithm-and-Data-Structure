
public class reverseKthGroup {
	public static ListNode reverseKGroup(ListNode head, int k) {
		if (head == null || head.next == null)return head;
		int count = 0;
		
		ListNode cur = head;
		while(cur!=null && count!=k) {
			cur = cur.next;
			count++;
		}
		if(count == k) {
			reverseKGroup(cur,k);
			while (count -- >0) {
				ListNode temp = head.next;
				head.next = cur;
				cur = head;
				head = temp;
			}
			head = cur;
		}
		return head;
		
	}
	
	
	
	public static void main(String [] args) {
		ListNode l1 = new ListNode(1);
		l1.next = new ListNode(5);
		l1.next.next  = new ListNode(3);
		l1.next.next.next = new ListNode(2);
		//l1.next.next.next.next = new ListNode(3);
		
		ListNode l2 = reverseKGroup(l1, 3);
		System.out.println(l2.toString());
	}

}
