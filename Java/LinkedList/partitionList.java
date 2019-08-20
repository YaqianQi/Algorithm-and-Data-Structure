
/*
 * 
public class ListNode {
	int val;
	ListNode next;
	ListNode(int val){
		this.val = val;
		this.next = null;
	}
	
	@Override
	
	public String toString() {
	    String result = val + " ";
	    if (next != null) {
	        result += next.toString();
	    }
	    return result;
	}
	

}
 * */

public class partitionList {
	
	public static ListNode parition (ListNode head, int x) {
		if(head == null || head.next == null) return head;
		
		ListNode smallHead = new ListNode(-1);
		ListNode largeHead = new ListNode(-1);
		
		ListNode small = smallHead;
		ListNode large = largeHead;
		
		while(head!=null) {
			ListNode temp = new ListNode(head.val); 
			if(head.val >= x ) {
				large.next = temp;
				large = large.next;
			}else {
				small.next = temp;
				small = small.next ;
			}
			
			head = head.next;
		}
		
		small.next = largeHead.next;
		
		
		
		return smallHead.next;
	}
	
	public static void main(String[] args) {
		ListNode l1 = new ListNode(1);
		l1.next = new ListNode(5);
		l1.next.next  = new ListNode(3);
		l1.next.next.next = new ListNode(2);
		System.out.println("Original: " + l1.toString());
		l1 = parition (l1, 3);
		System.out.println("Parition reverse: " + l1.toString());
	}

}
