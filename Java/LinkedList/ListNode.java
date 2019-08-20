
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
	
	public void print() {
		System.out.println(val);
				
	}

}
