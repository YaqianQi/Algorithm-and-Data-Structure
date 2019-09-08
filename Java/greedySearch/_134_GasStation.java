package greedySearch;

public class _134_GasStation {
	// 一个小车车，穿梭在不同的汽车站中间，return index 这个小车车最后能逆时针转一圈回到的
    public int canCompleteCircuit(int[] gas, int[] cost) {
    	int total = 0; 
    	int sum = 0;
    	int start = 0;
    	for(int i = 0; i < gas.length; i++) {
    		total += gas[i] - cost[i];
    		sum += gas[i] - cost[i];
    		if(sum < 0) {
    			start = i+ 1;
    			sum = 0;
    		}
    	}
        return total < 0 ? -1: start;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] gas = {1,2,3,4,5};
		int[] cost = {3,4,5,1,2};
		_134_GasStation gs = new _134_GasStation();
		gs.canCompleteCircuit(gas, cost);
		//System.out.println(gs.canCompleteCircuit(gas, cost));
	}

}
