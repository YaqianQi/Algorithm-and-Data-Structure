
public class _370_RangeAddition {
	public int[] getModifiedArray(int length, int[][] updates) {
	    int[] res = new int[length];
		for (int[] update : updates) {
	    	int start = update[0];
	    	int end = update[1];
	    	int val = update[2];
	    	res[start] += val;
	    	if (end+1<length) {
	    		res[end+1]-= val;
	    	}
	    }
		return res;
	    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		_370_RangeAddition ra = new _370_RangeAddition();
		int length = 5;
		int[][] updates = new int[][] {
			{1,3,2},
			{2,4,3},
			{0,2,-2}
			};
		int[] res = ra.getModifiedArray(length,updates);
		for(int r:res) {
			System.out.print(r + " ");
		}
	}

}
