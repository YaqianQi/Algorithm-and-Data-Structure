import java.util.*;
public class _5343_ConstructTargetArrayWithMultipleSums {
	public boolean isPossible(int[] target) {
		PriorityQueue<Integer> q = new PriorityQueue<>((a,b)->(b-a));
		int sum = 0;
		int n = target.length;
		for (int num : target) {
			q.offer(num);
			sum+= num;
		}
		while(sum > n) {
			int val = q.poll();
			int temp = val - (sum - val);
			if (temp < 1) {return false;}
			q.offer(temp);
			sum -= (val - temp);
		}	
		return sum == n;
	}
	
	public boolean isPossible2(int[] target) {
		Arrays.sort(target);
		int sum = 0;
		int n = target.length;
		for (int num : target) {
			sum+= num;
		}
		while(sum > n) {
			int val = target[n-1];
			int temp = val - (sum - val);
			if (temp < 1) {return false;}
			target[n-1] = temp;
			sum -= (val - temp);
			Arrays.sort(target);
		}	
		return sum == n;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] target = {9,3,5};
		_5343_ConstructTargetArrayWithMultipleSums  cs = new _5343_ConstructTargetArrayWithMultipleSums ();
		System.out.println(cs.isPossible2(target));
	}

}
